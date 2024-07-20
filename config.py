import asyncio
import logging

# from token import *
from db_manage import *

from contextlib import suppress
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.chat_member_status import ChatMemberStatus

# TOKEN = os.getenv("7437203058:AAEFjSvdH4aqPhVVo_96I4t70X0cqoUVpSk")
TOKEN = "7437203058:AAEFjSvdH4aqPhVVo_96I4t70X0cqoUVpSk"
ADMIN = 1277447609
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# dp = Dispatcher()
#
# router = Router()
# router.message.filter(F.chat.type != "private")
