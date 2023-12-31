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
            self.ALWAYS_DEPLOY_LATEST = config("ALWAYS_DEPLOY_LATEST", default=False, cast=bool)
            self.ALLOW_ACTION = config("ALLOW_ACTION", default=True, cast=bool)
            self.APP_ID = config("APP_ID", default=3847632, cast=int)
            self.API_HASH = config("API_HASH", default="1a9708f807ddd06b10337f2091c67657")
            self.ARIA2_PORT = config("ARIA2_PORT", default=6800, cast=int)
            self.BOT_TOKEN = config("BOT_TOKEN", default="6312969509:AAE4CYabaJQceMV1fB3fRFRnbDRljk_je_c")
            self.CACHE_DL = config("CACHE_DL", default=False, cast=bool)
            self.CAP_DECO = config("CAP_DECO", default="⚡️")
            self.C_LINK = config("C_LINK", default="@AnimeZenith_ongoing")
            self.CMD_SUFFIX = config("CMD_SUFFIX", default=str())
            self.DATABASE_URL = config("DATABASE_URL", default='mongodb+srv://sbzxbdbnd:CDHOr0X4p29CffcW@cluster0.iux92sb.mongodb.net/?retryWrites=true&w=majority')
            self.DBNAME = config("DBNAME", default="personaluse")
            self.DEV = config("DEV", default="6748415360,1130243906").split(",")
            self.DEV = [int(dev) for dev in self.DEV]
            self.DL_STUFF = config("DL_STUFF", default=None)
            self.DUMP_CHANNEL = config("DUMP_CHANNEL", default=-1002108819224, cast=int)
            self.DUMP_LEECH = config("DUMP_LEECH", default=True, cast=bool)
            self.DYNO = config("DYNO", default=None)
            self.ENCODER = config("ENCODER", default=None)
            self.EXT_CAP = config("EXTENDED_CAPTIONS", default=True, cast=bool)
            self.WORKERS = config("WORKERS", default=2, cast=int)
            self.FBANNER = config("FBANNER", default=True, cast=bool)
            self.FCHANNEL = config("FCHANNEL", default=-1002108819224, cast=int)
            self.FCHANNEL_STAT = config("FCHANNEL_STAT", default=2, cast=int)
            self.FCODEC = config("FCODEC", default=None)
            self.FFMPEG = config(
                "FFMPEG",
                default='ffmpeg -i """{}""" -metadata:s:v:0 title="[Anime zenith] : (This Episode)" -metadata:s:a:0 title="[Telegram: @AnimeZenith_ongoing]" -metadata:s:a:1 title="[Telegram: @AnimeZenith_ongoing]" -map 0:v? -map 0:a? -map 0:s? -map 0:t? -metadata title="Fileinfo | Zenith " -c:v libx264 -pix_fmt yuv420p10le -preset veryfast -s 852x480 -crf 30 -c:a libopus -ac 2 -vbr 2  -ab 32k -c:s copy -movflags +faststart """{}""" -y'
            )
            self.FL_CAP = config("FILENAME_AS_CAPTION", default=False, cast=bool)
            self.FS_THRESHOLD = config("FLOOD_SLEEP_THRESHOLD", default=600, cast=int)
            self.FSTICKER = config("FSTICKER", default=None)
            self.LOCK_ON_STARTUP = config("LOCK_ON_STARTUP", default=False, cast=bool)
            self.LOG_CHANNEL = config("LOG_CHANNEL", default=-1002108819224, cast=int)
            self.LOGS_IN_CHANNEL = config("LOGS_IN_CHANNEL", default=True, cast=bool)
            self.MI_CAP = config("MI_IN_CAPTION", default=True, cast=bool)
            self.MUX_ARGS = config("MUX_ARGS", default=None)
            self.NO_BANNER = config("NO_BANNER", default=False, cast=bool)
            self.NO_TEMP_PM = config("NO_TEMP_PM", default=False, cast=bool)
            self.OVR = config("OVR", default=None)
            self.OWNER = config("OWNER", default="6748415360")
            self.PAUSE_ON_DL_INFO = config("PODI", default=True, cast=bool)
            self.QBIT_PORT = config("QBIT_PORT", default=8090, cast=int)
            self.QBIT_TIMEOUT = config("QBIT_TIMEOUT", default=20, cast=int)
            self.RSS_CHAT = config("RSS_CHAT", default=6748415360, cast=int)
            self.RSS_DELAY = config("RSS_DELAY", default=60, cast=int)
            self.RSS_DIRECT = config("RSS_DIRECT", default=True, cast=bool)
            self.RELEASER = config("RELEASER", default="A-M|ANi-MiNE")
            self.TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
            self.TELEGRAPH_AUTHOR = config("TELEGRAPH_AUTHOR", default=None)
            self.TEMP_USER = config("TEMP_USERS", default=str())
            self.TG_DL_CLIENT = config("TG_DL_CLIENT", default="pyrogram")
            self.TG_UL_CLIENT = config("TG_UL_CLIENT", default="pyrogram")
            self.THUMB = config("THUMBNAIL", default="https://telegra.ph/file/1c2a8f45940e4cb43dbeb.jpg")
        except Exception:
            print("Environment vars Missing; or")
            print("something went wrong")
            print(traceback.format_exc())
            exit()
