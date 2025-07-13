from aiogram.fsm.state import State,StatesGroup
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery


fsm_router = Router()


class Deal(StatesGroup):
    sleep = State()
    deal = State()
    timer = State()
    del_deal = State()
    deal_id = State()
    user_id = State()

@fsm_router.callback_query(F.data == "menu_call_input")
async def get_query_nput(callback:CallbackQuery, state: FSMContext):
    await callback.answer("Сообщение обрабатывается!")
    await callback.message.answer("Введите название занятия для напоминания")
    await state.set_state(Deal.deal)

@fsm_router.message(Deal.deal)
async def input_deal(message:Message,state: FSMContext):
    await state.update_data(deal=message.text)
    await state.set_state(Deal.timer)
    await message.answer("Почти готово, введите время напоминания!")

@fsm_router.message(Deal.timer)
async def get_query_nput(message:Message, state: FSMContext):
    await state.update_data(timer=message.text)
    await message.answer("Сообщение обрабатывается!")
    data = await state.get_data()
    await message.answer(f"Я напомню вам про задачу - {data["deal"]}, ровно в {data["timer"]}")
    id_user = message.from_user.id


@fsm_router.callback_query(F.data == "menu_call_delete")
async def get_query_nput(callback:CallbackQuery, state: FSMContext):
    await callback.answer("Сообщение обрабатывается!")
    await callback.message.answer("Введите id удаляемого задания")
    await state.set_state(Deal.del_deal)

@fsm_router.message(Deal.del_deal)
async def input_deal(message:Message,state: FSMContext):
    await state.update_data(del_deal=message.text)
    await message.answer("Id записан!")

@fsm_router.callback_query(F.data == "menu_call_id's")
async def get_query_nput(callback:CallbackQuery, state: FSMContext):
    await callback.answer("Сообщение обрабатывается!")
    await callback.message.answer("Введите название Вашего задания для вывода id")
    await state.update_data(id=callback.message.text)

@fsm_router.callback_query(F.data == "menu_call_data_output")
async def get_query_nput(callback:CallbackQuery, state: FSMContext):
    await callback.answer("Сообщение обрабатывается!")
    await callback.message.answer("Ваши дела:")
    await state.clear()