from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from keyboards.inline import start_kb,menu_kb
command_router = Router()


@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    start_message = "<b>Привет!</b> 👋 Я бот-помощник, и моя главная задача - напоминать тебе о важных делах. Готов помочь тебе организовать день и ничего не забыть! Просто добавь задачу, и я позабочусь о том, чтобы ты получил напоминание в нужное время ✨"
    await message.answer_photo(
        photo='https://i.pinimg.com/1200x/de/f5/e8/def5e8990fef1c82c44a2500bf52235a.jpg',caption = start_message, reply_markup= start_kb,parse_mode="HTML")



@command_router.message(Command("about"))
async def about(message:Message) -> None:
    b = """Вот что я могу рассказать о себе:

Я бот-напоминалка, созданный, чтобы помочь тебе оставаться в курсе своих задач и дедлайнов. Я умею:

•  Добавлять задачи: Просто опиши задачу и укажи время напоминания 
•  Напоминать о задачах: Я отправлю тебе уведомление в указанное время, чтобы ты ничего не пропустил
•  Список задач: Показать список запланированных задач
•  Удаление задач: Удалить ненужные задачи

Я все еще в разработке, но стараюсь быть максимально полезным. Если у тебя есть предложения или вопросы, обращайся!"""
    await message.answer(text=b)

@command_router.message(Command("help"))
async def help(message:Message) -> None:
    await message.answer("""
Вот что я умею:

•  /start - Начать работу
•  /about - Узнать обо мне больше
•  /help - Список команд
•  /menu - Управление задачами

Готов помочь тебе организовать свой день! Стоит лишь обратиться! ✨
""")

@command_router.message(F.text.lower() == "привет")
async def hi(message:Message) -> None:
    await message.answer("Здравстуйте! Как Вы?")

@command_router.message(F.text.lower() =="пока")
async def bye(message:Message) -> None:
    await message.answer("Приятного дня!")

@command_router.message(Command("menu"))
async def menu(message:Message) -> None:
    text = "Здесь ты можешь управлять своими задачами: добавлять новые, просматривать существующие и удалять выполненные. Выбери нужную команду и начнем работу!"
    await message.answer(text=text,reply_markup=menu_kb)


