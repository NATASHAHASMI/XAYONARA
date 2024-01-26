import asyncio
import requests
from requests import get
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp


@Client.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        print(f"Text to write: {text}")  # Print the text to be written
        m = await message.reply_text("<b>ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...</b>")
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        print(f"Generated URL: {req}")  # Print the generated URL
        await message.reply_photo(
            photo=req,
            caption=(MALIK.format(message.from_user.mention, temp.U_NAME, temp.B_NAME, message.chat.title, req)),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📑 ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ 📑", url=f"{req}")]]
            ),
        )
        await asyncio.sleep(0.3)
        await m.delete()
        
