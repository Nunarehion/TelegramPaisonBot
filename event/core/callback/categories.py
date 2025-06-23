from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from messages.message import *
from event.router import logger

router = Router()

@router.callback_query(F.data == "query/categories")
async def query_about(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен запрос 'query/categories' от пользователя {callback.from_user.id}")
    await message_сategories(callback.message)
    await state.clear()
    await callback.answer()
    
@router.callback_query(F.data.startswith("query/categories/"))
async def query_about(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен запрос 'query/categories/{category}' от пользователя {callback.from_user.id}")
    category = callback.data.split("/")[-1]
    await message_categoria_name(callback.message, category)
    await state.clear()
    await callback.answer()
    
    

