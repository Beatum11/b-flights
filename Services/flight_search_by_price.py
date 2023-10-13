import requests
from Data.Flight import Flight


def search_by_price(heads, desire_flight, bot, message):

    parameters = {
        "origin": desire_flight.origin_iata,
        "destination": desire_flight.dest_iata,
        "value_min": desire_flight.min_price,
        "value_max": desire_flight.max_price,
        "one_way": "true",
        "limit": 3
    }
    print(parameters)

    try:
        response = requests.get(url="https://api.travelpayouts.com/aviasales/v3/search_by_price_range",
                                params=parameters,
                                headers=heads)
        response.raise_for_status()

        data = response.json()
        first_flight = data["data"][0]
        print(first_flight)

        return Flight(origin=first_flight["origin_name"],
                      destination=first_flight["destination_name"],
                      date_of_departure=first_flight["departure_at"],
                      link=first_flight["link"],
                      price=first_flight["price"])

    except KeyError as e:
        bot.send_message(message.chat.id, "Какая-то ошибка связанная с названием города. Давайте проверим, на всякий случай."
                                          "Можем попробовать заново: /flight_ticket или /start")
    except Exception:
        bot.send_message(message.chat.id, "Не нашел билетов в таком ценовом диапазоне. "
                                          "Можем попробовать заново: /flight_ticket или /start")
