import asyncio
import logging.config
import os

from aiogram import Bot, Dispatcher
from logging_config import LOGGING_CONFIG
from dotenv import load_dotenv

# from handlers.hdl_plan import router_plan
from handlers.hdl_start import router_start
from handlers.hnd_translat import router_transl
logging.config.dictConfig(LOGGING_CONFIG)
error_logger = logging.getLogger('log_error')
debug_logger = logging.getLogger('log_debug')
info_logger = logging.getLogger('log_info')

async def main():
    bot = Bot(os.environ['TG_TOKEN'])
    dp = Dispatcher()
    dp.include_routers(router_start)
    # dp.include_routers(router_plan)
    dp.include_routers(router_transl)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
