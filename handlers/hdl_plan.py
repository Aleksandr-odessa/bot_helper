import requests
from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from dialogs import replicas
from keyboards.kb_plan import buttons_plan
from keyboards.kbd_main import buttons_main

router_plan = Router()

# Check schedulle
@router_plan.message(F.text == replicas["plan"])
async def show_schedule(message: Message, state: FSMContext):
    request = requests.get("https://schedules.alwaysdata.net/schedule/show")
    schedule:dict= request.json()
    lessons: str = ''
    for day, lessson in schedule.items():
        lessons_for_day: str = "<b>" + day + "</b>" + "\n"
        for les in lessson:
            time_and_lesson = f'{les[0]} - {les[1]}:     <b><i>{les[2]}</i></b>'
            lessons_for_day: str = lessons_for_day + time_and_lesson + "\n"
        lessons: str = lessons + lessons_for_day + "\n"
    await message.answer(lessons, parse_mode = ParseMode.HTML, reply_markup=buttons_plan())

@router_plan.message(F.text == replicas["add_lesson"])
async def add_schedule(message: Message, state: FSMContext):
    await message.answer(replicas["empty"], reply_markup=buttons_main())

@router_plan.message(F.text == replicas["del_lesson"])
async def del_schedule(message: Message, state: FSMContext):
    await message.answer(replicas["empty"], reply_markup=buttons_main())