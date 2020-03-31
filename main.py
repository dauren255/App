import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1138212334:AAHKS3wFoMNu-CcBzKfZVxI94PYhwWiBi5Y')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_Keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Во всем мире")
    btn2 = types.KeyboardButton("Казахстан")
    btn3 = types.KeyboardButton("США")
    btn4 = types.KeyboardButton("Россия")
    btn5 = types.KeyboardButton("Украина")
    btn6 = types.KeyboardButton("Британия")
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)



    send_mess = f"<b>Hello {message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "казахстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "британия":
        location = covid19.getLocationByCountryCode("UK")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру: </u>\n" \
                        f"<b>Заболевшие: </b>{location['confirmed']}\n" \
                        f"<b>Умершие: </b>{location['deaths']}"
    if final_message == "":
        date = location[0]['last_updated'].split('T')
        time = date[1].split(".")
        final_message = f"<u>Данные по стране: </u>\n" \
                        f"Населения: {location[0]['country_population']}\n" \
                        f"Последние обновления: {date[0]} {time[0]}\n" \
                        f"Последние данные\n" \
                        f"<b>Заболевшие:</b> {location[0]['latest']['confirmed']}\n" \
                        f"<b>Умершие:</b> {location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')
bot.polling(none_stop=True)