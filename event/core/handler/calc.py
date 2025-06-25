from aiogram import Router, types, F
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext

from event.router import logger
from messages.message import *



router = Router()

@router.message(Form.waiting_for_price)
async def handle_price_input(message: types.Message, state: FSMContext):
    logger.info(f"Вызван калькулятор от пользователя {message.from_user.id}. Введенное значение: '{message.text}'")
    data = await state.get_data()
    subcategory = data.get('subcategory')
    item = data.get('item')
    if message.text.isdigit():
        price = int(message.text)
        logger.info(f"Пользователь {message.from_user.id} ввел корректную цену: {price}")
        await message_answer_amount(message, price, subcategory, item)
        await state.clear()
    else:
        logger.warning(f"Пользователь {message.from_user.id} ввел некорректное значение: '{message.text}'")
        await message.answer("⚠️ <b>Ошибка: Повторите ввод.</b> \nПожалуйста, введите <u>только цифры</u>.", parse_mode="HTML")
        await state.set_state(Form.waiting_for_price)
        # await message_input_price(message, state)
    

