import time
import asyncio
from aiogram.fsm.state import State,StatesGroup
from aiogram import Router
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline import menu_kb
from database import add_deal, show_deals, conn,show_db,deletings_func,show_deals_del
from datetime import datetime
import datetime as dt
#creating router and class for fsm_classes
fsm_router = Router()
class Deal(StatesGroup):
    deal = State()
    date = State()
    time = State()
    sleep = State()
    delete = State()
    reminder = State()

#fsm_router for adding new states
@fsm_router.callback_query(F.data == "menu_call_input")
async def menu_to_name_fsm(callback:CallbackQuery, state: FSMContext):
    await callback.answer("Сообщение обрабатывается!")
    await callback.message.answer("Чем займемся?")
    await state.set_state(Deal.deal)


@fsm_router.message(Deal.deal)
async def name_to_data_fsm(message:Message,state: FSMContext):
    await message.answer("Отлично, введите дату напоминания в формате число, месяц, год (например, 01.01.2025)")
    await state.update_data(deal=message.text)
    await state.set_state(Deal.date)


@fsm_router.message(Deal.date)
async def data_to_timer_fsm(message:Message,state:FSMContext):
    try:
        a = datetime.strptime(message.text.strip(), "%d.%m.%Y")
        print(type(a))
        b = datetime.today()
        print(type(b))
        if a.date() < b.date():
            await message.answer("Эта дата уже прошла, операция прервана, будь внимательнее!",reply_markup = menu_kb)
            await state.clear()
        elif a.date() >= b.date():
            await state.update_data(date=str(a)[:10])
            await message.answer("Почти готово, введите время напоминания")
            await state.set_state(Deal.time)
    except TypeError and ValueError:
        await message.answer("Вы ошиблись, операция прервана, будь внимательнее!",reply_markup = menu_kb)
        await state.clear()


@fsm_router.message(Deal.time)
async def timer_to_ans_fsm(message:Message,state: FSMContext):
    try:
        await message.answer("Подтвердите операцию, набрав Готово")
        a = ""
        a = datetime.strptime(message.text,"%H:%M")
        await state.update_data(time=str(a)[11:16])

        await state.set_state(Deal.sleep)
    except TypeError and ValueError:
        await message.answer("Вы ошиблись, операция прервана, будь внимательнее!",reply_markup = menu_kb)
        await state.clear()

@fsm_router.message(Deal.sleep)
async def ans_to_reminder_fsm(message:Message, state:FSMContext):
    id_user = message.from_user.id
    data = await state.get_data()
    task_id = add_deal(id_user, data['deal'], str(data['date']), str(data['time']))
    await message.reply(f"Готово!\n Я напомню вам про задачу: {data['deal']} {str(data['date'])} в {str(data['time'])}")
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%d.%m.%Y")
    data = await state.get_data()
    print(current_time, current_date)

    # current datetime
    dt_now = now

    # parse target datetime safely
    dt_target = datetime.strptime(f"{data['date']} {data['time']}", "%Y-%m-%d %H:%M")

    # calculate time difference
    difference = (dt_target - dt_now).total_seconds()

    if difference > 0:
        await asyncio.sleep(difference)

        await message.answer(f"Напоминанию, вы хотели сделать {data['deal']} в это время")
        deletings_func(task_id)
    await state.clear()

#func for pushing user's list of deals

@fsm_router.callback_query(F.data == "menu_call_data_output")
async def get_note_list(callback:CallbackQuery, state: FSMContext):
    await callback.answer("Сообщение обрабатывается!")
    id_user = callback.from_user.id
    b = show_deals(id_user)
    if len(b) == 0:
        await callback.message.answer("Пока что здесь ничего нет! Добавь свою первую задачу, чтобы начать!")
    else:
        await callback.message.answer("Вот список ваших активных дел:")
        d = ""
        f = 1
        for i in range(len(b)):
            d += f"{f}) Я напомню Вам про: {b[i][0]} {str(b[i][1])[:10]} числа ровно в {str(b[i][2])}\n"
            f += 1
        await callback.message.reply(d)
    await state.clear()


#func for deleting user's deals
@fsm_router.callback_query(F.data == "menu_call_delete")
async def get_deleting_id(callback:CallbackQuery, state: FSMContext):
    id_user = callback.from_user.id
    b = show_deals_del(id_user)
    await callback.answer("Сообщение обрабатывается!")
    if len(b) == 0:
        await callback.message.answer("Пока что здесь ничего нет! Добавь свою первую задачу, чтобы начать!",reply_markup = menu_kb)
    else:
        await callback.message.answer("Вот ваш список задач. Чтобы удалить задачу, введите ее порядковый номер (например, 1, 2, 3)")
        d = ""
        f = 1
        for i in range(len(b)):
            d += f"{f}) {b[i][0]}\n"
            f += 1
        await callback.message.answer(d)
        await state.set_state(Deal.delete)

@fsm_router.message(Deal.delete)
async def deleting_func(message:Message, state:FSMContext):
    id_user = message.from_user.id
    b = show_deals_del(id_user)
    idm = ""
    f = 1
    for i in range(len(b)):
        idm += str(f)
        f += 1
    if message.text in idm:
        name = b[int(message.text) - 1][1]
        deletings_func(name)
    else:
        await message.reply("Цифра не верна, операция прервана",reply_markup = menu_kb)
        await state.clear()
