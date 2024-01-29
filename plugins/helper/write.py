import asyncio
import requests
from requests import get
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp

# Add the owner's user ID here
owner_id = 1843754190

@Client.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.from_user.id != owner_id:
        await message.reply_text("ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ ɪɴ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ : /write ʏᴏᴜʀ ᴛᴇxᴛ ✍️")
        return

    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await message.reply_text("<b>ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...</b>")
        API = f"https://api.sdbots.tech/write?text={text}"
        req = requests.get(API).url
        await message.reply_photo(
            photo=req,
            caption=(MALIK.format(message.from_user.mention, temp.U_NAME, temp.B_NAME, message.chat.title, req)),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📑 ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ 📑", url=f"{req}")]]
            ),
        )
        await asyncio.sleep(0.3)
        await m.delete()

MALIK = """<b>sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ ✔️\n\n🔊 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ - {}.\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ - <a href=https://t.me/{}>{}</a>,\n👥 ɢʀᴏᴜᴘ - {}\n🖇 ʟɪɴᴋ - {}</b>"""

MALIKK = """<b>ʜᴇʏ {}.\n\nᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...\n\nᴡʀɪᴛɪɴɢ ʏᴏᴜʀ ᴛᴇxᴛ...</b>"""
        
