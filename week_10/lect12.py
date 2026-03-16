from tkinter import Tk, Frame, Label, Entry, Button


class Calculator:

    def __init__(self):
        self.win = Tk() #constructor, root of the application
        self.win.title = ("Calculator")#title
        self.win.geometry = ("200x150")#how big the window is

        self.main_frame = Frame(self.win)#divider bit like a div element in html, have to import this, self.win is the parent, creating the widget
        self.main_frame.pack(padx=10, pady=10) #placing the widget

        my_label = Label(self.main_frame, text="Hi")
        my_label.pack()

    def create_widgets(self):
        label_num1 = Label(self.main_frame, text="Number 1")
        label_num1.pack()

        label_num2 = Label(self.main_frame, text="Number 2")
        label_num2.pack()

        label_result = Label(self.main_frame, text="Result")
        label_result.pack()

        entry_num1 = Entry(self.main_frame, width=20)#num of space to enter the 
        entry_num1.pack()
        
        entry_num2 = Entry(self.main_frame, width=20)
        entry_num2.pack()

        button_mult = Button(self.main_frame, text="Multiply")
        button_mult.pack(side="left")

        button_close = Button(self.main_frame, text="Close")
        button_close.pack(side="right")

    def run(self):
        self.create_widgets()
        self.win.mainloop() #run function, keeps the main loop running

def main(): #test function
    calc = Calculator()
    calc.run()

main()