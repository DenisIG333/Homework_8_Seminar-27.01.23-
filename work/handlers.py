#import main
import time
from create import dp
from aiogram import Bot, Dispatcher, executor, types
import random

total = 150
number = 0
isBot = False
isGamer = False
scoreGamer = 0
scoreBot = 0
# HELP_COMMAND = """
# /help - список команд
# /start - начать работу с ботом
# """


@dp.message_handler(commands=['start', "старт"])
async def mes_hi(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name} мы будем играть в конфетки, для начала игры напиши "ок"')


@dp.message_handler(text=["Оk", "ok", "Ок", "ок"])
async def mes_start(message: types.Message):
    global number
    global total
    global isGamer
    global isBot
    await message.answer(f'Погнали играть!')
    time.sleep(1)
    rnd = random.randint(1, 2)
    if rnd == 1:
        await message.answer(f'По результатам жеребьевки первый ход делаешь ты, введи число от 1 до 28')
        isGamer = True
    if rnd == 2:
        await message.answer(f'По результатам жеребьевки первый ход делаю я. Введи бот')
        isBot = True


@dp.message_handler(text=["Bot", "bot", "бот", "Бот", ",jn", "ище"])
async def mes_all(message: types.Message):
    global total
    global isGamer
    global isBot
    global scoreBot
    global scoreGamer
    if isBot == True:
        if total > 0:
            await message.answer(f' На столе осталось {total} конфет')
            print(message)
            time.sleep(1)

            await message.answer(f' Следующий ход мой')
            time.sleep(1)
            await message.answer(f' Думаю......')
            time.sleep(2)
            casting_lots = random.randint(1, 28)
            if total > 28:
                total -= casting_lots
                await message.answer(f'возьму {casting_lots} конфет')
                time.sleep(0.5)
                await message.answer(f'На столе осталось {total} конфет')
                time.sleep(0.5)
                await message.answer(f'{message.from_user.first_name}, следующий ход твой, введи число от 1 до 28')
                isGamer = True
                isBot = False
            else:
                await message.answer(f' А нечего думать :-) забираю всё :-)')
                total -= total
                scoreBot += 1
                await message.answer(f'я победил!')
                await message.answer(f'счет побед: бот - {scoreBot}: ты - {scoreGamer}')
                await message.answer(f'Если хочешь начать игру заново, введи количество конфет')
                total = 150

                isGamer = True

        else:
            total = 150
            scoreGamer += 1
            await message.answer(f'ты победил!')
            await message.answer(f'счет побед: бот - {scoreBot}: ты - {scoreGamer}')
            await message.answer(f'Если хочешь начать игру заново, введи количество конфет')
            isGamer = True



# @dp.message_handler(text=["Оk", "ok", "Ок", "ок"])
# async def gamer_turn(message: types.Message):
#     global total
#     global isGamer
#     global isBot
#     if isGamer == True:
#         await message.answer(f'сколько конфет возьмешь?')


@dp.message_handler()
async def gamer_digit(message: types.Message):
    global total
    global isGamer
    global isBot
    global scoreBot
    global scoreGamer
    if isGamer == True:
        if message.text.isdigit():
            while True:
                if int(message.text) >0 and int(message.text) <= 28:
                        total -= int(message.text)
                        if total > 0:
                            await message.answer(f'следующий ход бота, для продолжения напиши бот')
                            isBot = True
                            isGamer = False
                            break
                        else:
                            scoreGamer += 1
                            await message.answer(f'ты победил!')
                            await message.answer(f'счет побед: бот - {scoreBot} : ты - {scoreGamer}')
                            await message.answer(f'Если хочешь начать игру заново, введи количество конфет')
                            isGamer = True
                            total = 150
                            break

                else:
                    return await message.answer(f'введи количество конфет (не более 28)')
