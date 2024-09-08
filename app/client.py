import asyncio
import logging
import sys

from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import TG_BOT_TOKEN
from handlers import router

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

async def main() -> None:
    dp.include_router(router)
    bot = Bot(TG_BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')