import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information

SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '28341884'))
API_HASH = environ.get('API_HASH', 'ca0c9295ce3ec910fd6f49e99970d9a8')
BOT_TOKEN = environ.get('BOT_TOKEN', "5852539727:AAG4e5PfLvTMLljlFHC2q4MMK-zsCPrJ_qs")

# Bot settings

CACHE_TIME = int(environ.get('CACHE_TIME', 300))

USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

PICS = (environ.get('PICS', 'https://te.legra.ph/file/1d0a2c18fe400858da722.jpg')).split()

# Admins, Channels & Users

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5676827158''6230062482').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001980108097').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5676827158''6230062482').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001918172990')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://aashukr5578:mEkWyhhwVqMFIdPY@cluster0.z49nllu.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files)

# Others

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001980108097'))

SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Movie_BIND')

P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)

IMDB = is_enabled((environ.get('IMDB', "False")), False)

SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "FILE : <code>{file_name}</code>\nSize : <i>{file_size}</i>\nCAPTION: {file_caption}\n<b>Join [Here](https://t.me/+Ph71PzEOzSM4ZTJl)</b>")

BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "FILE : <code>{file_name}</code>\nSize : <i>{file_size}</i>\nCAPTION: {file_caption}\n<b>Join [Here](https://t.me/+Ph71PzEOzSM4ZTJl)</b>")

IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")

LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)

SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)

MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]

MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)

PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)

PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"

LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")

LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")

LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")

LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")

LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")

LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")

LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")

LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

# Extra Features By TamilanBotsZ 💥

HOW_TO_DOWNLOAD = environ.get("HOW_TO_DOWNLOAD", "https://t.me/Ggjsns/9")

AUTO_DELETE_SECONDS = int(environ.get('AUTO_DELETE_SECONDS', 300))

FILE_REQ_CHANNEL = int(environ.get('FILE_REQ_CHANNEL', -1001961567517))

SHORTNER_SITE = environ.get("SHORTNER_SITE", "api.omegalinks.in/shortLink")

SHORTNER_API = environ.get("SHORTNER_API", "69767ef02ba3b32e7ecb823610cd3f107a88c99b")
