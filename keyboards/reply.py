from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="one")],
        [KeyboardButton(text="two")]
    ], resize_keyboard=True
)