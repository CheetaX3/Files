import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import telebot
from telebot import types

# Константы
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "users.json")
TIME_FORMAT = "%H:%M:%S %d-%m-%Y"
MAX_SLEEP_HOURS = 24
STATS_RECORDS_COUNT = 5
DEFAULT_TIMEZONE = 0
MIN_TIMEZONE = -12
MAX_TIMEZONE = 14
MIN_QUALITY = 1
MAX_QUALITY = 10

# Загрузка конфигурации
load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

# Временное хранилище данных
users_data = {}
users_timezone = {}

def get_current_time(user_id):
    """Возвращает текущее время с учетом часового пояса пользователя"""
    return datetime.now() + timedelta(hours=users_timezone.get(user_id, DEFAULT_TIMEZONE))

def validate_input(value, min_val, max_val, error_message):
    """Проверяет ввод пользователя на соответствие диапазону"""
    try:
        num = int(value)
        if min_val <= num <= max_val:
            return num
    except ValueError:
        pass
    return None

def create_keyboard():
    """Создает клавиатуру с основными кнопками"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [
        "😴 Уснул", "🌞 Проснулся", "📊 Оценка",
        "📝 Заметка", "➕ Запись", "📈 Статистика",
        "⏱ Час. пояс"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    return markup

def load_user_data():
    """Загружает данные пользователей из файла"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_user_data(data):
    """Сохраняет данные пользователей в файл"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@bot.message_handler(commands=["start"])
def start(message):
    """Обработчик команды /start"""
    user_id = str(message.from_user.id)
    
    # Очистка предыдущих данных пользователя при старте
    data = load_user_data()
    if user_id in data:
        del data[user_id]
        save_user_data(data)
    
    # Инициализация временных данных
    users_data[message.from_user.id] = {}
    users_timezone[message.from_user.id] = DEFAULT_TIMEZONE
    
    # Отправка приветственного сообщения
    welcome_text = """
Привет!
Я буду помогать тебе отслеживать параметры сна!

Используй кнопки:
😴 Уснул - время начала сна
🌞 Проснулся - время пробуждения
📊 Оценка - оценка качества сна от 1 до 10
📝 Заметка - сохранение заметок
➕ Запись - запись данных в базу
(если указаны начало и окончание сна,

📈 Статистика - за последние пять записей
⏱ Час. пояс: установка часового пояса
(введите отклонение от UTC. по умолчанию MSK)
"""
    bot.send_message(message.chat.id, welcome_text, reply_markup=create_keyboard())

@bot.message_handler(func=lambda msg: msg.text == "⏱ Час. пояс")
def timezone_button(message):
    """Обработчик кнопки часового пояса"""
    bot.send_message(message.chat.id, f"Введите отклонение от UTC от {MIN_TIMEZONE} до {MAX_TIMEZONE} (по умолчанию MSK)")
    bot.register_next_step_handler(message, process_timezone_input)

def process_timezone_input(message):
    """Обрабатывает ввод часового пояса"""
    user_id = message.from_user.id
    timezone = validate_input(
        message.text, 
        MIN_TIMEZONE, 
        MAX_TIMEZONE,
        f"Введите отклонение от UTC от {MIN_TIMEZONE} до {MAX_TIMEZONE}"
    )
    
    if timezone is None:
        bot.send_message(message.chat.id, f"Введите отклонение от UTC от {MIN_TIMEZONE} до {MAX_TIMEZONE}")
        bot.register_next_step_handler(message, process_timezone_input)
        return
    
    users_timezone[user_id] = timezone
    bot.send_message(message.chat.id, "Часовой пояс обновлен!")

@bot.message_handler(func=lambda msg: msg.text == "😴 Уснул")
def sleep_button(message):
    """Обработчик кнопки начала сна"""
    user_id = message.from_user.id
    now_str = get_current_time(user_id).strftime(TIME_FORMAT)
    users_data[user_id] = {"start_time": now_str}
    bot.send_message(message.chat.id, "Время сна записано!")

@bot.message_handler(func=lambda msg: msg.text == "🌞 Проснулся")
def wake_button(message):
    """Обработчик кнопки пробуждения"""
    user_id = message.from_user.id
    now = get_current_time(user_id)
    now_str = now.strftime(TIME_FORMAT)
    
    try:
        start_time = datetime.strptime(users_data[user_id]["start_time"], TIME_FORMAT)
    except KeyError:
        bot.send_message(message.chat.id, "Сначала нажмите кнопку '😴 Уснул'")
        return

    delta = now - start_time
    hours = delta.total_seconds() / 3600
    
    if hours < MAX_SLEEP_HOURS:
        users_data[user_id].update({
            "stop_time": now_str,
            "duration": hours
        })
        bot.send_message(message.chat.id, "Время пробуждения записано!")
        bot.send_message(message.chat.id, "Нажмите кнопку 📊 Оценка и проставьте оцену, а также нажмите кнопку 📝 Заметка и введите комментарий")
    else:
        bot.send_message(message.chat.id, "Навряд ли вы спите более 24 часов 😉")

@bot.message_handler(func=lambda msg: msg.text == "📊 Оценка")
def quality_button(message):
    """Обработчик кнопки оценки сна"""
    bot.send_message(message.chat.id, f"Введите число от {MIN_QUALITY} до {MAX_QUALITY}")
    bot.register_next_step_handler(message, process_quality_input)

def process_quality_input(message):
    """Обрабатывает ввод оценки сна"""
    user_id = message.from_user.id
    quality = validate_input(
        message.text, 
        MIN_QUALITY, 
        MAX_QUALITY,
        f"Введите число от {MIN_QUALITY} до {MAX_QUALITY}"
    )
    
    if quality is None:
        bot.send_message(message.chat.id, f"Введите число от {MIN_QUALITY} до {MAX_QUALITY}")
        bot.register_next_step_handler(message, process_quality_input)
        return
    
    users_data[user_id]["quality"] = quality
    bot.send_message(message.chat.id, "Оценка сохранена!")

@bot.message_handler(func=lambda msg: msg.text == "📝 Заметка")
def note_button(message):
    """Обработчик кнопки заметки"""
    bot.send_message(message.chat.id, "Введите заметку")
    bot.register_next_step_handler(message, process_note_input)

def process_note_input(message):
    """Обрабатывает ввод заметки"""
    user_id = message.from_user.id
    users_data[user_id]["note"] = message.text
    bot.send_message(message.chat.id, "Заметка сохранена!")

@bot.message_handler(func=lambda msg: msg.text == "➕ Запись")
def save_message_to_json(message):
    """Обработчик кнопки сохранения записи"""
    user_id = message.from_user.id
    user_data = users_data.get(user_id, {})
    
    required_fields = ["start_time", "stop_time", "duration", "quality", "note"]
    if not all(key in user_data for key in required_fields):
        bot.send_message(message.chat.id, "Не все данные заполнены. Пожалуйста, укажите время сна, пробуждения, оценку и заметку.")
        return

    data = load_user_data()
    user_id_str = str(user_id)
    
    entry = {
        "start_time": user_data["start_time"],
        "stop_time": user_data["stop_time"],
        "duration": user_data["duration"],
        "quality": user_data["quality"],
        "note": user_data["note"]
    }

    if user_id_str in data:
        data[user_id_str].append(entry)
    else:
        data[user_id_str] = [entry]

    save_user_data(data)
    
    response = f"""
Вы:
- уснули в {user_data['start_time']}
- проснулись в {user_data['stop_time']}
- время сна: {round(user_data['duration'], 2)} часов
- оценка: {user_data['quality']}
- заметка: {user_data['note']}
"""
    bot.send_message(message.chat.id, response)

@bot.message_handler(func=lambda msg: msg.text == "📈 Статистика")
def statistics_button(message):
    """Обработчик кнопки статистики"""
    user_id = str(message.from_user.id)
    data = load_user_data()
    
    if user_id not in data or not data[user_id]:
        bot.send_message(message.chat.id, "Данные отсутствуют!")
        return
    
    user_records = data[user_id][-STATS_RECORDS_COUNT:]
    avg_time = round(sum(record["duration"] for record in user_records) / len(user_records), 2)
    avg_quality = round(sum(record["quality"] for record in user_records) / len(user_records), 2)
    
    stats_message = f"""
Среднее время сна: {avg_time} часов
Средняя оценка: {avg_quality}
"""
    bot.send_message(message.chat.id, stats_message)
    
    for record in user_records:
        bot.send_message(message.chat.id, f"Заметка: {record['note']}")

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)