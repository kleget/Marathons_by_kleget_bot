import asyncio
import logging
from db_manage import *
from feature import *
from contextlib import suppress
from datetime import datetime, timedelta
import asyncio
import aioschedule
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.chat_member_status import ChatMemberStatus
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apsched import *
from aiogram.methods.set_message_reaction import SetMessageReaction
TOKEN = "7437203058:AAE59ffYA3miRJstp9OpChadmOnAloUJZ40"
ADMIN = 1277447609
logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()
# router.message.filter(F.chat.type != "private")

@dp.message()#F.chat.type == "group")
async def private(message: types.Message):
    # await bot.send_message(chat_id=)
    if '#марафон' in message.text and message.chat.type != 'private':
        with sq.connect('data_base.db') as con:
            sql = con.cursor()
            sql.execute(f"SELECT user_id FROM users WHERE user_id == {str(message.from_user.id)}")
            if sql.fetchone() is None:
                if message.from_user.username != None:
                    sql.execute(
                        "INSERT INTO users (user_id, link, marathone, msg_id) VALUES (?, ?, ?, ?)",
                        (message.from_user.id, message.from_user.username, 'NO', message.message_id))
                    await message.reply("<b>Поздравляю, теперь вы участник марафона!</b>")
                else:
                    sql.execute(
                        "INSERT INTO users (user_id, link, marathone, msg_id) VALUES (?, ?, ?, ?)",
                        (message.from_user.id, f"{message.from_user.full_name} user_id: {message.from_user.id}", 'NO', message.message_id))
                    await message.reply("<b>Поздравляю, теперь вы участник марафона!</b>")

            else:

                t = await db_select('marathone', 'user_id')
                t = list(t[0])
                # TODO: do no/yes filter
                if t == 'NO':
                    await message.reply("<b>Вы уже участник марафона!</b>")
                if t == 'YES':
                    await message.reply("<b>Вы уже прошли марафон!</b>")
                    # TODO: do set reaction
                # await bot.set_message_reaction(chat_id=message.chat.id, message_id=message.message_id, emoji='🔥', is_big=True, request_timeout=2)
    else:
        if message.chat.id == ADMIN and message.chat.type == 'private':
            if message.text == 'Participant stat with tab':
                a = await work_with_table(await db_select_all(), 'ALL')
                await bot.send_message(chat_id=ADMIN, text=a)
            elif message.text == 'Winner stat with tab':
                a = await work_with_table(await db_select_all(), 'YES')
                await bot.send_message(chat_id=ADMIN, text=a)
            else:
                kb = [
                    [types.KeyboardButton(text="Participant stat with tab")],
                    [types.KeyboardButton(text="Winner stat with tab")]
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,)
                await bot.send_message(chat_id='1277447609', text='К Вашим услоугам, хозяин', reply_markup=keyboard)
# @dp.message()
# async def feature(message: types.Message):
#     await bot.send_message(chat_id=message.chat.id, text='Hi!')

async def main():
    dp.include_router(router)
    # scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    # scheduler.add_job(send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10), kwargs={'bot': bot})

    #This sendion message everyday in 18:24
    # TODO: finish this feature
    # scheduler.add_job(send_message_cron, trigger='cron', hour=18, minute=24, start_date=datetime.now(), kwargs={'bot': bot})

    # scheduler.add_job(send_message_interval, trigger='interval', seconds = 60, kwargs = {'bot': bot})

    # scheduler.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
