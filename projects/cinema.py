class CinemaTicket:

    max_price = 20

    def __init__(self, customer_name, film_title, price):
        self.customer_name = customer_name
        self.film_title = film_title
        self._price = float(price)   # ✅ uses setter

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 0 <= new_price <= CinemaTicket.max_price:
            self._price = new_price
        return self._price

    def apply_discount(self, percent):
        self.price = self.price * (1 - percent / 100)

    def change_film(self, new_title):
        self.film_title = new_title

    def __str__(self):
        return f"{self.customer_name} - {self.film_title} - £{self.price:.2f}"


def test_cinema_ticket():
    ticket1 = CinemaTicket("Mustadah", "Avatar", 18)
    ticket2 = CinemaTicket("Ali", "Batman", 15)

    ticket1.apply_discount(20)
    ticket2.change_film("Inception")

    print(ticket1)
    print(ticket2)

    ticket1.price = 3
    print(ticket1)


test_cinema_ticket()
