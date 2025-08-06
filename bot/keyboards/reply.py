from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def get_language_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton("O'zbekcha")],
        [KeyboardButton("Русский")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_contact_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        text = "Telefon raqamingizni yuboring:"
    else:
        text = "Отправьте ваш номер телефона:"

    keyboard = [[KeyboardButton(text, request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_city_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        cities = ["Toshkent", "Samarqand", "Buxoro", "Andijon"]
    else:
        cities = ["Ташкент", "Самарканд", "Бухара", "Андижан"]

    keyboard = [[KeyboardButton(city)] for city in cities]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_main_menu_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        keyboard = [
            [KeyboardButton("Gadget turini tanlang")],
            [KeyboardButton("Buyurtma berish"), KeyboardButton("Mening buyurtmalarim")],
            [KeyboardButton("Sozlamalar")],
        ]
    else:
        keyboard = [
            [KeyboardButton("Выберите тип гаджета")],
            [KeyboardButton("Сделать заказ"), KeyboardButton("Мои заказы")],
            [KeyboardButton("Настройки")],
        ]
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

def get_gadget_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("Telefon", callback_data="telefon")],
            [InlineKeyboardButton("Planshet", callback_data="plansher")],
            [InlineKeyboardButton("Smart Soat", callback_data="smart_soat")],
            [InlineKeyboardButton("Quloqchinlar", callback_data="quloqchinlar")],
        ]
    else:
        inline_keyboard = [
    [InlineKeyboardButton("Телефон", callback_data="telefon")],
    [InlineKeyboardButton("Планшет", callback_data="plansher")],
    [InlineKeyboardButton("Смарт часы", callback_data="smart_soat")],
    [InlineKeyboardButton("Наушники", callback_data="quloqchinlar")],
]

    
    return InlineKeyboardMarkup(inline_keyboard)

def get_telefon_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("Apple", callback_data="apple_telefon")],
            [InlineKeyboardButton("Samsung", callback_data="samsung_telefon")],
            [InlineKeyboardButton("Redmi Xiaomi", callback_data="redmi_telefon")],
        ]
    else:
        inline_keyboard = [
            [InlineKeyboardButton("Эппл", callback_data="Эппл")],
            [InlineKeyboardButton("Самсунг", callback_data="самсунг")],
            [InlineKeyboardButton("Редми Сяоми", callback_data="Редми Сяоми")],
        ]
    
    return InlineKeyboardMarkup(inline_keyboard)

def get_apple_telefon_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("iPhone X", callback_data="apple_telefon_x")],
            [InlineKeyboardButton("iPhone 11", callback_data="apple_telefon_11")],
            [InlineKeyboardButton("iPhone 11 Pro", callback_data="apple_telefon_11_pro")],
            [InlineKeyboardButton("iPhone 11 Pro Max", callback_data="apple_telefon_11_pro_max")],
            [InlineKeyboardButton("iPhone 12", callback_data="apple_telefon_12")],
            [InlineKeyboardButton("iPhone 12 Pro", callback_data="apple_telefon_12_pro")],
            [InlineKeyboardButton("iPhone 12 Pro Max", callback_data="apple_telefon_12_pro_max")],
            [InlineKeyboardButton("iPhone 13 ", callback_data="apple_telefon_13")],
            [InlineKeyboardButton("iPhone 13 Pro", callback_data="apple_telefon_13_pro")],
            [InlineKeyboardButton("iPhone 13 Pro Max", callback_data="apple_telefon_13_pro_max")],
            [InlineKeyboardButton("iPhone 14 ", callback_data="apple_telefon_14")],
            [InlineKeyboardButton("iPhone 14 Pro", callback_data="apple_telefon_14_pro")],
            [InlineKeyboardButton("iPhone 14 Pro Max", callback_data="apple_telefon_14_pro_max")],
            [InlineKeyboardButton("iPhone 15", callback_data="apple_telefon_15")],
            [InlineKeyboardButton("iPhone 15 Pro ", callback_data="apple_telefon_15_pro")], 
            [InlineKeyboardButton("iPhone 15 Pro Max", callback_data="apple_telefon_15_pro_max")],
            [InlineKeyboardButton("iPhone 16 ", callback_data="apple_telefon_16")],
            [InlineKeyboardButton("iPhone 16 Pro ", callback_data="apple_telefon_16_pro")],
            [InlineKeyboardButton("iPhone 11 Pro Max", callback_data="apple_telefon_16_pro_max")],
            [InlineKeyboardButton("Chiqish", callback_data="chiqish")],         


        ]
    else:
        inline_keyboard = [
            [InlineKeyboardButton("Айфон X", callback_data="apple_telefon_x")],
            [InlineKeyboardButton("Айфон 11", callback_data="apple_telefon_11")],
            [InlineKeyboardButton("Айфон 11 Про", callback_data="apple_telefon_11_pro")],
            [InlineKeyboardButton("Айфон 11 Про Макс", callback_data="apple_telefon_11_pro_max")],
            [InlineKeyboardButton("Айфон 12", callback_data="apple_telefon_12")],
            [InlineKeyboardButton("Айфон 12 Про", callback_data="apple_telefon_12_pro")],
            [InlineKeyboardButton("Айфон 12 Про Макс", callback_data="apple_telefon_12_pro_max")],
            [InlineKeyboardButton("Айфон 13", callback_data="apple_telefon_13")],
            [InlineKeyboardButton("Айфон 13 Про", callback_data="apple_telefon_13_pro")],
            [InlineKeyboardButton("Айфон 13 Про Макс", callback_data="apple_telefon_13_pro_max")],
            [InlineKeyboardButton("Айфон 14", callback_data="apple_telefon_14")],
            [InlineKeyboardButton("Айфон 14 Про", callback_data="apple_telefon_14_pro")],
            [InlineKeyboardButton("Айфон 14 Про Макс", callback_data="apple_telefon_14_pro_max")],
            [InlineKeyboardButton("Айфон 15", callback_data="apple_telefon_15")],
            [InlineKeyboardButton("Айфон 15 Про", callback_data="apple_telefon_15_pro")], 
            [InlineKeyboardButton("Айфон 15 Про Макс", callback_data="apple_telefon_15_pro_max")],
            [InlineKeyboardButton("Айфон 16", callback_data="apple_telefon_16")],
            [InlineKeyboardButton("Айфон 16 Про", callback_data="apple_telefon_16_pro")],
            [InlineKeyboardButton("Айфон 16 Про Макс", callback_data="apple_telefon_16_pro_max")],
            [InlineKeyboardButton("Выход", callback_data="chiqish")],
        ]
    
    return InlineKeyboardMarkup(inline_keyboard)


def get_samsung_telefon_keyboard(language: str) -> InlineKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("Samsung Galaxy S20", callback_data="samsung_s_20")],
            [InlineKeyboardButton("Samsung Galaxy S21", callback_data="samsung_s_21")],
            [InlineKeyboardButton("Samsung Galaxy S22", callback_data="samsung_s_22")],
            [InlineKeyboardButton("Samsung Galaxy S23", callback_data="samsung_s_23")],
            [InlineKeyboardButton("Samsung Galaxy S24", callback_data="samsung_s_24")],
            [InlineKeyboardButton("Samsung Galaxy S25", callback_data="samsung_s_25")],
        ]
        inline_keyboard = [
            [InlineKeyboardButton("Самсунг Галакси S20", callback_data="samsung_s_20")],
            [InlineKeyboardButton("Самсунг Галакси S21", callback_data="samsung_s_21")],
            [InlineKeyboardButton("Самсунг Галакси S22", callback_data="samsung_s_22")],
            [InlineKeyboardButton("Самсунг Галакси S23", callback_data="samsung_s_23")],
            [InlineKeyboardButton("Самсунг Галакси S24", callback_data="samsung_s_24")],
            [InlineKeyboardButton("Самсунг Галакси S25", callback_data="samsung_s_25")],
        ]

    return InlineKeyboardMarkup(inline_keyboard)



def get_redmi_xiomi_telefon_keyboard(language: str) -> InlineKeyboardMarkup:
    if language == "O'zbekcha":
        inline_keyboard = [
            [InlineKeyboardButton("Redmi Note 7", callback_data="redmi_note_7")],
            [InlineKeyboardButton("Redmi Note 8", callback_data="redmi_note_8")],
            [InlineKeyboardButton("Redmi Note 9", callback_data="redmi_note_9")],
            [InlineKeyboardButton("Redmi Note 10", callback_data="redmi_note_10")],
            [InlineKeyboardButton("Redmi Note 11", callback_data="redmi_note_11")],
            [InlineKeyboardButton("Redmi Note 12", callback_data="redmi_note_12")],
            [InlineKeyboardButton("Redmi Note 13", callback_data="redmi_note_13")],
        ]

    else:
        inline_keyboard = [
            [InlineKeyboardButton("Редми Ноут 7", callback_data="redmi_note_7")],
            [InlineKeyboardButton("Редми Ноут 8", callback_data="redmi_note_8")],
            [InlineKeyboardButton("Редми Ноут 9", callback_data="redmi_note_9")],
            [InlineKeyboardButton("Редми Ноут 10", callback_data="redmi_note_10")],
            [InlineKeyboardButton("Редми Ноут 11", callback_data="redmi_note_11")],
            [InlineKeyboardButton("Редми Ноут 12", callback_data="redmi_note_12")],
            [InlineKeyboardButton("Редми Ноут 13", callback_data="redmi_note_13")],
        ]

    return InlineKeyboardMarkup(inline_keyboard)