from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from dialogs import replicas


def buttons_plan() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=replicas["add_lesson"])
    keyboard.button(text=replicas["del_lesson"])
    keyboard.button(text="Вернуться")
    keyboard.adjust(3)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)