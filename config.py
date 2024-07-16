import random
import sqlite3 as sq
from config import *
import logging
# from data_words import base
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

######## OTHER IMPORTS ########
# import sqlite3 as sq
# import re
# from datetime import datetime


# import datetime as dt

######## CONST ########
TOKEN = '7437203058:AAEFjSvdH4aqPhVVo_96I4t70X0cqoUVpSk'
# YOOTOKEN = "*****************" #test
# YOOTOKEN = "**************" #live
# v = 5.131
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())