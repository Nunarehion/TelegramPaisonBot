import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_reader import config
from event.router import router
# from aiogram.types import FSInputFile

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN.get_secret_value())
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Бот запущен. Начинаю опрос...")
    # file = FSInputFile("videos/video5276111355970089616.mp4")
    # file_id = bot.get_file(file)
    # print(file_id)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
