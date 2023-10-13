#Here we can grab information about DESTINATION


def get_dest(message, bot, cities, desire_flight, get_min_price):
    try:
        city_code = cities[message.text]
        desire_flight.origin_iata = city_code
        text = "Выбери город прибытия: "
        sent_msg = bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(sent_msg, get_min_price, desire_flight)
    except KeyError:
        bot.send_message(message.chat.id, "Первый раз слышу о таком городе 🤖👾 Прошу прощения.\n"
                                          "Давайте попробуем еще раз: /find_ticket")