from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class Buttons:
    
    """Buttons for Reply Keyboard"""    
    
    menu_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='bank'), KeyboardButton(text='spin 🎰')],
                                                [KeyboardButton(text='Statistics'), KeyboardButton(text='В меню🧑🏿‍💻🗂')]],
            
            resize_keyboard=True,
            input_field_placeholder='Выберите пунт меню.')
    
    
    info_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='В меню🧑🏿‍💻🗂')]],
                                      
                                      resize_keyboard=True,
                                      input_field_placeholder='Выберите пункт меню.')
    
    
    spin_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='spin🎰 2500'), KeyboardButton(text='spin🎰 5000')], 
                                                [KeyboardButton(text='spin🎰 10000'), KeyboardButton(text='spin🎰 20000')],
                                                [KeyboardButton(text='В меню🧑🏿‍💻🗂')]],
                                      
                                      resize_keyboard=True,
                                      input_field_placeholder='Выберите ставку.')