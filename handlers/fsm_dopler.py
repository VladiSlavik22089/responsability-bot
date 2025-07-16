
from aiogram.fsm.state import State,StatesGroup
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from database import add_deal,show_db,show_deals,show_date,show_time
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
    await message.answer("Отлично, введите дату напоминания в формате число, месяц, год")
    await state.update_data(deal=message.text)
    await state.set_state(Deal.date)


@fsm_router.message(Deal.date)
async def data_to_timer_fsm(message:Message,state:FSMContext):
    try:
        a = datetime.strptime(message.text.strip(), "%d.%m.%Y")
        if a < datetime.now():
            await message.answer("Эта дата уже прошла, операция прервана, будьте внимательнее!")
            await state.clear()
        else:
            await state.update_data(date=a)
            await message.answer("Почти готово, введите время напоминания")
            await state.set_state(Deal.time)
    except ValueError:
        await message.answer("Вы ошиблись, операция прервана, будьте внимательнее!")
        await state.clear()


@fsm_router.message(Deal.time)
async def timer_to_ans_fsm(message:Message,state: FSMContext):
    try:
        await message.answer("Подтвердите операцию, набрав Готово")
        a = ""
        a = datetime.strptime(message.text,"%H:%M")
        await state.update_data(time=a)
        id_user = message.from_user.id
        data = await state.get_data()
        print(data)
        add_deal(id_user, data["deal"], str(data["date"])[:10], str(data["time"])[11:])
        await state.set_state(Deal.sleep)
    except TypeError and ValueError:
        await message.answer("Вы ошиблись, операция прервана, будьте внимательнее!")
        await state.clear()

@fsm_router.message(Deal.sleep)
async def ans_to_sleep_fsm(message:Message, state:FSMContext):
    data = await state.get_data()
    await message.reply(f"Готово! Я напомню вам про задачу: {data["deal"]} {str(data["date"])[:10]} в {str(data["time"])[10:]}")
    print(show_db())
    await state.clear()

#func for pushing user's list of deals

@fsm_router.callback_query(F.data == "menu_call_data_output")
async def get_note_list(callback:CallbackQuery, state: FSMContext):
    await callback.answer("Сообщение обрабатывается!")
    await callback.message.answer("Ваши дела:")
    id_user = callback.from_user.id
    a = show_date(id_user)
    b = show_deals(id_user)
    c = show_time(id_user)
    f = 1
    for i in b:
        k = 1
        for j in a:
            for m in c:
                k += 1
                if k <= 2:
                    await callback.message.answer(text=f"{f}) Я напомню Вам про: {i[0]} {str(j[0])[:10]} числа ровно в{str(m[0])[10:]}")
                    f += 1
                else:
                    break
    await state.clear()

#func for deleting user's deals
