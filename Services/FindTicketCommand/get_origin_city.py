from Data.DesireFlight import DesireFlight


def get_origin(message, bot, get_dest_city):
    desire_flight = DesireFlight()
    print(message.text)
    text = "Выбери город отправления: "
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, get_dest_city, desire_flight)