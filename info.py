import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '22582906'))
API_HASH = environ.get('API_HASH', 'e3096dde3e27c72a50e0e53d8ab23d6a')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7861690278').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/darkworld008")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002635667025'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/UniformMoviesGroup')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002487267521 -1002185462771 -1002769886785').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://bibekkumarmahato0:echW1UgCBhCDdbEF@cluster0.lbxlub4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DATABASE_NAME = environ.get('DATABASE_NAME', "Sandhu")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Akmovie')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002635667025'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/uRY.jpg')
START_IMG = environ.get('START_IMG', 'https://envs.sh/fHy.jpg')
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1002783635871'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002783635871'))
URL = environ.get('URL', 'sandhubotz.onrender.com')
STICKERS_IDS = ('CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002635667025'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/UniformHelp/451/554")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "08a2c5a3420f0449b1f8090d2caf62813dc7a57f")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'zegalinks.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "dd17fd90a1db7e93013784016d13a4aa7a29ea76")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'pocolinks.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "e78e5f774a9dede8f6b3d155a1fea041a35bb720")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'linkcents.com')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "12000"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "86400"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '-1002810021160')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002681593596'))
request_channel = environ.get('REQUEST_CHANNEL', '')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002581890930'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002502729198'))

AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : False,
    'all_files_post_mode' : False
}
