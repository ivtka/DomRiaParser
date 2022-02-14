from email import message
import telebot
import config
from telebot import types
from domria import DomRia

bot = telebot.TeleBot(config.TOKEN)
parser = DomRia()
parser.load_page()

CITIES = {'Чернівці': ['Квартал Вілл', 'Ніжин', 'Першотравневий',
                       'Садгорський', 'Шевченківський'], 'Івано-Франківськ': ['Івасюка Надрічна', 'Арсенал', 'Бам']}


g

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     cities = []
#     for city in CITIES.keys():
#         item = types.KeyboardButton(city)
#         cities.append(item)
#     markup.add(*cities)
#     bot.send_message(
#         message.chat.id, "Вітаю, {0.first_name}. Я - <b>{1.first_name}</b>, знайду вам квартиру!\nОберіть місто".format(
#             message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


# def get_keybord_buttons(city: str) -> types.ReplyKeyboardMarkup:
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     states = []
#     for state in CITIES[city]:
#         item = types.KeyboardButton(state)
#         states.append(item)
#     markup.add(*states)
#     return markup


# @bot.message_handler(content_types=['text'])
# def choose_state(message):
#     parser.select_city(message.text)
#     markup = get_keybord_buttons(message.text)
#     bot.send_message(message.chat.id, "Який район?", reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def choose_price(message):
#     parser.select_state(message.text)
#     bot.send_message("Введіть ціну: (стартова-кінцева у $)")


# def report(message):
#     prices = message.text.split('-')
#     parser.select_price(start_price=prices[0], end_price=prices[1])


bot.polling(none_stop=True)
