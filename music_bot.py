import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "TOKEN WHERE R UUUUUUUUU"
MY_CLOUDFLARE_URL = "https://viperrkaibot.pazan4ok.workers.dev/"

my_private_server = TelegramAPIServer.from_base(MY_CLOUDFLARE_URL)
session = AiohttpSession(api=my_private_server)

bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🪐 Kai Angel"), KeyboardButton(text="🧛 9mice")],
        [KeyboardButton(text="🦇 VIPERR (Совместные)"), KeyboardButton(text="🟣 АЛЬБОМ 25.09 (ДРОП)")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери артиста или релиз..."
)

kai_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔥 Для зала (Драйв Кая)"), KeyboardButton(text="💔 Грустный вайб Кая")],
        [KeyboardButton(text="💻 Под домашку / Код"), KeyboardButton(text="🔙 Главное меню")]
    ],
    resize_keyboard=True
)


mice_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⚡ Драйв Майса"), KeyboardButton(text="⛓️ Темный вайб Майса")],
        [KeyboardButton(text="🔙 Главное меню")]
    ],
    resize_keyboard=True
)


playlists = {
    
    "🔥 для зала (драйв кая)": (
        "🔊 *KAI ANGEL DRIVE (Для жесткого кача):*\n\n"
        "1️⃣ *OFFICE SONG* — электронный качающий трек с альбома 'shh!'. Мощный ритм, под который только и надо поднимать веса!\n"
        "2️⃣ *sting* — сольный релиз из ТГ-канала. Тяжелая грязная гитара, которая идеально подходит под очередной жесткий подход!\n"
        "3️⃣ *LIPSTICK* — совместный разрывной трек с 9mice с альбома 'HEAVY METAL'. Давящий бас и электрогитара как раз для совместных подходов с другом!\n"
        "4️⃣ *DANCE LIKE U IN PAIN* — инопланетный трек с 'GOD SYSTEM'. Идеален для того, чтобы ощущать себя настоящим GOD OF SYSTEM на тренировке! 💪\n\n"
        "🔗 [Слушать треки в профиле Kai Angel на SoundCloud](https://soundcloud.com)"
    ),
    "💔 грустный вайб кая": (
        "🌧 *KAI ANGEL MELANCHOLY (На подумать):*\n\n"
        "1️⃣ *flowers* — меланхоличный, глубокий звук и сильный текст с первой части 'Shh...'.\n"
        "2️⃣ *pleasure* — лиричная и меланхоличная гитарная композиция, пробирающая до мурашек, из того же 'Shh...'.\n"
        "3️⃣ *__slash__godmode* — уникальный контраст: одновременно динамичный бит и грустный, меланхоличный текст с 'GOD SYSTEM'.\n"
        "4️⃣ *damage* — эмоционально тяжелый, плотный и атмосферный трек с одноименного альбома. Идеально на ночной подумать. 🖤\n\n"
        "🔗 [Слушать треки в профиле Kai Angel на SoundCloud](https://soundcloud.com)"
    ),
    "💻 под домашку / код": (
        "☕ *KAI ANGEL FOCUS (Фоновый звук для учебы):*\n\n"
        "1️⃣ *limousine music* — ровный, очень стильный синти-поп ритм с 'Shh...'. Помогает сосредоточиться и не отвлекает от задач.\n"
        "2️⃣ *madam* — спокойный рэп под красивый бит о любви с альбома 'damage'. Отличный фоновый саунд.\n"
        "3️⃣ *GOD SYSTEM* — те самые легендарные 10 минут глубокого эмбиента без слов. Чистый фокус для погружения в Python. 💻\n"
        "4️⃣ *lovesong* — любовный сингл со спокойным, размеренным битом и мягким текстом.\n\n"
        "🔗 [Слушать треки в профиле Kai Angel на SoundCloud](https://soundcloud.com)"
    ),
    
    
    "⚡ драйв майса": (
        "🔊 *9MICE DRIVE (Максимальный разгон в зале):*\n\n"
        "1️⃣ *BELLA* — плотный и качающий трек в фирменном стиле Майса с альбома 'ASPHALT'. Задает правильный темп тренировке!\n"
        "2️⃣ *RIOT MUSIK* — агрессивный и современный рэп-сингл с мощным, плотным звучанием из того же тейпа 'ASPHALT'.\n"
        "3️⃣ *kill bill __slash__ evian* — дерзкий, жесткий и максимально агрессивный как содержательно, так и стилистически релиз из альбома '9MM'.\n"
        "4️⃣ *FACE* — чистый грязный опиум-рэп о высокой моде с агрессивным и гипнотическим басом с альбома 'ORPHEUS'. Разнос наушников! ⚡\n\n"
        "🔗 [Слушать треки в профиле 9mice на SoundCloud](https://soundcloud.com)\n\n"
        "⚠️ *P.S. SoundCloud заблокирован в РФ. Ссылка откроется только с включенным VPN!*"
    ),
    "⛓️ темный вайб майса": (
        "🧛 *9MICE GOTHIC (Фирменный мрачный вайб 999999):*\n\n"
        "1️⃣ *jenna* — трек с альбома '9MM'. Агрессивный рейдж-трек о загадочной девушке с мрачной, тяжелой энергетикой в стиле Дженны Ортеги.\n"
        "2️⃣ *famous* — дерзкий и пафосный опиум-репрезент Майса под сумасшедший бит от топового американского продюсера F1LTHY с альбома '9MM'.\n"
        "3️⃣ *XO4ET* — минималистичный, холодный и пугающе агрессивный рейдж-трек с тяжелым, давящим басом с альбома 'ORPHEUS'.\n"
        "4️⃣ *Y3BOK* — грязный и дерзкий опиум-бэнгер с тейпа 'ASPHALT' на перегруженный бит от weluvneon. Пропитан пафосом и атмосферой ночного стрит-рейва! ⛓️\n\n"
        "🔗 [Слушать треки в профиле 9mice на SoundCloud](https://soundcloud.com)\n\n"
        "⚠️ *P.S. SoundCloud заблокирован в РФ. Ссылка откроется только с включенным VPN!*"
    ),
    
   
        "🦇 viperr (совместные)": (

        "🦇 *VIPERR ANTHEMS (Главные совместные фиты дуэта):*\n\n"
        "👑 *HEAVY METAL* — легендарный трек, который перевернул игру в СНГ и задал новый вектор всему стилю.\n"
        "👑 *da vinci* — гипнотический опиум-бэнгер с плотным, обволакивающим звуком из альбома 'Heavy Metal 2'. Дуэт филигранно сочетает пафосный репрезент о высокой моде с мрачной нуарной эстетикой.\n"
        "👑 *phoenix* — напористый опиум-трек из 'Heavy Metal 2' под плотный футуристичный бит. Артисты транслируют идеи превосходства над индустрией и верности своему темному стилю.\n"
        "👑 *риноплaстика (surgery)* — ультракороткий, цикличный и гиперагрессивный трек. Под ломаный перегруженный бит дуэт VIPERR метафорично сравнивает изменение рэп-индустрии со 'сменой лиц' на пластической операции! 🏥\n\n"
        "🔗 [Слушать VIPERR на SoundCloud](https://soundcloud.com)"
    ),
    "🟣 альбом 25.09 (дроп)": (
        "⏳ *ОЖИДАНИЕ ФИОЛЕТОВОГО РЕЛИЗА (25 СЕНТЯБРЯ)* ⏳\n\n"
        "По всем теориям, финальный диск трилогии SHH / HEAVY METAL 3 выйдет ровно через неделю!\n"
        "Включай VPN и следи за обновлениями в профилях артистов, чтобы услышать дроп первыми:\n\n"
        "🔗 [SoundCloud Kai Angel](https://soundcloud.com)\n"
        "🔗 [SoundCloud 9mice](https://soundcloud.com)"
    )
}


mood_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🪐 Kai Angel"), KeyboardButton(text="🧛 9mice")],
        [KeyboardButton(text="🦇 VIPERR (Совместные)"), KeyboardButton(text="🟣 АЛЬБОМ 25.09 (ДРОП)")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Вайбим под релизы VIPERR..."
)

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        f"🪐 Привет, {message.from_user.first_name}!\n\n"
        f"Добро пожаловать в объединенный *VIPERR инфо-бот* Кая Ангела и 9mice! 🦇\n"
        f"Выбирай артиста на кнопках внизу, чтобы открыть его плейлисты! 👇",
        reply_markup=mood_keyboard
    )

@dp.message(lambda msg: msg.text == "🔙 Главное меню")
async def back_to_main(message: types.Message):
    await message.answer("Возвращаемся в главное меню VIPERR:", reply_markup=mood_keyboard)

@dp.message(lambda msg: msg.text == "🪐 Kai Angel")
async def show_kai_menu(message: types.Message):
    await message.answer("Выбрано меню Kai Angel. Выбери вайб треков:", reply_markup=kai_keyboard)

@dp.message(lambda msg: msg.text == "🧛 9mice")
async def show_mice_menu(message: types.Message):
    await message.answer("Выбрано меню 9mice. Выбери вайб треков:", reply_markup=mice_keyboard)

@dp.message()
async def handle_playlists(message: types.Message):
    user_choice = message.text.lower().strip()
    
    found = False
    for mood_key, playlist_text in playlists.items():
        if user_choice in mood_key:
            await message.answer(playlist_text, parse_mode="Markdown", disable_web_page_preview=True)
            found = True
            break
            
    if not found:
        await message.answer("🤫 Тсс... Не понял команду. Используй кнопки меню!")

async def main():
    print("Супер-бот VIPERR успешно запущен через Cloudflare!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
