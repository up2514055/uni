from tkinter import Tk, Frame, Entry, Label, Button, IntVar, StringVar

class ToDoToday:

    def __init__(self):
        self.win = Tk()
        self.win.title("What To Do Today")
        self.win.geometry("300x150")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.temperature = IntVar()
        self.result = StringVar()
        self.result.set("What To Do Today:")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_temp = Label(
            self.main_frame,
            text="Temperature"
        )
        label_temp.pack()

        entry_temp = Entry(
            self.main_frame,
            width=20,
            textvariable=self.temperature
        )
        entry_temp.pack()

        label_result = Label(
            self.main_frame,
            textvariable=self.result
        )
        label_result.pack()

        button_todo_today = Button(
            self.main_frame,
            text="What To Do Today",
            command=self.what_to_do_today
        )
        button_todo_today.pack(side="left")

        button_close = Button(
            self.main_frame,
            text="Close",
            command=self.win.destroy
        )
        button_close.pack(side="right")

    def what_to_do_today(self):
        temperature = self.temperature.get()

        if temperature > 25:
            self.result.set("A swim would be a good idea")
        elif temperature <= 25 and temperature >= 10:
            self.result.set("Shopping in gunwarf quays is a good idea")
        else:
            self.result.set("Its best to stay home and watch a film")


def main():
    today = ToDoToday()
    today.run()


main()