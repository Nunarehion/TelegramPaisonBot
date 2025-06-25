from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.context import FSMContext

from event.router import logger
from messages.message import *

router = Router()

@router.callback_query(F.data.startswith("query/subcategory/"))
async def query_subcategory(callback: CallbackQuery,  state: FSMContext):
    parts = callback.data.split("/")
    if len(parts) >= 3:
        subcategory = parts[-2]
        item = parts[-1]
        print(f"Subcategory: {subcategory}, Item: {item}  {parts}")
        logger.info(f"Получен запрос 'query/subcategory/{subcategory}/{item}' от пользователя {callback.from_user.id}. Полные данные: {parts}")
        await state.update_data(subcategory=subcategory, item=item)
        if item == "none":
            await message_subcategory_none(callback.message)
        else:
            await message_input_price(callback.message, state)
    # await state.clear()
    await callback.answer()
    