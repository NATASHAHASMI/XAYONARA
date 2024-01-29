class script(object):
    START_TXT = """<b><i>ʜᴇʏ 😎.</i></b> <b>{}</b> {} <b><i>\nɪ ᴀᴍ ᴘᴏᴡᴇʀꜰᴜʟʟ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ ᴘʀᴏᴠɪᴅᴇʀ ʙᴏᴛ ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ.</i></b>

<spoiler><b>🔋 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ - <a href='https://telegram.me/xayonara_contact_bot'>xᴀʏᴏɴᴀʀᴀ</a></b></spoiler>"""

    GSTART_TXT = """<b><i>ʜᴇʏ 😎.</i></b> <b>{}</b> <b><i>ɪ ᴀᴍ ᴘᴏᴡᴇʀꜰᴜʟʟ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ ᴘʀᴏᴠɪᴅᴇʀ ʙᴏᴛ ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ.</i></b>

<spoiler><b>🔋 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ - <a href='https://telegram.me/xayonara_contact_bot'>xᴀʏᴏɴᴀʀᴀ</a></b></spoiler>"""
   
    HELP_TXT = """<b>Hᴇʏ {}
Hᴇʀᴇ Is Tʜᴇ Mʏ Cᴏᴍᴍᴀɴᴅs.</b>"""

    ABOUT_TXT = """<b>
 🤖 ᴍʏ ɴᴀᴍᴇ : {}
 👨‍💻 ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/XAYOONARA'>𝑿𝑨𝒀𝑶𝑵𝑨𝑹𝑨</a>
 📚 ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
 📝 ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>
 ♻️ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
 📡 ʜᴏsᴛᴇᴅ ᴏɴ  : <a href='https://www.heroku.com/'>Heroku</a>
 🥶 ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ3.0 [sᴛᴀʙʟᴇ​]</b>"""

    ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>"""
    
    USERS_TXT = """Uꜱᴇʀꜱ Cᴏᴍᴍᴀɴᴅs
<b>ɴᴏᴛᴇ:</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ Uꜱᴇʀꜱ Cᴏᴍᴍᴀɴᴅs ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ
Cʜᴇᴄᴋ Aɴᴅ Usᴀɢᴇ:
• /start - <code>ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ</code>
• /stats - <code>ᴄʜᴇᴄᴋ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ</code>
• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>"""

    
    STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>\n<b>⍟─────[ ʙᴏᴛ sᴛᴀᴛᴜ𝗌 ]─────⍟</b>"""

    
    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    SELECT = """ ᴜsᴇ ʙᴇʟᴏᴡ ᴏᴘᴛɪᴏɴs ᴛᴏ ꜰɪɴᴅ ʏᴏᴜʀ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs ꜰᴀsᴛʟʏ.⚡ """
    
    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """Sᴘᴇʟʟɪɴɢ Mɪꜱᴛᴀᴋᴇ Bʀᴏ ‼️
ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ 😊 Cʜᴏᴏꜱᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴏɴᴇ ʙᴇʟᴏᴡ 👇"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃

ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Uncharted or Uncharted 2022 or Uncharted En

ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""

    I_CUD_NT = """Sᴘᴇʟʟɪɴɢ Mɪꜱᴛᴀᴋᴇ Bʀᴏ ‼️
ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ 😊 Cʜᴏᴏꜱᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴏɴᴇ ʙᴇʟᴏᴡ 👇"""

    MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    DISCLAIMER_TXT = """
    𝑯𝒆𝒚 {}.😈
    <b><i>Tʜɪꜱ Iꜱ Aɴ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ.

Aʟʟ Tʜᴇ Fɪʟᴇꜱ Iɴ Tʜɪꜱ Bᴏᴛ Aʀᴇ Fʀᴇᴇʟʏ Aᴠᴀɪʟᴀʙʟᴇ Oɴ Tʜᴇ Iɴᴛᴇʀɴᴇᴛ Oʀ Pᴏꜱᴛᴇᴅ Bʏ Sᴏᴍᴇʙᴏᴅʏ Eʟꜱᴇ.
Jᴜꜱᴛ Fᴏʀ Eᴀꜱʏ Sᴇᴀʀᴄʜɪɴɢ Tʜɪꜱ Bᴏᴛ ɪꜱ Iɴᴅᴇxɪɴɢ Fɪʟᴇꜱ Wʜɪᴄʜ Aʀᴇ Aʟʀᴇᴀᴅʏ Uᴘʟᴏᴀᴅᴇᴅ Oɴ Tᴇʟᴇɢʀᴀᴍ.
Wᴇ Rᴇꜱᴘᴇᴄᴛ Aʟʟ Tʜᴇ Cᴏᴘʏʀɪɢʜᴛ Lᴀᴡꜱ Aɴᴅ Wᴏʀᴋꜱ Iɴ Cᴏᴍᴘʟɪᴀɴᴄᴇ Wɪᴛʜ Dᴍᴄᴀ Aɴᴅ Eᴜᴄᴅ.
Iꜰ Aɴʏᴛʜɪɴɢ Iꜱ Aɢᴀɪɴꜱᴛ Lᴀᴡ Pʟᴇᴀꜱᴇ Cᴏɴᴛᴀᴄᴛ Mᴇ Sᴏ Tʜᴀᴛ Iᴛ Cᴀɴ Bᴇ Rᴇᴍᴏᴠᴇᴅ Aꜱᴀᴘ.
ɪᴛ ɪꜱ Fᴏʀʙɪʙʙᴇɴ Tᴏ Dᴏᴡɴʟᴏᴀᴅ, Sᴛʀᴇᴀᴍ, Rᴇᴘʀᴏᴅᴜᴄᴇ, Sʜᴀʀᴇ ᴏʀ Cᴏɴꜱᴜᴍᴇ Cᴏɴᴛᴇɴᴛ Wɪᴛʜᴏᴜᴛ Exᴘʟɪᴄɪᴛ Pᴇʀᴍɪꜱꜱɪᴏɴ Fʀᴏᴍ Tʜᴇ Cᴏɴᴛᴇɴᴛ Cʀᴇᴀᴛᴏʀ Oʀ Lᴇɢᴀʟ Cᴏᴘʏʀɪɢʜᴛ Hᴏʟᴅᴇʀ.
ɪꜰ Yᴏᴜ Bᴇʟɪᴇᴠᴇ Tʜɪꜱ Bᴏᴛ ɪꜱ Vɪᴏʟᴀᴛɪɴɢ Yᴏᴜʀ Iɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ Pʀᴏᴘᴇʀᴛʏ, Cᴏɴᴛᴀᴄᴛ Tʜᴇ Rᴇꜱᴘᴇᴄᴛɪᴠᴇ Cʜᴀɴɴᴇʟꜱ Fᴏʀ Rᴇᴍᴏᴠᴀʟ.
Tʜᴇ Bᴏᴛ Dᴏᴇꜱ Nᴏᴛ Oᴡɴ Aɴʏ Oꜰ Tʜᴇꜱᴇ Cᴏɴᴛᴇɴᴛꜱ, Iᴛ Oɴʟʏ Iɴᴅᴇx Tʜᴇ Fɪʟᴇꜱ Fʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ.</b></i> 

<b><spoiler>🔋 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://telegram.me/xayonara_contact_bot'>Xᴀʏᴏɴᴀʀᴀ</a></b></spoiler>"""

    
    SHORTLINK_INFO = """
<b>🌟 "PREMIUM MEMBERSHIP" 🌟

🥁 Buy 'Premium Membership' & Get Movies, Series, etc., In Direct Files Without Any 🔗Links Or Ads...!

💫 Iɴ Oɴʟʏ 40/- Pᴇʀ Mᴏɴᴛʜ.....
Any Doubts or Not Connecting? Contact Me <a href='https://t.me/XAYOONARA'>𝑿𝑨𝒀𝑶𝑵𝑨𝑹𝑨</a></b>"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    SINFO = """
😁 ᴊᴏɪɴ ʙᴀᴄᴋᴜᴘ ᴄʜᴀɴɴᴇʟ & ᴛʀʏ ᴀɢᴀɪɴ ⚡"""

    NORSLTS = """ 
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """<b>🏷 Tɪᴛʟᴇ :</b><code>{file_name}</code>\n\n<b>📢 Jᴏɪɴ :</b> <b>@Moviestudioabhi</b> ❤️‍🔥""" 

    IMDB_TEMPLATE_TXT = """
<b>Query: {qurey}

IMDb Data:

<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
☀️ Languages : <code>{languages}</code>
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>


⏰Result Shown in: {remaining_seconds} <i>seconds</i> 🔥

Requested by : {message.from_user.mention}</b>"""
    
 
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """

BOT WORKING PROPERLY ⚡"""


    DEVELOPER_TXT = """
special Thanks To ❤️ Developers -

-Dev 1 [Owner of this bot ]<a href='https://t.me/XAYOONARA'>XAYONARA</a>
"""



    
