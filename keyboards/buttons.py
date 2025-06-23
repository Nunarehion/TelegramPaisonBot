from aiogram import types


btnBack = [types.InlineKeyboardButton(text="« Назад", callback_data="back")]
btnBackToCategories = [types.InlineKeyboardButton(text="« Назад", callback_data="query/categories")]

def kbPageStart():
    buttons = [
        [types.InlineKeyboardButton(text="❓ Как оформить заказ?", url="https://telegra.ph/Kak-zakazat-08-12-2")],
        [types.InlineKeyboardButton(text="💰 Калькулятор стоимости", callback_data="query/categories")],
        [types.InlineKeyboardButton(text="📝 Наши отзывы в телеграмм", url="https://t.me/sinistore")],
        [types.InlineKeyboardButton(text="📚 Ответы на популярные вопросы", callback_data="query/faq", disable_web_page_preview=True)],
        [types.InlineKeyboardButton(text="💬 Написать в ЛС", url="https://t.me/vdncv")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def kbPageAbout():
    buttons = [ btnBack, ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbFaQ():
    buttons = [
        [types.InlineKeyboardButton(text="Инструкция по приложению",  url="http://telegra.ph/Instrukciya-po-prilozheniyu-08-05")],
        [types.InlineKeyboardButton(text="Как заказать товар",  url="https://telegra.ph/Kak-zakazat-08-12-2")],
        [types.InlineKeyboardButton(text="Сроки доставки",  url="https://telegra.ph/Sroki-dostavki-08-12")],
        [types.InlineKeyboardButton(text="Процесс доставки",  url="https://telegra.ph/Process-dostavki-08-12")],
        [types.InlineKeyboardButton(text="Оплата заказа",  url="https://telegra.ph/Oplata-08-12-5")],
        [types.InlineKeyboardButton(text="Конечная стоимость",  url="https://telegra.ph/O-nas--CHasto-zadavaemye-voprosy-08-05")],
        [types.InlineKeyboardButton(text="Часто задаваемые вопросы ",  url="https://telegra.ph/O-nas--CHasto-zadavaemye-voprosy-08-05")],
        [types.InlineKeyboardButton(text="Вещи и обувь в наличии",  url="http://avito.ru/brands/i80571675")],
        btnBack
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def kbPageCalcCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="👟 Обувь", callback_data="query/categories/shoes"),
            types.InlineKeyboardButton(text="👕 Одежда", callback_data="query/categories/clothing")
        ],
        [
            types.InlineKeyboardButton(text="👖 Штаны", callback_data="query/categories/pants"),
            types.InlineKeyboardButton(text="🧦 Носки", callback_data="query/categories/socks")
        ],
        [
            types.InlineKeyboardButton(text="🧢 Головные уборы", callback_data="query/subcategory/hats/all"),
            types.InlineKeyboardButton(text="👜 Сумки / Рюкзаки", callback_data="query/categories/bags"),
        ],
        [
            types.InlineKeyboardButton(text="❓ Моей категории нет в списке", callback_data="query/subcategory/none"),
        ],
        btnBack
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def kbSubNone():
    buttons = [
        [types.InlineKeyboardButton(text="💬 Написать администратору", url="https://t.me/vdncv")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbShoesCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="👟 Кроссовки", callback_data="query/subcategory/shoes/sneakers"),
        ],
        [
            types.InlineKeyboardButton(text="👢 Ботинки", callback_data="query/subcategory/shoes/boots"),
            types.InlineKeyboardButton(text="👟 Кеды", callback_data="query/subcategory/shoes/sneakers")
        ],
        [
            types.InlineKeyboardButton(text="⚽ Бутсы", callback_data="query/subcategory/shoes/cleats"),
            types.InlineKeyboardButton(text="👞 Туфли", callback_data="query/subcategory/shoes/shoes")
        ],
        btnBackToCategories
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbClothingCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="👕 Футболки", callback_data="query/subcategory/clothing/tshirts"),
            types.InlineKeyboardButton(text="👚 Блузки", callback_data="query/subcategory/clothing/blouses")
        ],
        [
            types.InlineKeyboardButton(text="👖 Джинсы", callback_data="query/subcategory/clothing/jeans"),
            types.InlineKeyboardButton(text="👗 Платья", callback_data="query/subcategory/clothing/dresses")
        ],
        [
            types.InlineKeyboardButton(text="🧥 Куртки", callback_data="query/subcategory/clothing/jackets"),
            types.InlineKeyboardButton(text="🧥 Пальто", callback_data="query/subcategory/clothing/coats")
        ],
        btnBackToCategories
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbPantsCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="👖 Джинсы", callback_data="query/subcategory/pants/jeans"),
        ],
        [
            types.InlineKeyboardButton(text="👖 Спортивные", callback_data="query/subcategory/pants/sport"),
            types.InlineKeyboardButton(text="👖 Шорты", callback_data="query/subcategory/pants/shorts")
        ],
        btnBackToCategories
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

"""
def kbUnderwearCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="👙 Бикини", callback_data="query/subcategory/underwear/bikini"),
            types.InlineKeyboardButton(text="👙 Бюстгальтеры", callback_data="query/subcategory/underwear/brassieres")
        ],
        [
            types.InlineKeyboardButton(text="👙 Трусы", callback_data="query/subcategory/underwear/panties"),
            types.InlineKeyboardButton(text="👙 Нижнее белье", callback_data="query/subcategory/underwear/lingerie")
        ],
        btnBackToCategories
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbHatsCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="🧢 Бейсболки", callback_data="query/subcategory/hats/baseball_caps"),
            types.InlineKeyboardButton(text="🧢 Шляпы", callback_data="query/subcategory/hats/hats")
        ],
        [
            types.InlineKeyboardButton(text="🧢 Панамы", callback_data="query/subcategory/hats/panamas"),
            types.InlineKeyboardButton(text="🧢 Кепки", callback_data="query/subcategory/hats/caps")
        ],
        btnBack
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
"""

def kbSocksCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="🧦 Носки для спорта", callback_data="query/subcategory/socks/sport_socks"),
            types.InlineKeyboardButton(text="🧦 Повседневные носки", callback_data="query/subcategory/socks/casual_socks")
        ],
        [
            types.InlineKeyboardButton(text="🧦 Термоноски", callback_data="query/subcategory/socks/thermal_socks"),
            types.InlineKeyboardButton(text="🧦 Носки с рисунком", callback_data="query/subcategory/socks/patterned_socks")
        ],
        btnBackToCategories
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbBagsCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="👜 Сумки", callback_data="query/subcategory/bags/bags"),
            types.InlineKeyboardButton(text="🎒 Рюкзаки", callback_data="query/subcategory/bags/backpacks")
        ],
        [
            types.InlineKeyboardButton(text="🧳 Чемоданы", callback_data="query/subcategory/bags/suitcases"),
            types.InlineKeyboardButton(text="👜 Клатчи", callback_data="query/subcategory/bags/clutches")
        ],
        btnBack
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

"""
def kbAccessoriesCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="🧤 Перчатки", callback_data="query/subcategory/accessories/gloves"),
            types.InlineKeyboardButton(text="🧣 Шарфы", callback_data="query/subcategory/accessories/scarves")
        ],
        [
            types.InlineKeyboardButton(text="🕶️ Очки", callback_data="query/subcategory/accessories/glasses"),
            types.InlineKeyboardButton(text="📿 Украшения", callback_data="query/subcategory/accessories/jewelry")
        ],
        btnBack
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbCosmeticsCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="💄 Помады", callback_data="query/subcategory/cosmetics/lipsticks"),
            types.InlineKeyboardButton(text="💅 Лаки для ногтей", callback_data="query/subcategory/cosmetics/nail_polishes")
        ],
        [
            types.InlineKeyboardButton(text="🧴 Кремы", callback_data="query/subcategory/cosmetics/creams"),
            types.InlineKeyboardButton(text="🧴 Парфюмерия", callback_data="query/subcategory/cosmetics/perfumes")
        ],
        btnBack
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbSportCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="⚽ Футбол", callback_data="query/subcategory/sport/soccer"),
            types.InlineKeyboardButton(text="🏀 Баскетбол", callback_data="query/subcategory/sport/basketball")
        ],
        [
            types.InlineKeyboardButton(text="🏋️‍♂️ Фитнес", callback_data="query/subcategory/sport/fitness"),
            types.InlineKeyboardButton(text="🏊‍♂️ Плавание", callback_data="query/subcategory/sport/swimming")
        ],
        btnBack
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def kbFiguresCategories():
    buttons = [
        [
            types.InlineKeyboardButton(text="🧸 Игрушки", callback_data="query/subcategory/figures/toys"),
            types.InlineKeyboardButton(text="🧩 Конструкторы", callback_data="query/subcategory/figures/building_sets")
        ],
        [
            types.InlineKeyboardButton(text="🚀 Модели", callback_data="query/subcategory/figures/models"),
            types.InlineKeyboardButton(text="🎲 Настольные игры", callback_data="query/subcategory/figures/board_games")
        ],
        btnBack
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
"""

def kbAnswerAmount():
    buttons = [
        [types.InlineKeyboardButton(text="« Вернутся в калькулятор", callback_data="query/categories")], 
        [types.InlineKeyboardButton(text="Написать в ЛС", url="https://t.me/vdncv")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard