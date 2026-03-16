from tkinter import Tk, Frame, Label, Entry, Button, IntVar

class Temperature:

    def __init__(self):
        self.win = Tk()
        self.win.title("Converter")
        self.win.geometry("400x150")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.celsius_num = IntVar()
        self.fahrenheit_num = IntVar()

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_celsius = Label(
            self.main_frame,
            text="Celsius"
        )
        label_celsius.pack()

        entry_celsius = Entry(
            self.main_frame,
            width=20,
            textvariable=self.celsius_num
        )
        entry_celsius.pack()

        label_fahrenheit = Label(
            self.main_frame,
            text="Farenheit"
        )
        label_fahrenheit.pack()

        entry_fahrenheit = Entry(
            self.main_frame,
            width=20,
            textvariable=self.fahrenheit_num
        )
        entry_fahrenheit.pack()

        button_tofahrenheit = Button(
            self.main_frame,
            text="Convert To Fahrenheit",
            command=self.celsius_to_fahrenheit
        )
        button_tofahrenheit.pack(side="left")

        button_tocelsius = Button(
            self.main_frame,
            text="Convert To Celsius",
            command=self.fahrenheit_to_celsius
        )
        button_tocelsius.pack(side="left")

        button_close = Button(
            self.main_frame,
            text="Close",
            command=self.win.destroy
        )
        button_close.pack(side="right")

    def celsius_to_fahrenheit(self):
        celsius = self.celsius_num.get()
        fahrenheit = (celsius * (9/5)) + 32

        self.fahrenheit_num.set(f"{fahrenheit:.2f}")

    def fahrenheit_to_celsius(self):
        fahrenheit = self.fahrenheit_num.get()
        celsius = (fahrenheit - 32) * 5/9

        self.celsius_num.set(f"{celsius:.2f}")


def main():
    temp = Temperature()
    temp.run()


main()