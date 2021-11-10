import datetime
import telebot
import logging
import re

import create_database as db_creator
from models.database import DATABASE_NAME
from models.database import Session
from models.data import Data
from models.users import Users
from sqlalchemy import and_

from settings import *

session = Session()

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TOKEN)

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

all_time = 'Отримати дані за весь час'
last_day = 'За останній день'
last_week = 'За останній тиждень'
last_month = 'За останній місяць'
last_year = 'За останній рік'


def query_db(n: int):
    pass


@bot.message_handler(commands=['start'])
def start_message(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/help', '/stop')
    user_markup.row(all_time)
    user_markup.row(last_day, last_week)
    user_markup.row(last_month, last_year)
    bot.send_message(message.from_user.id, 'Вітаю, цей бот створений для того, щоб зберігати інформацію про '
                                           'мотогодини.\n '
                                           'Командою /help ви отримаєте більше інструкцій', reply_markup=user_markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Для того, щоб зберігти ваші мотогодини відправте боту їх кількість переведену '
                                      'у хвилини.\n'
                                      'Для того щоб отримати сумарну кількість хвилин скористайтесь меню')


@bot.message_handler(commands=['stop'])
def stop_message(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Сессія завершена, щоб знову відкрити меню введіть /start',
                     reply_markup=hide_markup)


@bot.message_handler(content_types=['text'])
def get_info(message):
    try:
        if len(re.findall(r'[А-я]', message.text)) > 0:
            if message.text == all_time:
                bot.send_message(message.chat.id, 'Сума мотогодин за увесь час складає:')
                # add here query for variable in if
            if message.text == last_day:
                bot.send_message(message.chat.id, 'Сума мотогодин за останній день складає:')
                # add here query for variable in if
            if message.text == last_week:
                bot.send_message(message.chat.id, 'Сума мотогодин за останній тиждень складає:')
                # add here query for variable in if
            if message.text == last_month:
                bot.send_message(message.chat.id, 'Сума мотогодин за останній місяць складає:')
                # add here query for variable in if
            if message.text == last_year:
                bot.send_message(message.chat.id, 'Сума мотогодин за останній рік складає:')
                # add here query for variable in if
        elif len(re.findall(r'[А-я]', message.text)) == 0 and len(re.findall(r'[\d]', message.text)) > 0:
            tg_id = message.from_user.id
            user_firstname = message.from_user.first_name
            user_lastname = message.from_user.last_name
            fdb = session.query(Users.tg_user_id).all()
            fdb = [amount[0] for amount in fdb]
            if tg_id not in fdb:
                incoming_user = Users(tg_id, user_firstname, user_lastname)
                session.add(incoming_user)
            received = datetime.datetime.today().strftime(f"%d-%m-%Y %H:%M:%S")
            incoming_data = Data(tg_id, message.text, received)
            session.add(incoming_data)
            bot.send_message(message.from_user.id, 'Ваш запис додано!')
            session.commit()
    except():
        bot.send_message(message.chat.id, "Виникла помилка, спробуйте ще раз")


bot.polling(none_stop=True)
