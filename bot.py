import sys
import glob
import importlib
from pathlib import Path
import logging
import logging.config
from pyrogram import Client, __version__, idle
from pyrogram.raw.all import layer
from database.ia_filterdb import Media, Media2, choose_mediaDB, db as clientDB
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR, LOG_CHANNEL, PORT, SECONDDB_URI
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script 
from datetime import date, datetime 
import pytz
from aiohttp import web
from plugins import web_server
import asyncio
from util.keepalive import ping_server
from lazybot import LazyPrincessBot
from lazybot.clients import initialize_clients
from sample_info import tempDict

# Configure logging
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

# Initialize LazyPrincessBot and event loop
LazyPrincessBot.start()
loop = asyncio.get_event_loop()

# Load plugins from directory
ppath = "plugins/*.py"
files = glob.glob(ppath)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem.replace(".py", "")
        plugins_dir = Path(f"plugins/{plugin_name}.py")
        import_path = "plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
        load = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(load)
        sys.modules["plugins." + plugin_name] = load
        print("Lazy Imported => " + plugin_name)

# Check if running on Heroku
ON_HEROKU = False  # Adjust as per your deployment environment

async def main():
    print('\n')
    print('Initializing Lazy Bot')

    # Initialize clients and bot information
    bot_info = await LazyPrincessBot.get_me()
    LazyPrincessBot.username = bot_info.username
    await initialize_clients()

    # Load banned users and chats
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats

    # Ensure indexes in primary and secondary databases
    await Media.ensure_indexes()
    await Media2.ensure_indexes()

    # Check database space and choose the appropriate DB
    stats = await clientDB.command('dbStats')
    free_dbSize = round(512 - ((stats['dataSize'] / (1024 * 1024)) + (stats['indexSize'] / (1024 * 1024))), 2)
    if SECONDDB_URI and free_dbSize < 10:
        tempDict["indexDB"] = SECONDDB_URI
        logging.info(f"Since Primary DB has only {free_dbSize} MB left, Secondary DB will be used to store data.")
    elif SECONDDB_URI is None:
        logging.error("Missing second DB URI! Exiting...")
        exit()
    else:
        logging.info(f"Since primary DB has enough space ({free_dbSize}MB) left, it will be used for storing data.")

    # Choose media database
    await choose_mediaDB()

    # Get bot information
    me = await LazyPrincessBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    LazyPrincessBot.username = '@' + me.username

    # Log startup information
    logging.info(f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    logging.info(script.LOGO)

    # Send restart message
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await LazyPrincessBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))

    # Setup web server
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()

    # Start idle
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')
    
