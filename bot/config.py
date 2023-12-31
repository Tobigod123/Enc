#    This file is part of the Encoder distribution.
#    Copyright (c) 2021 Danish_00, Nubuki-all
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/Nubuki-all/Enc/blob/main/License> .
import traceback

from decouple import config


class Config:
    def __init__(self):
        try:
            ALWAYS_DEPLOY_LATEST = config("ALWAYS_DEPLOY_LATEST", default=False, cast=bool)
    ALLOW_ACTION = config("ALLOW_ACTION", default=True, cast=bool)
    APP_ID = config("APP_ID", default=3847632, cast=int)
    API_HASH = config("API_HASH", default="1a9708f807ddd06b10337f2091c67657")
    ARIA2_PORT = config("ARIA2_PORT", default=6800, cast=int)
    BOT_TOKEN = config("BOT_TOKEN", default="6312969509:AAE4CYabaJQceMV1fB3fRFRnbDRljk_je_c")
    CACHE_DL = config("CACHE_DL", default=False, cast=bool)
    CAP_DECO = config("CAP_DECO", default="🌚")
    C_LINK = config("C_LINK", default="@AnimeZenith_ongoing")
    CMD_SUFFIX = config("CMD_SUFFIX", default=str())
    DATABASE_URL = config("DATABASE_URL", default='mongodb+srv://sbzxbdbnd:CDHOr0X4p29CffcW@cluster0.iux92sb.mongodb.net/?retryWrites=true&w=majority')
    DBNAME = config("DBNAME", default="personaluse")
    DEV = config("DEV", default="6748415360,1130243906").split(",")
    DEV = [int(dev) for dev in DEV]
    DL_STUFF = config("DL_STUFF", default=None)
    DUMP_CHANNEL = config("DUMP_CHANNEL", default=-1002108819224, cast=int)
    DUMP_LEECH = config("DUMP_LEECH", default=True, cast=bool)
    DYNO = config("DYNO", default=None)
    ENCODER = config("ENCODER", default=None)
    EXT_CAP = config("EXTENDED_CAPTIONS", default=True, cast=bool)
    WORKERS = config("WORKERS", default=2, cast=int)
    FBANNER = config("FBANNER", default=True, cast=bool)
    FCHANNEL = config("FCHANNEL", default=-1002108819224, cast=int)
    FCHANNEL_STAT = config("FCHANNEL_STAT", default=2, cast=int)
    FCODEC = config("FCODEC", default=None)
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i """{}""" -metadata:s:v:0 title="[Anime zenith] : (This Episode)" -metadata:s:a:0 title="[Telegram: @AnimeZenith_ongoing]" -metadata:s:a:1 title="[Telegram: @AnimeZenith_ongoing]" -map 0:v? -map 0:a? -map 0:s? -map 0:t? -metadata title="Fileinfo | Zenith " -c:v libx264 -pix_fmt yuv420p10le -preset veryfast -s 852x480 -crf 30 -c:a libopus -ac 2 -vbr 2  -ab 32k -c:s copy -movflags +faststart """{}""" -y'
    )
    FL_CAP = config("FILENAME_AS_CAPTION", default=False, cast=bool)
    FS_THRESHOLD = config("FLOOD_SLEEP_THRESHOLD", default=600, cast=int)
    FSTICKER = config("FSTICKER", default=None)
    LOCK_ON_STARTUP = config("LOCK_ON_STARTUP", default=False, cast=bool)
    LOG_CHANNEL = config("LOG_CHANNEL", default=-1002108819224, cast=int)
    LOGS_IN_CHANNEL = config("LOGS_IN_CHANNEL", default=True, cast=bool)
    MI_CAP = config("MI_IN_CAPTION", default=True, cast=bool)
    MUX_ARGS = config("MUX_ARGS", default=None)
    NO_BANNER = config("NO_BANNER", default=False, cast=bool)
    NO_TEMP_PM = config("NO_TEMP_PM", default=False, cast=bool)
    OVR = config("OVR", default=None)
    OWNER = config("OWNER", default="6748415360")
    PAUSE_ON_DL_INFO = config("PODI", default=True, cast=bool)
    QBIT_PORT = config("QBIT_PORT", default=8090, cast=int)
    QBIT_TIMEOUT = config("QBIT_TIMEOUT", default=20, cast=int)
    RSS_CHAT = config("RSS_CHAT", default=6748415360, cast=int)
    RSS_DELAY = config("RSS_DELAY", default=60, cast=int)
    RSS_DIRECT = config("RSS_DIRECT", default=True, cast=bool)
    RELEASER = config("RELEASER", default="A-M|ANi-MiNE")
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    TELEGRAPH_AUTHOR = config("TELEGRAPH_AUTHOR", default=None)
    TEMP_USER = config("TEMP_USERS", default=str())
    TG_DL_CLIENT = config("TG_DL_CLIENT", default="pyrogram")
    TG_UL_CLIENT = config("TG_UL_CLIENT", default="pyrogram")
    THUMB = config("THUMBNAIL", default="https://telegra.ph/file/1c2a8f45940e4cb43dbeb.jpg")
except Exception:
    print("Environment vars Missing; or")
    print("something went wrong")
    print(traceback.format_exc())
    exit()
