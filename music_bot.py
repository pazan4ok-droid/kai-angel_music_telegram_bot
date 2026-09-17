import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ТВОЙ РАБОЧИЙ ТОКЕН И ССЫЛКА ОБЛАКА (Вставь сюда токен от BotFather)
TOKEN = "TOKEN AUUUUU WHERE R UUUU"
MY_CLOUDFLARE_URL = "https://viperrkaibot.pazan4ok.workers.dev/"

my_private_server = TelegramAPIServer.from_base(MY_CLOUDFLARE_URL)
session = AiohttpSession(api=my_private_server)

bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

# База данных треков, собранная лично тобой по канонам VIPERR
playlists = {
    "🔥 для зала (драйв)": (
        "🔊 *VIPERR DRIVE PLAYLIST (Для зала и жесткого кача):*\n\n"
        "1️⃣ *OFFICE SONG* — электронный качающий трек с альбома 'shh!'. Мощный ритм, под который только и надо поднимать веса!\n"
        "2️⃣ *sting* — сольный релиз из ТГ-канала. Тяжелая грязная гитара, которая идеально подходит под очередной жесткий подход!\n"
        "3️⃣ *LIPSTICK* — совместный разрывной трек с 9mice с альбома 'HEAVY METAL'. Давящий бас и электрогитара как раз для совместных подходов с другом!\n"
        "4️⃣ *DANCE LIKE U IN PAIN* — инопланетный трек с 'GOD SYSTEM'. Идеален для того, чтобы ощущать себя настоящим GOD OF SYSTEM на тренировке! 💪\n\n"
        "🔗 [Слушать треки в профиле Kai Angel на SoundCloud](https://soundcloud.com)\n\n"
        "⚠️ *P.S. SoundCloud заблокирован в РФ. Ссылка откроется только с включенным VPN!*"
    ),
    "💔 грустный вайб": (
        "🌧 *VIPERR MELANCHOLY (Погрустить / Подумать):*\n\n"
        "1️⃣ *flowers* — меланхоличный, глубокий звук и сильный текст с первой части 'Shh...'.\n"
        "2️⃣ *pleasure* — лиричная и меланхоличная гитарная композиция, пробирающая до мурашек, из того же 'Shh...'.\n"
        "3️⃣ *__slash__godmode* — уникальный контраст: одновременно динамичный бит и грустный, меланхоличный текст с 'GOD SYSTEM'.\n"
        "4️⃣ *damage* — эмоционально тяжелый, плотный и атмосферный трек с одноименного альбома. Идеально на ночной подумать. 🖤\n\n"
        "🔗 [Слушать треки в профиле Kai Angel на SoundCloud](https://soundcloud.com)\n\n"
        "⚠️ *P.S. SoundCloud заблокирован в РФ. Ссылка откроется только с включенным VPN!*"
    ),
    "💻 под домашку / код": (
        "☕ *VIPERR FOCUS (Фоновый звук для учебы и вайб-кодинга):*\n\n"
        "1️⃣ *limousine music* — ровный, очень стильный синти-поп ритм с 'Shh...'. Помогает сосредоточиться и не отвлекает от задач.\n"
        "2️⃣ *madam* — спокойный рэп под безумно красивый бит о любви с альбома 'damage'. Отличный фоновый саунд.\n"
        "3️⃣ *GOD SYSTEM* — те самые легендарные 10 минут глубокого эмбиента без слов. Чистый фокус для погружения в Python. 💻\n"
        "4️⃣ *lovesong* — любовный сингл со спокойным, размеренным битом и мягким текстом.\n\n"
        "🔗 [Слушать треки в профиле Kai Angel на SoundCloud](https://soundcloud.com)\n\n"
        "⚠️ *P.S. SoundCloud заблокирован в РФ. Ссылка откроется только с включенным VPN!*"
    ),
    "🟣 новый альбом (дроп)": (
        "🔥 *ФИОЛЕТОВАЯ ЧАСТЬ ТРИЛОГИИ ТУТ!* 🔥\n\n"
        "Третья часть масштабного арт-проекта Кая официально вышла на площадки!\n"
        "Смешение синего поп-рока и красного тяжелого трэпа.\n\n"
        "Включай VPN, переходи в профиль артиста и слушай свежий звук самым первым:\n"
        "🔗 [Слушать НОВЫЙ ДРОП на SoundCloud](https://soundcloud.com)"
    )
}

# Главная клавиатура (названия плейлистов строго сохранены!)
mood_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔥 Для зала (Драйв)"), KeyboardButton(text="💔 Грустный вайб")],
        [KeyboardButton(text="💻 Под домашку / Код"), KeyboardButton(text="🟣 НОВЫЙ АЛЬБОМ (ДРОП)")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Вайбим под релиз Кая Ангела..."
)

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        f"🪐 Привет, {message.from_user.first_name}!\n\n"
        f"Я твой музыкальный гид по SoundCloud-трекам *Kai Angel* под ночной релиз трилогии.\n"
        f"Выбери вайб или жми кнопку Дропа, когда наступит 00:00! 👇",
        reply_markup=mood_keyboard
    )

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
    print("Идеальный VIPERR-бот успешно запущен через Cloudflare!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
