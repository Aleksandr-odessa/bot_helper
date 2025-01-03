from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from dialogs import replicas
from keyboards.kbd_main import buttons_main

router_start = Router()


@router_start.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(replicas["select_action"], reply_markup=buttons_main())
