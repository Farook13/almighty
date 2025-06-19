class script(object):
    START_TXT = """𝖸𝗈...𝖸𝗈... {} 💖

<b><u>𝖨'𝗆 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖠𝗎𝗍𝗈-𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖬𝖾 𝖠𝗌 𝖠 𝖠𝗎𝗍𝗈-𝖿𝗂𝗅𝗍𝖾𝗋 𝗂𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉</u></b>

<i>𝖨𝗍𝗌 𝖤𝖺𝗌𝗒 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾; 𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇, 
𝖳𝗁𝖺𝗍𝗌 𝖠𝗅𝗅, 𝗂 𝗐𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖳𝗁𝖾𝗋𝖾...🤓🤪</i>

<b>😎 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖻𝗒 @Farook13</b>"""

    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    STATUS_TXT2 = """📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

𝗗𝗕 𝟭
𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌         - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB

𝗗𝗕 𝟮
𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌         - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB

𝗗𝗕 𝟯
📦 𝖴𝗌𝖾𝗋𝗌            - <code>{}</code>
🖥️ 𝖢𝗁𝖺𝗍𝗌            - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""


    MOVREQ_TXT = """<b><blockquote> 🚸 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖱𝗎𝗅𝖾𝗌 🚸

🌿ഇംഗ്ലീഷ് ഭാഷയിൽ തന്നെ movies/Series റിക്വസ്റ്റ് ചെയ്യുക 
🌿റിലീസ് ആവാത്ത മൂവീസ് ചോദിച്ചു സമയം കളയണ്ട 
🌿സിനിമയുടെ പേര് വർഷം എന്നിവ മാത്രം അയച്ചാൽ മതി 
🌿ഉണ്ടോ,തരുവോ,മൂവി,ലിങ്ക്,സിനിമ എന്നീ ഡയലോഗ്കൾ വേണ്ട കേട്ടോ 
🌿സ്റ്റൈലിഷ് അക്ഷരങ്ങൾ ഉപയോഗിക്കരുത് 
🌿സിംബൽസിന്റെ ആവശ്യവും ഇവിടെ വരുന്നില്ല.. അത് ഒഴിവാക്കുക(+:;'!-|...𝖾𝗍𝖼)</blockquote></b>"""
    
    NORSLTS = """𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>


𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <code>{}</code>"""


    CUSTOM_FILE_CAPTION = """<b>𝐻𝑒𝑙𝑙𝑜 👋 {mention} 😍
    
{file_caption}

╔═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╗ 
➲ <a href='https://t.me/batmancineflix'>@batmancineflix</a>
➲ <a href='https://t.me/batmancineflix'>@batmancineflix</a>
╚═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╝
</b>"""
