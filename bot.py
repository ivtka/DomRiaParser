from typing import Any, Dict
import config
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup

from domria import DomRia, UserData

bot = TeleBot(config.TOKEN)
parser = DomRia()

user_dict: Dict[Any, UserData] = {}

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    markup.add(*list(config.CITIES.keys()))
    msg = bot.reply_to(message, "Вітаю, {0.first_name}. Я - {1.first_name}, знайду вам квартиру!\nДля початку оберіть місто".format(
        message.from_user, bot.get_me()), reply_markup=markup)
    bot.register_next_step_handler(msg, process_city_step)


def process_city_step(message):
    try:
        chat_id = message.chat.id
        name = message.from_user.first_name
        user = UserData(name)
        user_dict[chat_id] = user
        city = message.text
        user.city = city
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True, resize_keyboard=True)
        markup.add(*config.CITIES[city])
        msg = bot.reply_to(
            message, 'Оберіть район', reply_markup=markup)
        bot.register_next_step_handler(msg, process_state_step)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Щось пішло не так. Натисність /start або /help, щоб перезапустити')


def process_state_step(message):
    try:
        chat_id = message.chat.id
        state = message.text
        user = user_dict[chat_id]
        user.state = state
        msg = bot.reply_to(message, 'Введіть ціну (<стартова>-<кінцева>')
        bot.register_next_step_handler(msg, process_prices_step)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Щось пішло не так. Натисність /start або /help, щоб перезапустити')


def process_prices_step(message):
    try:
        chat_id = message.chat.id
        prices = message.text.split('-')
        if not prices[0].isdigit() or not prices[1].isdigit():
            msg = bot.reply_to(message, "Ціну введено неправильно. Введіть ціну (<стартова>-<кінцева>")
            bot.register_next_step_handler(msg, process_prices_step)
            return
        user = user_dict[chat_id]
        user.start_price = prices[0]
        user.end_price = prices[1]

        result = parser.report(user)
        
        text =  "Ось що я найшов: \n"
        for item in result:
            text += "{}\n{}\n{}\n\n".format(item[0], item[1], item[2])
        for x in range(0, len(text), 4096):
            bot.send_message(chat_id, text[x:x+4096])
    except Exception as e:
        print(e)
        bot.reply_to(message, "За вашим запитом нічого не знайдено. Натисність /start або /help, щоб перезапустити")

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.infinity_polling()