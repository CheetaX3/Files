import os
import json
from datetime import timezone, datetime, timedelta
from dotenv import load_dotenv
import telebot
from telebot import types


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "users.json")
MAX_SLEEP_HOURS = 24
STATS_RECORDS_COUNT = 5
DEFAULT_TIMEZONE = 0
MIN_TIMEZONE = -12
MAX_TIMEZONE = 14
MIN_QUALITY = 1
MAX_QUALITY = 10


load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

# временное хранилище для всех пользователей
users_data = {}
users_timezone = {}

@bot.message_handler(commands=["start"])
def start(message):
    user_id = str(message.from_user.id)

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if user_id in data:
            del data[user_id]

            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button1 = types.KeyboardButton("😴 Уснул")
    button2 = types.KeyboardButton("🌞 Проснулся")
    button3 = types.KeyboardButton("📊 Оценка")
    button4 = types.KeyboardButton("📝 Заметка")
    button5 = types.KeyboardButton("➕ Запись")
    button6 = types.KeyboardButton("📈 Статистика")
    button7 = types.KeyboardButton("⏱ Час. пояс")
    markup.add(button1, button2, button3, button4, button5, button6, button7)
    bot.send_message(
        message.chat.id,
        "Привет!\n"
        "Я буду помогать тебе отслеживать параметры сна!\n"
        "\n"
        "Используй кнопки:\n"
        "😴 Уснул - время начала сна\n"
        "🌞 Проснулся - время пробуждения\n"
        "📊 Оценка - оценка качества сна от 1 до 10\n"
        "📝 Заметка - сохранение заметок\n"
        "➕ Запись - запись данных в базу\n"
        "(если указаны начало и окончание сна,\n"
        "\n"
        "📈 Статистика - за последние пять записей\n"
        "⏱ Час. пояс: установка часового пояса\n"
        "(введите отклонение от UTC. по умолчанию MSK)",
        reply_markup=markup
    )
    user_id = message.from_user.id
    users_data[user_id] = {}
    users_timezone[user_id] = DEFAULT_TIMEZONE

@bot.message_handler(func=lambda msg: msg.text == "⏱ Час. пояс")
def timezone_button(message):
    bot.send_message(message.chat.id, "Введите отклонение от UTC от {MIN_TIMEZONE} до {MAX_TIMEZONE} (по умолчанию MSK) (по умолчанию MSK)")
    bot.register_next_step_handler(message, save_user_timezone)

def save_user_timezone(message):
    user_id = message.from_user.id
    try:
        user_timezone = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Введите отклонение от UTC от {MIN_TIMEZONE} до {MAX_TIMEZONE} (по умолчанию MSK)")
        bot.register_next_step_handler(message, save_user_timezone)
        return
    if user_timezone not in range(MIN_TIMEZONE, MAX_TIMEZONE):
        bot.send_message(message.chat.id, "Введите отклонение от UTC от {MIN_TIMEZONE} до {MAX_TIMEZONE} (по умолчанию MSK)")
        bot.register_next_step_handler(message, save_user_timezone)
        return
    users_timezone[user_id] = user_timezone
    bot.send_message(message.chat.id, "Часовой пояс обновлен!")

@bot.message_handler(func=lambda msg: msg.text == "😴 Уснул")
def sleep_button(message):
    user_id = message.from_user.id
    now = datetime.now() + timedelta(hours=users_timezone[user_id])
    now_str = now.strftime("%H:%M:%S %d-%m-%Y")
    users_data[user_id] = {"start_time": now_str}
    bot.send_message(message.chat.id, f"Время сна записано!") 

@bot.message_handler(func=lambda msg: msg.text == "🌞 Проснулся")
def wake_button(message):
    user_id = message.from_user.id
    now = datetime.now() + timedelta(hours=users_timezone[user_id])
    now_str = now.strftime("%H:%M:%S %d-%m-%Y")
    
    try:
        start_time = datetime.strptime(users_data[user_id]["start_time"], "%H:%M:%S %d-%m-%Y")
    except KeyError:
        bot.send_message(message.chat.id, "Сначала нажмите кнопку '😴 Уснул'")
        return

    delta = now - start_time
    hours = delta.total_seconds() / 3600
    if hours < MAX_SLEEP_HOURS:
        users_data[user_id]["stop_time"] = now_str
        users_data[user_id]["duration"] = hours
        bot.send_message(message.chat.id, f"Время пробуждения записано!")
        bot.send_message(message.chat.id, f"Нажмите кнопку 📊 Оценка и проставьте оцену, а также нажмите кнопку 📝 Заметка и введите комментарий")
    else:
        bot.send_message(message.chat.id, "Навряд ли вы спите более 24 часов 😉")

@bot.message_handler(func=lambda msg: msg.text == "📊 Оценка")
def quality_button(message):
    user_id = message.from_user.id 
    try:
        start_time = datetime.strptime(users_data[user_id]["start_time"], "%H:%M:%S %d-%m-%Y")
        stop_time = datetime.strptime(users_data[user_id]["stop_time"], "%H:%M:%S %d-%m-%Y")
    except KeyError:
        bot.send_message(message.chat.id, "Сначала введите данные о сне")
        return
    bot.send_message(message.chat.id, "Введите число от 1 до 10")
    bot.register_next_step_handler(message, save_user_quality)

def save_user_quality(message):
    user_id = message.from_user.id
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Введите число от 1 до 10")
        bot.register_next_step_handler(message, save_user_quality)
        return
    quality = int(message.text)
    if quality not in range(1, 11):
        bot.send_message(message.chat.id, "Введите число от 1 до 10")
        bot.register_next_step_handler(message, save_user_quality)
        return
    users_data[user_id]["quality"] = quality
    bot.send_message(message.chat.id, "Оценка сохранена!")

@bot.message_handler(func=lambda msg: msg.text == "📝 Заметка")
def note_button(message):
    user_id = message.from_user.id 
    try:
        start_time = datetime.strptime(users_data[user_id]["start_time"], "%H:%M:%S %d-%m-%Y")
        stop_time = datetime.strptime(users_data[user_id]["stop_time"], "%H:%M:%S %d-%m-%Y")
    except KeyError:
        bot.send_message(message.chat.id, "Сначала введите данные о сне")
        return
    bot.send_message(message.chat.id, "Введите заметку")
    bot.register_next_step_handler(message, save_user_note)

def save_user_note(message):
    user_id = message.from_user.id
    users_data[user_id]["note"] = message.text
    bot.send_message(message.chat.id, "Заметка сохранена!")

@bot.message_handler(func=lambda msg: msg.text == "➕ Запись")
def save_message_to_json(message):
    user_id = message.from_user.id

    required_fields = ["start_time", "stop_time", "duration", "quality", "note"]
    if not all(key in users_data.get(user_id, {}) for key in required_fields):
        bot.send_message(message.chat.id, "Не все данные заполнены. Пожалуйста, укажите время сна, пробуждения, оценку и заметку.")
        return

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    user_id_str = str(user_id)
    entry = {
        "start_time": users_data[user_id]["start_time"],
        "stop_time": users_data[user_id]["stop_time"],
        "duration": users_data[user_id]["duration"],
        "quality": users_data[user_id]["quality"],
        "note": users_data[user_id]["note"]
    }

    if user_id_str in data:
        data[user_id_str].append(entry)
    else:
        data[user_id_str] = [entry]

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    bot.send_message(message.chat.id, f"""
        Вы 
        - уснули в {users_data[user_id]['start_time']}
        - проснулись в {users_data[user_id]['stop_time']}
        - время сна: {round(users_data[user_id]['duration'], 2)} часов
        - оценка: {round(users_data[user_id]['quality'], 2)}
        - заметка: {users_data[user_id]['note']}
        """)
print(users_data)

@bot.message_handler(func=lambda msg: msg.text == "📈 Статистика")
def statistics_button(message):
    user_id = message.from_user.id
    try:
        start_time = datetime.strptime(users_data[user_id]["start_time"], "%H:%M:%S %d-%m-%Y")
        stop_time = datetime.strptime(users_data[user_id]["stop_time"], "%H:%M:%S %d-%m-%Y")
    except KeyError:
        bot.send_message(message.chat.id, "Сначала введите данные о сне")
        return

    # Загружаем данные, если файл уже существует
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        bot.send_message(message.chat.id, "Данные отсутствуют!")
        return
    
    user_records = data.get(str(user_id), [])
    last_records = user_records[-STATS_RECORDS_COUNT:]
    aver_time = sum(record["duration"] for record in last_records) / len(last_records)
    aver_time = round(aver_time, 2)
    aver_quality = sum(record["quality"] for record in last_records) / len(last_records)
    aver_quality = round(aver_quality, 2)
    bot.send_message(message.chat.id, f"""
        Среднее время сна: {aver_time}
        Средняя оценка: {aver_quality}
        """)
    for record in last_records:
        bot.send_message(message.chat.id, f"Заметка: {record['note']}")

bot.polling(none_stop=True, interval=0)