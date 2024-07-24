import uuid
import hashlib
from telebot import *
import config
from random import * 
import datetime

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])

def wellcum(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЯ - <b>бот приемки грека.</b> Напиши соообщение, которое хочешь передать греку.'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup = markup)

@bot.message_handler(content_types=['text'])

def lalala(message):
    if message.chat.type == 'private':
        bot.copy_message(
        chat_id=config.TO_CHAT_ID,  
        from_chat_id=message.chat.id,  
        message_id=message.message_id)

bot.polling(none_stop=True)