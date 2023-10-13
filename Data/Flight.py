class Flight:

    def __init__(self, origin, destination, date_of_departure,
                 link, price):
        self.origin = origin
        self.destination = destination
        self.date_of_departure = date_of_departure
        self.link = link
        self.price = price

    def show_information(self):
        print(f"Вылет из города: {self.origin}\n"
              f"Прилет в город: {self.destination}\n"
              f"Дата вылета: {self.date_of_departure}\n"
              f"Цена перелета: {self.price} рублей!\n"
              f"Посмотреть на сайте: {self.link}")
