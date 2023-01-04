import pathlib
import os
import logging
from logging.config import dictConfig
from dotenv import load_dotenv
import discord

# GUILDS_ID = discord.Object(id=int(os.getenv("GUILD_IDS")))
GUILDS_ID = 454726525464477699
load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"
COGS_DIR = BASE_DIR / "cogs"


LOGGING_CONFIG = {
    "version": 0.1,
    "disabled_existing_loggers": False,
    "formatters":   {
        "verbose":  {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard":  {
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers": {
        "console": {
            'level': "DEBUG",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "console2": {
            'level': "WARNING",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "file": {
            'level': "INFO",
            'class': "logging.FileHandler",
            'filename': "logs/infos.log",
            'mode': "w",
            'formatter': "verbose"
        },
        "loggers": {
            "kirakota": {
                'handlers': ['console'],
                'level': "INFO",
                'propagate': False,
            },
            "discord": {
                'handlers': ['console2', "file"],
                'level': "INFO",
                'propagate': False,
            }
        }
    }
}
dictConfig(LOGGING_CONFIG)
