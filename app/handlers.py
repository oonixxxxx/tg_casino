from turtle import dot
from aiogram import F, Router, types

from aiogram.filters import CommandStart
from aiogram.types import Message

from oth.buttons import Buttons
from oth.text import menu_text

router = Router()

class Functionss:
    def get_combo_text(dice_value: int, self):
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

@router.message_handler(commands=['dice'])
async def roll_dice(message: types.Message):
    data = await message.send_dice(message.chat.id, emoji='🎲')
    await message.send_message(message.chat.id, f'значение кубика {data.dice.value}')

@router.message_handler(commands=['dart'])
async def roll_dice(message: types.Message):
    data = await message.send_dice(message.chat.id, emoji='🎯')
    await message.send_message(message.chat.id, f'значение дартс {data.dice.value}')

@router.message_handler(commands=['bask'])
async def roll_dice(message: types.Message):
    data = await message.send_dice(message.chat.id, emoji='🏀')
    await message.send_message(message.chat.id, f'значение баскет {data.dice.value}')

@router.message_handler(commands=['foot'])
async def roll_dice(message: types.Message):
    data = await message.send_dice(message.chat.id, emoji='⚽')
    await message.send_message(message.chat.id, f'значение футбол {data.dice.value}')

@router.message_handler(commands=['bowl'])
async def roll_dice(message: types.Message):
    data = await message.send_dice(message.chat.id, emoji='🎳')
    await message.send_message(message.chat.id, f'значение боулинг {data.dice.value}')

@router.message_handler(commands=['slot'])
async def roll_dice(message: types.Message):
    data = await message.send_dice(message.chat.id, emoji='🎰')
    await message.send_message(message.chat.id, f'значение слоты {Functionss.get_combo_text(data.dice.value)}')