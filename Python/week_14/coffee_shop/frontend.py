from tkinter import Tk, Frame, Entry, Button, Label, StringVar
from backend import CoffeeShop


class CoffeeShopApp:

    def __init__(self, coffee_shop):
        self.coffee_shop = coffee_shop

        self.win = Tk()
        self.win.title("Coffee Shop")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        self.new_customer_name = StringVar()

        self.customer_widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_customer_widgets()

        customer_entry = Entry(
            self.main_frame,
            textvariable=self.new_customer_name
        )
        customer_entry.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )

        add_customer_button = Button(
            self.main_frame,
            text="Add",
            command=self.add_customer
        )
        add_customer_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )

        num_customers = self.coffee_shop.get_num_customers()
        i = 0
        while i < num_customers: 
            # Supplied code was <= therefore when i = length of list it is 1 higher 
            # than the index therefore IndexError gets thrown at 3 
            # which is the length as index goes 0-2
            customer = self.coffee_shop.get_customer_at(i)
            customer_label = Label(
                self.main_frame,
                text=customer
            )
            customer_label.grid(
                row=i+1,
                column=0,
                padx=5,
                pady=5,
            )
            self.customer_widgets.append(customer_label)

            remove_customer_button = Button(
                self.main_frame,
                text="Remove",
                command=lambda: self.remove_customer(i)
            )
            remove_customer_button.grid(
                row=i+1,
                column=1,
                padx=5,
                pady=5,
            )
            self.customer_widgets.append(remove_customer_button)
            i = i + 1

    def add_customer(self):
        name = self.new_customer_name.get()
        self.coffee_shop.add_customer(name)
        self.create_widgets()
        self.new_customer_name.set("")

    def remove_customer(self, index):
        self.coffee_shop.remove_customer_at(index)
        self.create_widgets()

    def delete_customer_widgets(self):
        for widget in self.customer_widgets:
            widget.destroy()


def main():
    coffee_shop = CoffeeShop()

    coffee_shop.add_customer("Alice")
    coffee_shop.add_customer("Bob")
    coffee_shop.add_customer("Charlie")

    app = CoffeeShopApp(coffee_shop)
    app.run()


main()