import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "7217645"))
API_HASH = getenv("API_HASH", "78ba6352dd5cdc166fdef5aa84ba7c67")

BOT_TOKEN = getenv("BOT_TOKEN", "6292817735:AAEpf5QdF_TmY8NKwC9qv1e5gPMaEeZ4Ngo")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001564289796"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Makise")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1793699293").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Roninopp/Musicomp")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Imperial_arena")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Ronin_Fighters_Fd")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQBdya6Czxgx-D5krI_lwhHe45KduhWGAOM10V9WtlsO4Ft0fKNpNl-tCEHxNKkpAXvl50zMYgb70-dvWBb3tE8bg6fwQGpeebvzJbl9YAgdEXlc5acKpHZqsEbULe_4MqXCNjL5K6sUuVunEwRJKkkjy7p_aMrbIy8hRi0O8Aos6xEuyLcqng7DyVQ_W-C-eMyaIOVlsgA-WUUOnabHkwy9IaOEgaliiBqidQEfgcKHxNl-VOw3cx_WWXbBr4SgIjZmlfTZxRZPdMuU96yw8CXZxhVlCOEF10S8xL1fiFkMroxPaRfHwb4Vx_o3jod2T-UDNemnPPPgbPFuFZAQ-VnyAAAAAUK509kA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/e833bcbb6ab8db805825c.jpg"
