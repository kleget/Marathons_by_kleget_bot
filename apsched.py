# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# import asyncio
# import aioschedule
#
# # Замените токеном вашего бота
# bot = Bot(token='YOUR_BOT_TOKEN')
# dp = Dispatcher(bot, storage=MemoryStorage())
#
# # Функция для получения списка пользователей, которые не выбрали ужин (замените на вашу реализацию)
# async def the_users_without_dinner():
#     # TODO: реализовать логику получения пользователей
#     return []
#
# # Меню гарниров (замените на ваше меню)
# menu_garnish = types.ReplyKeyboardMarkup(resize_keyboard=True)
# menu_garnish.add(types.KeyboardButton('Картошка'), types.KeyboardButton('Рис'))
#
# # Функция для отправки сообщения о выборе ужина
# async def choose_your_dinner():
#     for user in set(await the_users_without_dinner()):
#         await bot.send_message(chat_id=user,
#                               text="Хей🖖 не забудь выбрать свой ужин сегодня",
#                               reply_markup=menu_garnish)
#
# # Функция для запуска планировщика
# async def scheduler():
#     aioschedule.every().week.at("17:45").do(choose_your_dinner)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)
#
# # Запуск планировщика при старте бота
# async def on_startup(dp):
#     asyncio.create_task(scheduler())
#
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=on_startup)

from aiogram import Bot


async def send_message_time(bot: Bot):

    await bot.send_message('-1002221559614', f'Это сообщение отправлено через несколько секунд после старта бота')

async def send_message_cron(bot: Bot):

    await bot.send_message('-1002221559614', f'Это сообщение будет отправляться ежедневно в указанное время.')

async def send_message_interval(bot: Bot):

    await bot.send_message('-1002221559614', f'Это сообщение будет отправляться с интервалом в 1 минуту')

