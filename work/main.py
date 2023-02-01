from aiogram import Bot, Dispatcher, executor, types
from handlers import dp
# bot = Bot("5986460561:AAGPxdr55UOIUPp1RMc_jVlfGfefHwY64Ks")
# dp = Dispatcher(bot)



async def on_start(_):
    print("Бот запущен")



# @dp.message_handler(commands=['start'])
# async def mes_start(message: types.Message):
#     await message.answer(f'Привет, {message.from_user.first_name} мы будем играть в конфетки')
#
#
# @dp.message_handler(commands=['help'])
# async def mes_help(message: types.Message):
#     await message.answer('Помощь тебе')
#
#
# @dp.message_handler(commands=['set'])
# async def mes_settings(message: types.Message):
#     global total
#     count = int(message.text.split()[1])
#     total = count
#     await message.answer(f'Максимальное количество конфет установлено {total}')
#
#
# # @dp.message_handler()
# # async def mes_all(message: types.Message):
# #     await message.answer(f'{message.from_user.full_name}, смотри что я поймал - {message.text}')
# #     print(message)
#
#
# @dp.message_handler()
# async def mes_all(message: types.Message):
#     global total
#     if message.text.isdigit():
#         total -= int(message.text)
#     await message.answer(f' На столе осталось {total} конфет')
#     print(message)

executor.start_polling(dp, skip_updates=True, on_startup=on_start)