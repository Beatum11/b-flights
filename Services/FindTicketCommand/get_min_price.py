

def get_min(message, bot, cities, desire_flight, get_max_price):
    try:
        city_code = cities[message.text]
        desire_flight.dest_iata = city_code
        text = "От какой цены отталкиваемся (rub): "
        sent_msg = bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(sent_msg, get_max_price, desire_flight)
    except KeyError:
        bot.send_message(message.chat.id, "Первый раз слышу о таком городе 🤖👾 Прошу прощения.\n"
                                          "Давайте попробуем еще раз: /find_ticket")