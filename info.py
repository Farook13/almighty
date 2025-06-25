import re
from os import environ
from Script import script
from pyrogram import utils as pyroutils

# Strict pattern for Telegram channel IDs (e.g. -1001234567890)
id_pattern = re.compile(r"^-100\d{10}$")

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'autodelete')
API_ID = int(environ.get("API_ID", "19071424"))
API_HASH = environ.get("API_HASH", "c4b3e298cc50fd4cc563ae75ee882948")
BOT_TOKEN = environ.get("BOT_TOKEN", "7693803634:AAHYtfbdaFtDkYebZYWHUE7R4qgZ6Txdhao")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = environ.get('PICS', '').split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5032034594').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002397004421').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

NORES_CHANNEL = environ.get("NORES_CHANNEL", '-1002332361885')

# ✅ Corrected REQ_CHANNEL logic
REQ_CHANNEL1 = environ.get("REQ_CHANNEL1")
REQ_CHANNEL1 = int(REQ_CHANNEL1) if REQ_CHANNEL1 and id_pattern.match(REQ_CHANNEL1) else False

REQ_CHANNEL2 = environ.get("REQ_CHANNEL2")
REQ_CHANNEL2 = int(REQ_CHANNEL2) if REQ_CHANNEL2 and id_pattern.match(REQ_CHANNEL2) else False

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://farook:farook@cluster0.aaed9bf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://daddybro:daddybro@cluster0.lw0tu70.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI3 = environ.get('DATABASE_URI3', "mongodb+srv://Nigga:nigga@cluster0.neynray.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'TELEGRAM_FILES')

# Auto Approve
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour request has been approved")
APPROVED = environ.get("APPROVED_WELCOME", "off").lower()

# Peer ID fix
pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

# Other Settings
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1002332361885"))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-0').split()]
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'cine_flix01')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "False"), False)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", script.CUSTOM_FILE_CAPTION)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "False"), False)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "False"), False)

# Logging Setup Summary
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending files directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is found, filename and file size will be shown in a single button instead of two.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled, filename and file size will be shown as separate buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION found, default captions will be used.\n")
LOG_STR += ("Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled, bot will suggest related movies if not found.\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY mode is disabled.\n")
LOG_STR += (f"MAX_LIST_ELM is set; long lists will be shortened to the first {MAX_LIST_ELM} elements.\n" if MAX_LIST_ELM else "Full cast/crew list will be shown unless MAX_LIST_ELM is set.\n")
LOG_STR += f"Your current IMDB template is:\n{IMDB_TEMPLATE}"
