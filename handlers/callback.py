import asyncio

from aiogram import Router,F
from aiogram.types import CallbackQuery
from handlers.commands import help,menu
callbacks_router = Router()

@callbacks_router.callback_query(F.data == "menu")
async def get_query(callback:CallbackQuery):
    await callback.message.edit_caption(
       caption = "<b>Здравствуй!</b> Я — ответственный за твои задачи бот. Рад видеть, что вы будете пользоваться моим функционалом. Удачного пользования!")
    await menu(callback.message)
    await callback.answer("Обрабатывается, подождите!")


@callbacks_router.callback_query(F.data == "help")
async def get_queryl(callback:CallbackQuery):
    await help(callback.message)
    await callback.answer("Обрабатывается, подождите!")




