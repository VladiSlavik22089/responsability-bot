from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
start_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text="Меню",callback_data="menu")],
        [InlineKeyboardButton(text="Помощь",callback_data="help")],
    ]
)

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Добавление задачи",callback_data="menu_call_input")],
        [InlineKeyboardButton(text="Удаление задачи",callback_data="menu_call_delete")],
        [InlineKeyboardButton(text="Список задач", callback_data="menu_call_data_output")],
    ]
)