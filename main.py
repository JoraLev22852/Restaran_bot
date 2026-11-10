import asyncio
from os import getenv
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart
from aiogram.types import Message,CallbackQuery,InputMediaPhoto
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from button import *

from aiogram.client.session.aiohttp import AiohttpSession
session = AiohttpSession(proxy="http://proxy.server:3128")

BOT_TOKEN = "9244726768:AAG2CseWa9yH25jwlJPYuJ0NAqyfEO_qZe0"
TOKEN = BOT_TOKEN
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp =Dispatcher()

@dp.message(CommandStart())
async def camanda (message:Message):
    await message.answer("Salom Kino turini tallang",reply_markup=menu)
    

#millitaomlar

@dp.callback_query(F.data == "milliytaom")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://uzbekistan.travel/storage/app/media/wepb/gastro_turizm/cropped-images/%D0%94%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%20%D0%B1%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-0-0-0-0-1740051502.webp"),reply_markup=milliy_butons)
    await callback.answer("Milliy Taomlar")

    
@dp.callback_query(F.data == "osh")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://arbuz.com/wp-content/uploads/2009/12/Uzbek-Palov.jpg",
     caption="""Osh (yoki palov) — oʻzbek milliy oshxonasining shoh taomi, oʻzbek madaniyati va mehmondoʻstligining bosh ramzidir. Guruch, goʻsht, sabzi va piyoz kabi asosiy masalliqlardan qozonda pishiriladigan ushbu taom 2016-yilda UNESCO Nomoddiy madaniy meros roʻyxatiga kiritilgan.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "somsa")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://arbuz.com/wp-content/uploads/2009/07/Somsa-Samosa-Sambusa.jpg",
     caption="""The name somsa primarily refers to a traditional savory baked pastry prominent across Central Asian cuisines, but it is also the acronym for the Society of OMS Administrators""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()


@dp.callback_query(F.data == "shashlik")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://recipeworld.blog/recipes/shashlik.webp",
     caption="""Shashlik is a popular traditional dish of skewered, marinated, and grilled cubes of meat that originated in Central Asia, the Caucasus, and Eastern Europe. Derived from the Turkic word shish, meaning "skewer," it is a direct relative of the shish kebab but is distinguished primarily by its larger chunks of meat and uniquely tangy, acidic marinades. Across many post-Soviet states and Eastern Europe, preparing shashlik on a mangal (an open-top charcoal grill) serves as a popular backyard and social picnic staple, much like a traditional barbecue.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()


@dp.callback_query(F.data == "manti")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://i0.wp.com/kennascooks.com/wp-content/uploads/2025/02/img_8610.jpg?w=1080&ssl=1",
     caption="""Manti (also spelled mantı) is a traditional type of dumpling popular across Turkish, Armenian, Central Asian, and Caucasian cuisines. Originating as a shared nomadic culinary heritage transported from Central Asia westward during the 13th century, these tiny parcels typically consist of thin wheat dough sheets stuffed with a spiced mixture of ground beef or lamb and finely minced onion.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

#millitoamlar tamom

#fast-food

@dp.callback_query(F.data == "fastfood")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU0yuXfpWUe5rY0cBELIwFKEyG1bHo0sJiHvGqULTn_6-j-TLuelA0wp1g&s=10"),reply_markup=fast_button)
    await callback.answer("Fast food")


@dp.callback_query(F.data == "burger")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrsYKgD_tebeVuk-NhQJy196N0HSkvpjZCurNEwASnyLUxQ2x9dI8dR4c&s=10",
     caption="""Бургер (гамбургер) — это популярное блюдо, состоящее из разрезанной пополам булочки и вложенной внутрь рубленой жареной котлеты, которая дополняется овощами, соусами и расплавленным сыром. Слово «бургер» является общим названием для всей категории таких сэндвичей, а его классической разновидностью считается гамбургер с говяжьей котлетой, луком, огурцами и соусом, но без сыра""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "burrito")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://villacocina.com/wp-content/uploads/2023/06/Burrito-Supremo-WEBSITE--1024x683.jpg",
     caption="""Burrito — bugʻdoy unidan tayyorlangan yupqa non (tortilya) ichiga turli masalliqlar solib, oʻralgan anʼanaviy Meksika taomidir. Uning nomi ispanchadan tarjima qilinganda "kichkina eshakcha" degan maʼnoni anglatadi.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "pizza")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://www.liveeatlearn.com/wp-content/uploads/2025/09/Veggie-Pizza-12.jpg",
     caption="""Pitsa (Pizza) — tayyorlanishi va ko'rinishi bo'yicha dunyodagi eng ommabop taomlardan biri bo'lib, xamirdan yasalgan yumaloq korj (tekis non) ustiga turli masalliqlar terib, pechda pishiriladigan italyan milliy taomidir.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "tacos")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7K6q4zhfn1u20drJCKydB5eoH1t-sH1UYQsRhHBzLCevK185Q4Ddq9f6J&s=10",
     caption="""Tako (Taco) — makkajoʻxori yoki bugʻdoy unidan tayyorlangan kichik tortilla (kulcha) ichiga goʻsht, sabzavotlar, pishloq va turli ziravorlar solib tayyorlanadigan anʼanaviy Meksika taomidir. Uni odatda qoʻlda buklab, issiqligida isteʼmol qilinadi""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

#fast-food tamom

#turktaom

@dp.callback_query(F.data == "turktaom")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://thumb.wikimedia.org/wikipedia/commons/thumb/5/51/Baklava_1.jpg/250px-Baklava_1.jpg?utm_source=uz.wikipedia.org&utm_campaign=parser&utm_content=thumbnail")
     ,reply_markup=turktaom_button)
    await callback.answer("turktaom")

@dp.callback_query(F.data == "kebap")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://www.kitchenstories.com/wp-content/uploads/sites/13/2026/09/r3490-adana-kebap.jpg",
     caption="""Kebap (kabob) — olovda, qoʻrda (koʻmirda) yoki tandirda pishiriladigan, asosan goʻshtdan tayyorlanadigan dunyoga mashhur taomlar guruhidir [5.2]. Uning vatani Yaqin va Oʻrta Sharq hisoblanib, soʻzning oʻzi qadimgi oromiy (shom) tilidagi "kabāba" (kuydirish, olovda pishirish) soʻzidan kelib chiqqan.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()


@dp.callback_query(F.data == "dolma")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://images.immediate.co.uk/production/volatile/sites/30/2024/11/Dolma-c52e916.jpg",
     caption="""Dolma — uzum bargi, karom yoki turli sabzavotlar (qalampir, pomidor, baqlajon) ichini go'shtli va guruchli qiyma bilan to'ldirib pishiriladigan an'anaviy Yaqin Sharq va Markaziy Osiyo taomidir. Bu so'z turkiy "dolmak" (to'ldirmoq, tiqmoq) fe'lidan kelib chiqqan bo'lib, Usmonli imperiyasi oshxonasida shakllangan va butun dunyoga tarqalgan. Ayniqsa, O'zbekistonda bahor va yoz oylarida yangi uzilgan tok barglaridan tayyorlanadigan "tok dolma" juda mashhur hisoblanadi.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "pide")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUjSpvIHSELhx96VeLUWY9bS6hUTJ5HnkDjMEHvhiTDA&s=10",
     caption="""Pide — bu turk oshxonasining mashhur va lazzatli taomi boʻlib, u qayiqsimon shakldagi yassi xamir (tekis non) ustiga turli masalliqlar solib pishiriladigan milliy pissa turidir. Odatda uning ustiga maydalangan qiyma goʻsht, pishloq, sosiska yoki sabzavotlar solib, pechda qaynoq holatda pishiriladi.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "sarma")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQr0otT3JAPHIjUSx5syxDPa3EPMGxvC-PRWuHZsQdqRMgnhjZt-xUzab0E&s=10",
     caption="""Sarma — turkiy, Yaqin Sharq va Bolqon oshxonalariga mansub, ichiga guruch, bulgʻor yormasi va qiyma solib, turli oʻsimlik barglariga oʻrab pishiriladigan anʼanaviy taomdir. Uning nomi turkcha "sarmak" (заворачивать / oʻramoq) soʻzidan kelib chiqqan. Oʻzbek oshxonasidagi kava tok oshi (kovtok dolma) sarmaga juda yaqin variant hisoblanadi.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

#turktaom taom 

#ichimliklar


@dp.callback_query(F.data == "ichimliklar")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://zamin.uz/uploads/posts/2025-02/f250d5996a_95330eb04a00f51352f36c119e192741_original_263442.webp")
     ,reply_markup=ichimliklar_button)
    await callback.answer("turktaom")

@dp.callback_query(F.data == "cola")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBA_kAIMyLpbt29UC3pSJ51musVOXDvW4Mr3z610VyOQ&s=10",
     caption="""Coca-Cola (yoki oddiygina Kola) — dunyodagi eng mashhur gazlangan salkam ichimliklardan biridir.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "pepsi")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8wXy4x8JKpf63bW3xOA-yavbkkiCjzhIQhjHI0SrUpg&s=10",
     caption="""Pepsi — butun dunyoda mashhur boʻlgan alkogolsiz gazlangan kola ichimligi boʻlib, u AQShning PepsiCo kompaniyasi tomonidan ishlab chiqariladi. Ichimlik ilk bor 1893-yilda farmatsevt Caleb Bradham tomonidan "Brad's Drink" nomi bilan ixtiro qilingan va keyinchalik 1898-yilda Pepsi-Cola deb qayta nomlangan.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

@dp.callback_query(F.data == "sprite")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://static.wikia.nocookie.net/the-soda-encyclopedia/images/d/d7/Sprite.png/revision/latest?cb=20200822143050",
     caption="""Sprite koʻpincha quyidagi asosiy maʼnolardan birini anglatadi.""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()


@dp.callback_query(F.data == "fanta")
async def milliy(callback: CallbackQuery):
    await callback.message.edit_media(media=InputMediaPhoto(media="https://images.albertsons-media.com/is/image/ABS/960130209-C1N1?$ng-ecom-pdp-mobile$&defaultImage=Not_Available  ",
     caption="""Fanta — The Coca-Cola Company korporatsiyasiga tegishli dunyodagi eng mashhur meva ta'mli gazlangan salqin ichimliklar brendidir. Bugungi kunda u dunyoning 180 dan ortiq mamlakatlarida 100 dan ziyod ta'm turida sotiladi, biroq uning eng tanilgan va eng ko'p sotiladigan turi klassik apelsin (Fanta Orange) hisoblanadi""")
     ,reply_markup=sonlar.as_markup())
    await callback.answer()

#ichimliklar taom

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
