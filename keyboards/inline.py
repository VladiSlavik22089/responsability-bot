from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
start_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text="Помощь",callback_data="help")],
        [InlineKeyboardButton(text="Меню",callback_data="menu")],
    ]
)

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Список задач", callback_data="menu_call_data_output")],
        [InlineKeyboardButton(text="Добавление задачи",callback_data="menu_call_input")],
        [InlineKeyboardButton(text="Удаление задачи",callback_data="menu_call_delete")],
        [InlineKeyboardButton(text="Id задачи",callback_data="menu_call_id's")]
    ]
)