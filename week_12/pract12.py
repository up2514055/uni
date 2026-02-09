from tkinter import Tk, Frame, Label, Entry, Button, StringVar
import math


class CircleInfoGUI:
    def __init__(self):
        self.win = Tk()
        self.win.title("Circle Info")
        self.win.geometry("300x180")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0, padx=10, pady=10)

        # Variables
        self.radius = StringVar()
        self.area_result = StringVar()
        self.circ_result = StringVar()

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):

        # Radius label + entry
        Label(self.main_frame, text="Radius (cm):").grid(column=0, row=0, sticky="w")

        Entry(self.main_frame, textvariable=self.radius, width=20).grid(column=1, row=0)

        # Button
        Button(self.main_frame, text="Calculate", command=self.calculate).grid(
            column=0, row=1, columnspan=2, pady=10
        )

        # Output labels
        Label(self.main_frame, textvariable=self.area_result).grid(
            column=0, row=2, columnspan=2, sticky="w"
        )

        Label(self.main_frame, textvariable=self.circ_result).grid(
            column=0, row=3, columnspan=2, sticky="w"
        )

    def area_of_circle(self, radius):
        self.radius = radius
        return math.pi * radius ** 2

    def circumference_of_circle(self, radius):
        self.radius = radius
        return 2 * math.pi * radius

    def calculate(self):
        try:
            r = float(self.radius.get())

            area = self.area_of_circle(r)
            circumference = self.circumference_of_circle(r)

            self.area_result.set(f"Area: {area:.2f} cm²")
            self.circ_result.set(f"Circumference: {circumference:.2f} cm")

        except ValueError:
            self.area_result.set("Please enter a valid number.")
            self.circ_result.set("")


if __name__ == "__main__":
    app = CircleInfoGUI()
    app.run()
