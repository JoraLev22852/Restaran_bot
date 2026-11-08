from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Milliy Taomlar",callback_data="milliytaom"),InlineKeyboardButton(text="Fast-Food",callback_data="fastfood")],
         [InlineKeyboardButton(text="Turk Taomlar",callback_data="turktaom"),InlineKeyboardButton(text="Ichimliklar",callback_data="ichimliklar")]
    ]
)

milliy_butons=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Osh",callback_data="osh"),InlineKeyboardButton(text="Somsa",callback_data="somsa")],
        [InlineKeyboardButton(text="Shashlik",callback_data="shashlik"),InlineKeyboardButton(text="Manti",callback_data="manti")]
    ]
)

fast_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Burger",callback_data="burger"),InlineKeyboardButton(text="Burrito",callback_data="burrito")],
        [InlineKeyboardButton(text="Pizza",callback_data="pizza"),InlineKeyboardButton(text="Tacos",callback_data="tacos")],
    ]
)
turktaom_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kebap",callback_data="kebap"),InlineKeyboardButton(text="Dolma",callback_data="dolma")],
        [InlineKeyboardButton(text="Pide",callback_data="pide"),InlineKeyboardButton(text="Sarma",callback_data="sarma")],
    ]
)
ichimliklar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Cola",callback_data="cola"),InlineKeyboardButton(text="Pepsi",callback_data="pepsi")],
        [InlineKeyboardButton(text="Sprite",callback_data="sprite"),InlineKeyboardButton(text="Fanta",callback_data="fanta")],
    ]
)
sonlar = InlineKeyboardBuilder()
for i in range(1,10):
    sonlar.button(text=f"{i}",callback_data=f"{i}")
sonlar.adjust(3)
