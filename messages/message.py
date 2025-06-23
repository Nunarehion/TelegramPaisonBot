from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.markdown import text, hbold, italic, code, link
from aiogram.types import FSInputFile
from aiogram import types
from aiogram.fsm.context import FSMContext

from keyboards.buttons import kbPageStart, kbFaQ, kbPageAbout, kbPageCalcCategories

from keyboards.buttons import (
    kbPageStart,
    kbFaQ,
    kbPageAbout,
    kbPageCalcCategories,
    kbShoesCategories,
    kbClothingCategories,
    kbPantsCategories,
    # kbUnderwearCategories,
    # kbHatsCategories,
    kbSocksCategories,
    kbBagsCategories,
    # kbAccessoriesCategories,
    # kbCosmeticsCategories,
    # kbSportCategories,
    # kbFiguresCategories,
    kbAnswerAmount,
    kbSubNone
)


"""
# async def message_welcome(message: types.Message):
#     file = FSInputFile("images/header_image.jpg")
#     welcome_text = text(
#         "😉 Добро пожаловать в бот группы ", hbold("China Fairy Tale!"), "\n\n",
#         "Наша группа поможет Вам выкупить товары с ЛЮБЫХ китайских площадок, например:\n",
#         "1⃣ POIZON (DEWU)\n",
#         "2⃣ taobao.com\n",
#         "3⃣ и другие.\n\n",
#         "⛔️ Все расчеты, заказы и оплата производятся ТОЛЬКО В БОТЕ. Мы не принимаем оплату в личных сообщениях! ⛔️\n\n",
#         "⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров."
#     )
#     await message.answer_photo(photo=file, caption=welcome_text, parse_mode=ParseMode.HTML, reply_markup=kbPageStart())
"""

async def message_welcome(message: types.Message):
    file = FSInputFile("images/header_image.jpg")
    welcome_text = (
        "<b>"
            "Добро пожаловать в бот группы SINI!"
        "</b>"
        "\n\n"
        "Наша команда поможет вам выкупить товары с ЛЮБЫХ платформ."
        "\n\n"
        "В частности этот бот создан для расчета товаров из Китая"
        "\n"
        "(сумму нужно прописывать в юанях), для расчета товаров из США / Европы - пишите менеджеру."
        "\n\n"
        "<b>"
        "⚠️ Товар возврату и обмену не подлежит. Мы оказываем услуги только выкупа и доставки товаров. С нашей стороны вы можете рассчитывать на помощь в продаже если размер не подойдет или в полном возврате денежных средств если с вашим товаром что-то случится."
        "</b>"
    )
    await message.answer_photo(photo=file, caption=welcome_text, parse_mode=ParseMode.HTML, reply_markup=kbPageStart())


async def message_about(message: types.Message):
    file = FSInputFile("videos/video5276111355970089616.mp4")
    welcome_text = text(
        "Текстовый гайд как сделать заказ:",
        "POIZON - как правильно оформить заказ? (https://telegra.ph/POIZON---kak-pravilno-oformit-zakaz-09-27)"
    )
    fileID = "BAACAgIAAxkDAAIUM2hXxrqPynZNpyAyyRTSUKuWnLfoAAJIdAACm0PBSmhK9Jymj08eNgQ"
    await message.answer_video(video=fileID, caption=welcome_text, parse_mode=ParseMode.HTML, reply_markup=kbPageAbout())
    # print(msg.video.file_id)
    # BAACAgIAAxkDAAIUM2hXxrqPynZNpyAyyRTSUKuWnLfoAAJIdAACm0PBSmhK9Jymj08eNgQ
    

async def message_faq(message: types.Message):
    welcome_text = text(
        "😉 Ответы на самые популярные вопросы уже ждут Вас.",
    )
    await message.answer(welcome_text, parse_mode=ParseMode.HTML, reply_markup=kbFaQ())


async def message_сategories(message: types.Message):
    file = FSInputFile("images/header_image.jpg")
    welcome_text = (
    "📊 В нашем калькуляторе Вы можете сделать расчет стоимости товара с 🚚 доставкой до России."
    "\n\n"
    f"🔍 <u>Товары из приложения 95 выкупаем!</u> Подробно распишем почему цена ниже и есть ли моменты по товару 📝"
    "\n"
    f"💰 <u>Товары с ≈ ВЫКУПАЕМ!</u> Будет +10% к стоимости конечной цены при расчете 📈"
    "\n\n"
    f"<i>Это сделано из-за ограничений трансграничных покупок (касается товаров с Poizon из США / Европы / Японии / Тайваня)</i>"
    )
    await message.answer_photo(photo=file, caption=welcome_text, parse_mode=ParseMode.HTML, reply_markup=kbPageCalcCategories())
   

async def message_categoria_name(message: types.Message, category: str):
    category_messages = {
        # "sport": ("💬 Выберите подходящий раздел для спорта:", kbSportCategories),
        "shoes": ("💬 Выберите подходящий раздел для обуви:", kbShoesCategories),
        "clothing": ("💬 Выберите подходящий раздел для одежды:", kbClothingCategories),
        "pants": ("💬 Выберите подходящий раздел для штанов:", kbPantsCategories),
        # "underwear": ("💬 Выберите подходящий раздел для нижнего белья:", kbUnderwearCategories),
        # "hats": ("💬 Выберите подходящий раздел для головных уборов:", kbHatsCategories),
        "socks": ("💬 Выберите подходящий раздел для носок:", kbSocksCategories),
        "bags": ("💬 Выберите подходящий раздел для сумок:", kbBagsCategories),
        # "accessories": ("💬 Выберите подходящий раздел для аксессуаров:", kbAccessoriesCategories),
        # "cosmetics": ("💬 Выберите подходящий раздел для косметики:", kbCosmeticsCategories),
        # "figures": ("💬 Выберите подходящий раздел для фигурок:", kbFiguresCategories),
    }

    if category in category_messages:
        msg, keyboard_function = category_messages[category]
        await message.answer(msg, parse_mode=ParseMode.HTML, reply_markup=keyboard_function())
    else:
        await message.answer("Неизвестная категория.")
        

from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    waiting_for_price = State()
    
async def message_input_price(message: types.Message, state):
    file = FSInputFile("images/header_image.jpg")
    welcome_text = text(
        "📊 Напишите стоимость товара в юанях:"
    )
    await message.answer_photo(photo=file, caption=welcome_text, parse_mode=ParseMode.HTML)
    await state.set_state(Form.waiting_for_price)
    
 
async def message_subcategory_none(message: types.Message):
    msg = (
        "Если вашей категории нет в списке или - можете написать менеджеру для подробного расчета"
    )
    await message.answer(msg, parse_mode=ParseMode.HTML, reply_markup=kbSubNone())

def utilConvertAmountRU(amount):
    return  amount * 12

def utilConvertAmountUSD(amount, commission):
    result = utilConvertAmountRU(amount) * 0.14 + commission * 0.013
    return round(result)

def utilCalcAmount(amount, commission):
    return utilConvertAmountRU(amount) + commission

async def message_answer_amount(message: types.Message, amount):
    commission = 2500
    print( utilCalcAmount(amount, commission), utilConvertAmountUSD(amount, commission))
    msg = (
        f"💰 Итоговая стоимость товара <b>{utilCalcAmount(amount, commission)} рублей</b>"
        "\n\n"
        "<i>🚚 Доставка СДЭком по России до Вашего пункта выдачи оплачивается</i>"
        "<b> ОТДЕЛЬНО.</b>"
        "<i> Она рассчитывается после того как ваш товар приедет на склад в Москву</i>"
        "\n\n"
        "🚛 <b>Итоговая стоимость</b> - это конечная стоимость доставки товара до Москвы, включая комиссию сервиса, упаковку, страховку и комиссию платежной системы."
        "\n\n"
        "❤️ Стоимость может измениться в любую сторону только из-за курса!"
    )
    await message.answer(msg, parse_mode=ParseMode.HTML, reply_markup=kbAnswerAmount())