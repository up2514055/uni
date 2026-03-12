class CoffeeShop:
    def __init__(self, limit=5):
        self.customers = []
        self.limit = limit

    def add_customer(self, name):
        if len(self.customers) < self.limit:
            self.customers.append(name)
        else:
            return "Coffee shop is full capacity"

    def remove_customer_at(self, index):
        del self.customers[index]

    def get_customer_at(self, index):
        return self.customers[index]

    def get_num_customers(self):
        return len(self.customers)
    
    def is_full(self):
        if len(self.customers) == self.limit:
            return True
        else:
            return False


def test_coffee_shop():
    shop = CoffeeShop()
    shop.add_customer("Alice")
    shop.add_customer("Bob")
    shop.add_customer("Charlie")
    print(shop.get_num_customers())


if __name__ == "__main__":
    test_coffee_shop()