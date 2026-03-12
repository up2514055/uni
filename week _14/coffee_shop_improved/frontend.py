from tkinter import Tk, Frame, Entry, Button, Label, StringVar
from backend import CoffeeShop, CoffeeShopError


class CoffeeShopApp:
    def __init__(self, coffee_shop):
        self.coffee_shop = coffee_shop

        self.win = Tk()
        self.win.title("Coffee Shop Improved")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.new_customer_name = StringVar()

        self.error_text = StringVar(value="")

        self.customer_widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_customer_widgets()

        Entry(self.main_frame, textvariable=self.new_customer_name).grid(row=0, column=0, padx=5, pady=5)
        Button(self.main_frame, text="Add", command=self.add_customer).grid(row=0, column=1, padx=5, pady=5)

        error_label = Label(self.main_frame, textvariable=self.error_text)
        error_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        self.customer_widgets.append(error_label)

        try:
            count = self.coffee_shop.get_num_customers()

            for i in range(count):
                customer = self.coffee_shop.get_customer_at(i)
                customer_label = Label(self.main_frame, text=customer)
                customer_label.grid(row=i + 2, column=0, padx=5, pady=5)
                self.customer_widgets.append(customer_label)

                remove_button = Button(
                    self.main_frame,
                    text="Remove",
                    command=lambda index=i: self.remove_customer(index)
                )
                remove_button.grid(row=i + 2, column=1, padx=5, pady=5)
                self.customer_widgets.append(remove_button)

        except CoffeeShopError as e:
            self.show_error(str(e))

    def add_customer(self):
        name = self.new_customer_name.get()
        try:
            self.coffee_shop.add_customer(name)
            self.new_customer_name.set("")
            self.clear_error()
            self.create_widgets()
        except CoffeeShopError as e:
            self.show_error(str(e))

    def remove_customer(self, index):
        try:
            self.coffee_shop.remove_customer_at(index)
            self.clear_error()
            self.create_widgets()
        except CoffeeShopError as e:
            self.show_error(str(e))

    def show_error(self, message):
        self.error_text.set(f"Error: {message}")

    def clear_error(self):
        self.error_text.set("")

    def delete_all_customer_widgets(self):
        for widget in self.customer_widgets:
            widget.destroy()
        self.customer_widgets = []


def main():
    # test capacity (change as needed)
    coffee_shop = CoffeeShop(max_capacity=3)
    coffee_shop.add_customer("Tatenda")
    coffee_shop.add_customer("Fahad")
    coffee_shop.add_customer("Xinran")

    app = CoffeeShopApp(coffee_shop)
    app.run()


main()