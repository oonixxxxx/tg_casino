# imports
from aiogram import F, Router, types, Bot

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode

from oth.buttons import Buttons
from oth.text import menu_text
from oth.functions import get_combo_text, check_combo
from config import TG_BOT_TOKEN


router = Router()
bot = Bot(TG_BOT_TOKEN, parse_mode=ParseMode.HTML)

class Constanse:
    bank = 1_000_000

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello! welcome to казик", 
                         reply_markup=Buttons.menu_button)


@router.message(F.text == 'В меню🧑🏿‍💻🗂')
async def get_menu(message: Message):
    await message.answer(str(menu_text), reply_markup=Buttons.menu_button)


@router.message(F.text == 'spin 🎰')
async def roll_dice(message: types.Message):
    
    data = await bot.send_dice(message.chat.id, emoji='🎰')
    result = get_combo_text(data.dice.value)
    Constanse.bank -= 2500
    cost = check_combo(result, 2500)
    Constanse.bank += cost
            
    await bot.send_message(message.chat.id, f'Ставка: {2500},\nВыйгрыш: {cost},\nВаш текущий баланс: {Constanse.bank}$')


# functions with bank
@router.message(F.text == 'bank')
async def get_my_bank(message: types.Message):
    await bot.send_message(message.chat.id, f'Ваш баланс: {Constanse.bank}$')


@router.message(F.text == 'add million')
async def add_million(message: types.Message):
    await bot.send_message(message.chat.id, f'Ваш баланс: {Constanse.bank + 1_000_000}$')
    Constanse.bank += 1_000_000


@router.message(F.text == 'test spin')
async def test_spin(message: types.Message):
    await bot.send_message(message.chat.id, f'Тестовый прокрут совершен. Ваш баланс {Constanse.bank - 1000}$')
    Constanse.bank -= 2500
    
    
@router.message(F.text == 'reset bank')
async def reset_bank(message: types.Message):
    Constanse.bank = 0
    await bot.send_message(message.chat.id, f'Ваш баланс: {Constanse.bank}$')