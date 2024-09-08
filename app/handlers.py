from aiogram import F, Router, types, Bot

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode

from oth.buttons import Buttons
from oth.text import menu_text
from config import TG_BOT_TOKEN

router = Router()
bot = Bot(TG_BOT_TOKEN, parse_mode=ParseMode.HTML)

class Constanse:
    bank = 1_000_000


def get_combo_text(dice_value: int):
    """
    Возвращает то, что было на конкретном дайсе-казино
    :param dice_value: значение дайса (число)
    :return: массив строк, содержащий все выпавшие элементы в виде текста
    Альтернативный вариант (ещё раз спасибо t.me/svinerus):
    return [casino[(dice_value - 1) // i % 4]for i in (1, 4, 16)]
    """
    #           0       1         2        3
    values = ["BAR", "виноград", "лимон", "семь"]

    dice_value -= 1
    result = []
        
    for _ in range(3):
        result.append(values[dice_value % 4])
        dice_value //= 4
        
    return result


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello! Я бот длля продажи предметов в локальном магазине \n что бы перейти к выполнению заказа напиши 'Корзина 🛒'", 
                         reply_markup=Buttons.menu_button)


@router.message(F.text == 'В меню🧑🏿‍💻🗂')
async def get_menu(message: Message):
    await message.answer(str(menu_text), reply_markup=Buttons.menu_button)


@router.message(F.text == 'spin')
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎰')
    result = get_combo_text(data.dice.value)
    await bot.send_message(message.chat.id, f'значение слоты {result}')
    
    if result[0] == result[1] == result[2]:
        await bot.send_message('jackpot')


@router.message(F.text == 'bank')
async def get_my_bank(message: types.Message):
    await bot.send_message(message.chat.id, f'Ваш баланс: {Constanse.bank}')


@router.message(F.text == 'add million')
async def add_million(message: types.Message):
    await bot.send_message(message.chat.id, f'Ваш баланс: {Constanse.bank + 1_000_000}')
    Constanse.bank += 1_000_000


@router.message(F.text == 'test spin')
async def test_spin(message: types.Message):
    await bot.send_message(message.chat.id, f'Тестовый прокрут совершен. Ваш баланс {Constanse.bank - 1000}')
    Constanse.bank -= 1000
    
    
@router.message(F.text == 'reset bank')
async def reset_bank(message: types.Message):
    Constanse.bank = 0
    await bot.send_message(message.chat.id, f'Ваш баланс: {Constanse.bank}')