
from aiogram.fsm.state import State,StatesGroup
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from database import add_deal,show_db,show_deals
from datetime import datetime


fsm_router = Router()


class Deal(StatesGroup):
    deal = State()
    date = State()
    time = State()
    sleep = State()

#fsm_router for adding new states
@fsm_router.callback_query(F.data == "menu_call_input")
async def menu_to_name_fsm(callback:CallbackQuery, state: FSMContext):
    await callback.answer("Сообщение обрабатывается!")
    await callback.message.answer("Введите название занятия для напоминания")
    await state.set_state(Deal.deal)


@fsm_router.message(Deal.deal)
async def name_to_data_fsm(message:Message,state: FSMContext):
    await message.answer("Почти готово, введите год.месяц.дату напоминания")
    await state.update_data(deal=message.text)
    await state.set_state(Deal.date)


@fsm_router.message(Deal.date)
async def data_to_timer_fsm(message:Message,state:FSMContext):
    try:
        await message.answer("Почти готово, введите время напоминания Ч:М")
        a = datetime.strptime(message.text, "%d.%m.%Y")
        await state.update_data(date=a)
        await state.set_state(Deal.time)
    except Exception:
        await message.answer("Вы ошиблись, операция прервана")
        await state.clear()


@fsm_router.message(Deal.time)
async def timer_to_ans_fsm(message:Message,state: FSMContext):
    try:
        a = ""
        a = datetime.strptime(message.text,"%H:%M")
        await state.update_data(time=a)
        id_user = message.from_user.id
        data = await state.get_data()
        add_deal(id_user, data["deal"], data["date"], data["time"])
        await state.set_state(Deal.sleep)
    except Exception(BaseException):
        await message.answer("Вы ошиблись, операция прервана")
        await state.clear()

@fsm_router.message(Deal.sleep)
async def ans_to_sleep_fsm(message:Message, state:FSMContext):
    data = await state.get_data()
    await message.answer(f"Готово! Я напомню вас про задачу : ({data["deal"]}) {data["date"]} в {data["time"]}")
    await state.clear()