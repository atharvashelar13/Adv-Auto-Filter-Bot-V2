#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID", '25858155'))

API_HASH = os.environ.get("API_HASH", 'f9519e4543cbfd48c0e52dc9ba64a4a6')

BOT_TOKEN = os.environ.get("BOT_TOKEN", '8231240200:AAHL7dtSce2_lak2d6Mfxi4RaIJUzt6VukE')

DB_URI = os.environ.get("DB_URI", 'guessyourage_bot')

USER_SESSION = os.environ.get("USER_SESSION")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

