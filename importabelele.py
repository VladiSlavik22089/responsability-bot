from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.callback import callbacks_router
from handlers.commands import command_router
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

import asyncio

from handlers.fsm_dopler import fsm_router

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot = bot,storage = storage)
dp.include_router(command_router)
dp.include_router(callbacks_router)
dp.include_router(fsm_router)


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
