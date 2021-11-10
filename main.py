import datetime
import telebot
import sqlite3
import logging
from settings import *

logger = logging.getLogger(__name__)


bot = telebot.TeleBot(TOKEN)

# conn = sqlite3.connect('db/moto_database.db', check_same_thread=False)
# cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вітаю, цей бот створений для того, щоб зберігати інформацію про мотогодини.\n'
                                      'Командою /help ви отримаєте більше інструкцій')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Для того, щоб зберігти ваші мотогодини відправте боту їх кількість переведену '
                                      'у хвилини.\n'
                                      'Для того щоб отримати сумарну кількість хвилин скористайтесь меню')


bot.polling(none_stop=True)
