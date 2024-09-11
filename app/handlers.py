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
    bank = 1_000_000 #initial balance
    '''jackpots = 0 # number of jackpots for all time
    lose_money = 0 #money lost
    get_money = 0 #money earned
    

def get_statistics(bank, lose_money, win_money, jackpots):
    return 'Balance: {bank}\nMoney spent: {lose_money}\nMoney won: {win_money}\nNumber of jackpots: {jackpots}\n"'.format()'''



@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(str(menu_text), reply_markup=Buttons.menu_button)


@router.message(F.text == 'В меню🧑🏿‍💻🗂')
async def get_menu(message: Message):
    await message.answer(str(menu_text), reply_markup=Buttons.menu_button)


'''@router.message(F.text =='Statistics')
async def get_statistics(message: Message):
    await message.answer(str(get_statistics(Constanse.bank, Constanse.lose_money, Constanse.get_money, Constanse.jackpots)), 
                         reply_markup=Buttons.statistics_button)'''


@router.message(F.text == 'spin 🎰')
async def get_spin_menu(message: types.Message):
    await message.answer('Выберите стоимость ставки', reply_markup=Buttons.spin_button)


@router.message(F.text == 'spin🎰 2500')
async def roll_dice_2500(message: types.Message):
    
    data = await bot.send_dice(message.chat.id, emoji='🎰')
    result = get_combo_text(data.dice.value)
    Constanse.bank -= 2500
    cost = check_combo(result, 2500)
    Constanse.bank += cost
            
    await bot.send_message(message.chat.id, f'Ставка: {2500},\nВыйгрыш: {cost},\nВаш текущий баланс: {Constanse.bank}$')


@router.message(F.text == 'spin🎰 5000')
async def roll_dice_5000(message: types.Message):
    
    data = await bot.send_dice(message.chat.id, emoji='🎰')
    result = get_combo_text(data.dice.value)
    Constanse.bank -= 5000
    cost = check_combo(result, 5000)
    Constanse.bank += cost
            
    await bot.send_message(message.chat.id, f'Ставка: {5000},\nВыйгрыш: {cost},\nВаш текущий баланс: {Constanse.bank}$')


@router.message(F.text == 'spin🎰 10000')
async def roll_dice_10000(message: types.Message):
    
    data = await bot.send_dice(message.chat.id, emoji='🎰')
    result = get_combo_text(data.dice.value)
    Constanse.bank -= 10000
    cost = check_combo(result, 10000)
    Constanse.bank += cost
            
    await bot.send_message(message.chat.id, f'Ставка: {10000},\nВыйгрыш: {cost},\nВаш текущий баланс: {Constanse.bank}$')


@router.message(F.text == 'spin🎰 20000')
async def roll_dice_20000(message: types.Message):
    
    data = await bot.send_dice(message.chat.id, emoji='🎰')
    result = get_combo_text(data.dice.value)
    Constanse.bank -= 20000
    cost = check_combo(result, 20000)
    Constanse.bank += cost
            
    await bot.send_message(message.chat.id, f'Ставка: {20000},\nВыйгрыш: {cost},\nВаш текущий баланс: {Constanse.bank}$')


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