

def get_max(message, bot, desire_flight, get_ticket):
    desire_flight.min_price = int(message.text)
    text = "Максимально возможная цена (rub): "
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, get_ticket, desire_flight)