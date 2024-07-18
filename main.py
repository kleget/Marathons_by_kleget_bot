import asyncio
import logging
from db_manage import *

from contextlib import suppress
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.chat_member_status import ChatMemberStatus

TOKEN = "7437203058:AAE59ffYA3miRJstp9OpChadmOnAloUJZ40"

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()
# router.message.filter(F.chat.type != "private")


@dp.message()#F.chat.type == "group")
async def private(message: types.Message):
    # await bot.send_message(chat_id=)
    if '#марафон' in message.text:
        with sq.connect('data_base.db') as con:
            sql = con.cursor()
            sql.execute(f"SELECT user_id FROM users WHERE user_id == {str(message.chat.id)}")
            if sql.fetchone() is None:
                sql.execute(
                    "INSERT INTO users (user_id, marathone, msg_id) VALUES (?, ?, ?)",
                    (message.chat.id, 'YES', message.id))
                await message.reply("<b>Поздравляю, теперь вы участник марафона!</b>")
            else:
                await message.reply("<b>Вы уже участник марафона!</b>")


# I'n not understand, then need function
async def main():
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())