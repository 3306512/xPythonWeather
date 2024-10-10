from os import getenv
from dotenv import load_dotenv
import asyncio
from utils.basic_utils import validate
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class BotStates(StatesGroup):
    whether_input = State()


load_dotenv()
TOKEN = getenv('TOKEN')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer('Hi! You can now send your temperature')
    await state.set_state(BotStates.whether_input)


@dp.message(BotStates.whether_input)
async def i_and_a(message: Message, state: FSMContext):
    if validate(message.text):
        if int(message.text) < 0 or int(message.text) == 0:
            await message.answer('A cold, isn’t it?')
        elif 0 < int(message.text) < 10:
            await message.answer('Cool. ')
        else:
            await message.answer('Nice weather we’re having.')
    else:
        await message.answer('incorrect or false number')


async def main() -> None:
    """
        Главная функция, вызывается в точке входа
    :return: None
    """
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('starting bot')
    asyncio.run(main())
