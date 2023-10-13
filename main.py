from Services.flight_search_by_price import search_by_price
from Utils.cities_information import get_cities_and_iata
from Services.FindTicketCommand.get_origin_city import get_origin
from Services.FindTicketCommand.get_dest_city import get_dest
from Services.FindTicketCommand.get_min_price import get_min
from Services.FindTicketCommand.get_max_price import get_max
from dotenv import load_dotenv
import os
import telebot as tb

load_dotenv()

AVIASALES_TOKEN = os.environ.get("AVIASALES_KEY")
BOT_TOKEN = os.environ.get("BOT_KEY")


heads = {
    "X-Access-Token": AVIASALES_TOKEN
}

bot = tb.TeleBot(BOT_TOKEN)

cities = get_cities_and_iata()



#Так я могу реагировать на команды
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "<b>Привет!</b> Это b-flights. Здесь ты можешь найти действительно дешевые билеты на любой рейс. Используй <a>/find_ticket</a>, чтобы найти билет, который подходит под твой бюджет."
    img_url = 'https://images.unsplash.com/photo-1605590427165-3884d6aa6731?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZmxpZ2h0JTIwd2luZG93fGVufDB8fDB8fHww&w=1000&q=80'
    bot.send_message(message.chat.id, text, parse_mode="HTML")
    bot.send_photo(message.chat.id, img_url)


@bot.message_handler(commands=['find_ticket'])
def get_origin_city(message):
    get_origin(message, bot, get_dest_city)


def get_dest_city(message, desire_flight):
    get_dest(message, bot, cities, desire_flight, get_min_price)


def get_min_price(message, desire_flight):
    get_min(message, bot, cities, desire_flight, get_max_price)


def get_max_price(message, desire_flight):
    get_max(message, bot, desire_flight, get_ticket)


def get_ticket(message, desire_flight):
    desire_flight.max_price = int(message.text)
    # SEARCH FLIGHT TICKET BY PRICE
    try:
        flight = search_by_price(heads, desire_flight, message, bot)
        if flight:
            text = (f"Из: <b>{flight.origin}</b>\n"
                    f"В: <b>{flight.destination}</b>\n"
                    f"Дата: <b>{flight.date_of_departure}</b>\n"
                    f"Самое главное, какая цена: <b>{flight.price} РУБ.!</b>\n"
                    f"Ссылочка на покупку: <a href='https://aviasales.ru{flight.link}'>Нажми сюда</a>")
            bot.send_message(message.chat.id, text, parse_mode="HTML")
    except Exception as e:
        bot.send_message(message.chat.id, "Что пошло не так в самом конце. Очень жаль."
                                          "Пробуем еще раз? /flight_ticket")


bot.infinity_polling()
