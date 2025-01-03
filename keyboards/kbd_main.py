from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from dialogs import replicas


def buttons_main() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=replicas["plan"])
    keyboard.button(text=replicas["translate"])
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)