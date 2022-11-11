# Изучение библиотеки aiogram
# Писарев Николай Владимирович
# 09.11.2022
import logging

from aiogram import Dispatcher, Bot, types, executor
from aiogram.dispatcher.filters import Text

from bas import *

#Константы и экземпляры основных классов.
API_TOKEN = 'ToKeN'
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

"""
 настройка logging. Записывать в файл  log.txt
 Понижение уровня записи до info событий.
"""
logging.basicConfig(
    filename = "log.txt",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

"""
 Слушатель `/start` или `/help` команд
"""
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    kb = [
            [
            types.KeyboardButton(text="dice"),
            types.KeyboardButton(text="цитата bashorg.org")
            ]
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=keyboard)

@dp.message_handler(Text(equals="dice"))
@dp.message_handler(commands=['dice'])
async def cmd_dice(message: types.Message):
    """
     Просто прикольная эмодзи. При клике по emoji можно посмотреть другие варианты
    """
    msg1 = await message.answer_dice(emoji="🎲")
    logger.info(f"{message.from_user.first_name}, выкинул на кубике {msg1.dice.value}")
    """
     Для получения значения кости выполнить код: msg1.dice.value
    """


@dp.message_handler(Text(equals="цитата bashorg.org"))
async def echo(message: types.Message):
    await message.answer(random_quote())
    logger.info(f"{message.from_user.first_name}, Прочитал цитату в баше.")

@dp.message_handler()
async def echo(message: types.Message):
    """
     возвращаем в телеграмм полученный текст.
    """
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


#===========================================


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


