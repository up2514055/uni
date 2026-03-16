from tkinter import Tk, Frame, Entry, StringVar, Button, Label
from backend import CoffeeShop


class CoffeeShopApp:
    def __init__(self, coffee_shop):
        self.coffee_shop = coffee_shop
        self.root = Tk()
        self.root.title("Coffee Shop")

        self.main_frame = Frame(self.root)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )
        self.new_customer_name = StringVar()

    def create_widgets(self):
        customer_entry = Entry(self.main_frame, textvariable=self.new_customer_name)
        customer_entry.grid(
            row=0,
            column=0,
        )
        add_customer_button = Button(
            self.main_frame, text="Add", command=self.add_customer
        )
        add_customer_button.grid(row=0, column=1)
        #if full it will disable the button
        if self.coffee_shop.is_full():
            add_customer_button.config(state="disabled")



        count = self.coffee_shop.get_num_customers()
        for i in range(count):
            customer = self.coffee_shop.get_customer_at(i)
            customer_label = Label(self.main_frame, text=customer)
            customer_label.grid(row=i + 1, column=0, padx=5, pady=5)

    def add_customer(self):
        name = self.new_customer_name.get()
        self.coffee_shop.add_customer(name)
        self.create_widgets()

    def run(self):
        self.create_widgets()
        self.root.mainloop()


def main():
    coffee_shop = CoffeeShop()

    coffee_shop.add_customer("Tatenda")
    coffee_shop.add_customer("Fahad")
    coffee_shop.add_customer("Xinran")

    app = CoffeeShopApp(coffee_shop)
    app.run()


main()