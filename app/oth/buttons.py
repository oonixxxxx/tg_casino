from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class Buttons: 
    menu_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='bank'), KeyboardButton(text='spin 🎰')]],
            resize_keyboard=True,
            input_field_placeholder='Выберите пунт меню.')
    
    info_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Menu')]],
                                      resize_keyboard=True,
                                      input_field_placeholder='Выберите пункт меню.')