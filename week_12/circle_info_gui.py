from tkinter import Tk, Frame, Entry, Label, Button, StringVar, IntVar
from circle_info import area_of_circle, circumference_of_circle

class circle:
      
    def __init__(self):
        self.win = Tk()
        self.win.title("Radius in cm:")
        self.win.geometry("400x300")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.radius = IntVar()
        self.area = StringVar()
        self.area.set("Area: 0")
        self.circumference = StringVar()
        self.circumference.set("Circumference: 0")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_num1 = Label(
            self.main_frame,
            text="Radius in cm"
        )
        label_num1.pack()

        entry_num1 = Entry(
            self.main_frame,
            width=20,
            textvariable=self.radius
        )
        entry_num1.pack()

        label_area = Label(
            self.main_frame,
            textvariable=self.area
        )
        label_area.pack()

        label_circumference = Label(
            self.main_frame,
            textvariable=self.circumference
        )
        label_circumference.pack()

        button_calc = Button(
            self.main_frame,
            text="Calculate",
            command=self.calculate
        )
        button_calc.pack(side="left")

        button_close = Button(
            self.main_frame,
            text="Close",
            command=self.win.destroy
        )
        button_close.pack(side="right")

    def calculate(self):
        radius = self.radius.get()
        area = area_of_circle(radius)
        circumference = circumference_of_circle(radius)

        self.area.set(f"Area: {area:.2f}cm^2")
        self.circumference.set(f"Circumference: {circumference:.2f}cm")

def main():
    circ = circle()
    circ.run()

main()