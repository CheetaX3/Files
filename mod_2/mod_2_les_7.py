import telebot
import wikipedia
from telebot import types

bot = telebot.TeleBot('8167516573:AAH7Eb-bIW6phOlMK9wogt6NeIYQ1e3aNQo')
wikipedia.set_lang('ru')

@bot.message_handler(commands=['start'])
def start(message):   
    text = (
        'Введите краткое название интересующей вас статьи на русском языке, '
        'чтобы получить информацию о ней из википедии. \n'
        'Приятного пользования!'
    )
    # Удаление предыдущих кнопок
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        summary = wikipedia.summary(message.text, sentences=5)
        bot.reply_to(message, summary)
    except wikipedia.exceptions.DisambiguationError as e:
        bot.reply_to(message, f'Слишком много значений. Уточните запрос.\nПримеры: {e.options[:2]}')
    except wikipedia.exceptions.PageError:
        bot.reply_to(message, 'Статья не найдена.')
    except Exception as e:
        bot.reply_to(message, f'Ой, произошла ошибка! Обязательно разберемся!')
        # Прописать код для отладки в лог-файл
        # bot.reply_to(message, f'Ошибка: {str(e)}') 

bot.polling(none_stop=True, interval=0)