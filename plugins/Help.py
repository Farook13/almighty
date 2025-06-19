from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("help"))
async def generate_link(client, message):
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        await message.reply("<b>❗️How to Search Movies Here❓\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n1. Just Send Movie Name and Movie Released Year Correctly.\n<blockquote>(Check Google for Correct Movie Spelling and Movie Released Year)</blockquote>\n\nExamples: -\nOppam 2016\nBaahubali 2015 1080p\n<blockquote>(For Getting only 1080p Quality Files)</blockquote>\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nBaahubali 2015 Malayalam\nBaahubali 2015 Tamil\n<blockquote>(For Dubbed Movie Files)</blockquote>\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❗️On Android, Better Use VLC Media Player For Watch Movie's.\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n</b>")
        return
