class CoffeeShop:

    def __init__(self):
        self.customers = []

    def add_customer(self, name):
        self.customers.append(name)

    def remove_customer_at(self, index=0):
        del self.customers[index]

    def get_customer_at(self, index):
        return self.customers[index]

    def get_num_customers(self):
        return len(self.customers)