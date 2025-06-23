from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from event.router import logger
from messages.message import *

router = Router()

@router.callback_query(F.data == "back")
async def query_back(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен запрос 'back' от пользователя {callback.from_user.id}")
    await message_welcome(callback.message)
    await callback.answer()
    await state.clear()