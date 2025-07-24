import telebot
import random
from telebot import types

scores = {'pc_count': 0, 'user_count': 0}

bot = telebot.TeleBot('8167516573:AAH7Eb-bIW6phOlMK9wogt6NeIYQ1e3aNQo')

choices = ['Камень', 'Ножницы', 'Бумага']

WIN_RULES = {
    'Камень': 'Ножницы',
    'Ножницы': 'Бумага',
    'Бумага': 'Камень'
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Камень')
    button2 = types.KeyboardButton('Ножницы')
    button3 = types.KeyboardButton('Бумага')
    button4 = types.KeyboardButton('Начать игру заново')
    markup.add(button1, button2, button3, button4)    
    bot.send_message(message.chat.id, 'Нажми кнопку и начни игру ',  reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Начать игру заново')
def reset_game(message):
    scores['pc_count'] = 0
    scores['user_count'] = 0
    bot.send_message(message.chat.id, 'Игра сброшена. Счёт обнулён.')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    
    user_choice = message.text

    if user_choice not in choices:
        bot.send_message(message.chat.id, 'Пожалуйста, нажми на одну из кнопок: Камень, Ножницы, Бумага')
        return

    pc_choice = random.choice(choices)
    bot.send_message(message.chat.id, pc_choice)

    if pc_choice == user_choice:
        bot.send_message(message.chat.id, 'Ничья!')
    elif WIN_RULES[pc_choice] == user_choice:
        bot.send_message(message.chat.id, 'Вы проиграли!')
        scores['pc_count'] += 1
    else:
        bot.send_message(message.chat.id, 'Вы выиграли!')
        scores['user_count'] += 1
    
    bot.send_message(message.chat.id, f'Компьютер: {scores['pc_count']} Пользователь: {scores['user_count']}')

bot.polling(none_stop=True, interval=0)