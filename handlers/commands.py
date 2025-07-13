import asyncio

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from keyboards.inline import start_kb,menu_kb
from keyboards.reply import keyboard
command_router = Router()


@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    start_message = "<b>Здравствуй!</b> Я — ответственный за твои задачи бот. Рад видеть, что вы будете пользоваться моим функционалом. Удачного пользования!"
    await message.answer_photo(
        photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5bMKagpOOdp9v7P3nl0PFpN7LSPTjGo6anA&s',caption = start_message, reply_markup= start_kb,parse_mode="HTML")


@command_router.message(Command("about"))
async def about(message:Message) -> None:
    b = "Я - бот, который может помочь вам сделать все, что вы захотите в будущем всего с помощью нескольких напоминаний"
    await message.answer(text=b)

@command_router.message(Command("help"))
async def help(message:Message) -> None:
    await message.answer("""
/start - перезапустит мою работу
/about - поможет узнать меня ближе
/help - тут находятся мои основные команды 
/menu - здесь ты сможешь узнать все функции работы с твоими задачами
""")

@command_router.message(F.text.lower() == "привет")
async def hi(message:Message) -> None:
    await message.answer("Здравстуйте! Как Вы?")

@command_router.message(F.text.lower() =="пока")
async def bye(message:Message) -> None:
    await message.answer("Приятного дня!")

@command_router.message(Command("menu"))
async def menu(message:Message) -> None:
    text = "Меню доступа к командам"
    await message.answer(text=text,reply_markup=menu_kb)


