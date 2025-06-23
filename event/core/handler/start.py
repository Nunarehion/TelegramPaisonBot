from aiogram import Router, types, F
from aiogram.filters import Command

from event.router import logger
from messages.message import *



router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    logger.info(f"Получена команда /start от пользователя {message.from_user.id}")
    await state.clear()
    await message_welcome(message)
