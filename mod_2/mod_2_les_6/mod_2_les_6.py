import telebot
from telebot import types
import random
import os
import glob

TOKEN = '8167516573:AAH7Eb-bIW6phOlMK9wogt6NeIYQ1e3aNQo'
bot = telebot.TeleBot(TOKEN)
# Путь к папке с картинками
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER = os.path.join(BASE_DIR, 'mems')

# Получить список файлов с расширением .jpg в папке
image_files = glob.glob(os.path.join(IMAGE_FOLDER, '*.jpg'))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Mem')
    markup.add(button1)
    bot.send_message(message.chat.id, 'Нажми кнопку и получи мем',  reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    
    if not message.text == 'Mem':
        bot.reply_to(message, 'Чтобы получить мем нажмите кнопку')
        return

    if not image_files:  
        return bot.reply_to(message, 'За новыми мемами приходите завтра :)')

    with open(random.choice(image_files), 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
        image_files.remove(photo.name)
           
bot.polling(none_stop=True)