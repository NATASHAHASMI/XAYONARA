class script(object):
    START_TXT = """<b> ʜᴇʏ 😎. <i>{}</i> {},</b>
    
<blockquote><i><b>Iᴍ Tʜᴇ Mᴏsᴛ Aᴅᴠᴀɴᴄᴇ Aɪ Pᴏᴡᴇʀᴅ 🤖 Aᴜᴛᴏ Fɪʟᴛᴇʀ Bᴏᴛ..
Jᴜꜱᴛ Sᴇɴᴅ Mᴇ Aɴʏ Mᴏᴠɪᴇꜱ & Sᴇʀɪᴇꜱ Nᴀᴍᴇ Aɴᴅ Sᴇᴇ Mʏ Pᴏᴡᴇʀ..✨</b></i></blockquote>
<pre><i><b>ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴜsᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ 🤞🏻</b></i></pre>

<spoiler><b>🔋 Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ - <a href='https://telegram.me/xayonara_contact_bot'>✘ 𝐚 𝐲 𝐨 𝐧 𝐚 𝐫 𝐚.</a></b></spoiler>
"""

    GSTART_TXT = """<b><i>ʜᴇʏ 😎.</i></b> <b>{}</b> <b><i><blockquote>ɪ ᴀᴍ ᴘᴏᴡᴇʀꜰᴜʟʟ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ ᴘʀᴏᴠɪᴅᴇʀ ʙᴏᴛ ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ.</blockquote></i></b>

<spoiler><b>🔋 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ - <a href='https://telegram.me/xayonara_contact_bot'>xᴀʏᴏɴᴀʀᴀ</a></b></spoiler>"""
   
    HELP_TXT = """<b><pre>Hᴇʏ</pre></b> {}
<b><blockquote>Hᴇʀᴇ Is Tʜᴇ Mʏ Cᴏᴍᴍᴀɴᴅs.</blockquote></b>"""

    ABOUT_TXT = """<b><pre>Hᴇʏ 😈 {},</pre>
    
🧑‍💻 ᴍʏ ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/XAYOONARA'>✘ 𝐚 𝐲 𝐨 𝐧 𝐚 𝐫 𝐚.</a>
📚 ʟɪʙʀᴀʀʏ: <a href="https://github.com/Mayuri-Chan/pyrofork">ᴘʏʀᴏғᴏʀᴋ</a>
📡 ᴄʜɪʟʟɪɴɢ ᴏɴ : <a href="https://aws.amazon.com/">Vᴘꜱ</a>
⚙️ ʙʀᴀɪɴ ғᴜᴇʟᴇᴅ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
📝 ᴄᴏᴅɪɴɢ ᴍᴜsᴄʟᴇs : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ 3</a>
</b>"""

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

    
    STATUS_TXT = """<b><blockquote>Tᴏᴛᴀʟ Fɪʟᴇs Fʀᴏᴍ Bᴏᴛʜ DBs: <code>{}</code></blockquote>

<blockquote><b>Bᴏᴛ Usᴇʀs ᴀɴᴅ Cʜᴀᴛs Cᴏᴜɴᴛ</b></blockquote>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>

<blockquote><b>Pʀɪᴍᴀʀʏ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛɪsᴛɪᴄs</b></blockquote>
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>

<blockquote><b>Sᴇᴄᴏɴᴅᴀʀʏ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛɪsᴛɪᴄs</b></blockquote>
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
</b>\n<b>⍟─────[ ʙᴏᴛ sᴛᴀᴛᴜ𝗌 ]─────⍟</b>"""

    
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

    CUDNT_FND = """<blockquote><b><i>Sᴘᴇʟʟɪɴɢ Mɪꜱᴛᴀᴋᴇ Bʀᴏ ‼️
ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ 😊 Cʜᴏᴏꜱᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴏɴᴇ ʙᴇʟᴏᴡ 👇</i></b></blockquote>"""

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
    <b><i><pre><code class="language-Tʜɪꜱ Iꜱ Aɴ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ.">⚡️</pre>

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

    CAPTION = """<b>🏷 Tɪᴛʟᴇ :</b><pre><b><i>{file_name}</i></b></pre>\n\n<blockquote><b>📢 Jᴏɪɴ </b></blockquote>: <b>@Moviestudioabhi</b> ❤️‍🔥\n\n<blockquote><b><i><a href='https://graph.org/All-Solution-In-One-Page-08-03'>ᴘʟᴇᴀꜱᴇ ʀᴇᴀᴅ ʙᴇꜰᴏʀᴇ ᴡᴀᴛᴄʜɪɴɢ.📚</a></i></b></blockquote>""" 

    IMDB_TEMPLATE_TXT = """
    <b>📌{title}.</b>
╭──────────────────────
<b>‣ Lᴀɴɢᴜᴀɢᴇꜱ </b>» <code>{languages}</code>
<b>‣ Gᴇɴʀᴇꜱ » {genres}</b>
<b>‣ Yᴇᴀʀ » {year}</b>
<b>‣ Rᴀᴛɪɴɢ » {rating} / 10</b>
╰──────────────────────
<b><i>📢 <a href='t.me/moviestudioabhi'>Jᴏɪɴ Bᴀᴄᴋᴜᴘ</a></i></b>
"""
    
 
    RESTART_TXT = """
<b><pre>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b></pre>"""

    LOGO = """

BOT WORKING PROPERLY ⚡"""


    DEVELOPER_TXT = """
special Thanks To ❤️ Developers -

-Dev 1 [Owner of this bot ]<a href='https://t.me/XAYOONARA'>XAYONARA</a>
"""



    
