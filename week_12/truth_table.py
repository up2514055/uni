from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar, BooleanVar

class TruthTable:

    def __init__(self):
        self.win = Tk()
        self.win.title("Truth Table")
        self.win.geometry("400x300")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.user_vars = [] 
        self.correct_answers = [False, True, True, True]

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label = Label(self.main_frame,
                       text="Enter 1 for True, 0 for False")
        .grid(row=0, column=0, columnspan=2, pady=10)

        # Row 1
        label_row1 = Label(
            self.main_frame, 
            text="0 OR 0 = "
        )
        label_row1.grid(
            row=1, 
            column=0, 
            sticky="e"
        )

        var1 = BooleanVar()
        self.user_vars.append(var1)

        entry_row1 = Entry(
            self.main_frame, 
            textvariable=var1, 
            width=5
        )
        entry_row1.grid(
            row=1, 
            column=1, 
            sticky="w"
        )

        # Row 2
        label_row2 = Label(
            self.main_frame, 
            text="0 OR 1 = "
        )
        label_row2.grid(
            row=2, 
            column=0, 
            sticky="e"
        )

        var2 = BooleanVar()
        self.user_vars.append(var2)

        entry_row2 = Entry(
            self.main_frame, 
            textvariable=var2, 
            width=5
        )
        entry_row2.grid(
            row=2, 
            column=1, 
            sticky="w"
        )

        # Row 3
        label_row3 = Label(
            self.main_frame, 
            text="1 OR 0 = "
        )
        label_row3.grid(
            row=3, 
            column=0, 
            sticky="e"
        )

        var3 = BooleanVar()
        self.user_vars.append(var3)

        entry_row3 = Entry(
            self.main_frame, 
            textvariable=var3, 
            width=5
        )
        entry_row3.grid(
            row=3, 
            column=1, 
            sticky="w"
        )

        # Row 4
        label_row4 = Label(
            self.main_frame, 
            text="1 OR 1 = "
        )
        label_row4.grid(
            row=4, 
            column=0, 
            sticky="e"
        )

        var4 = BooleanVar()
        self.user_vars.append(var4)

        entry_row4 = Entry(
            self.main_frame, 
            textvariable=var4, 
            width=5
        )
        entry_row4.grid(
            row=4, 
            column=1, 
            sticky="w"
        )

        check_score = Button(
            self.main_frame, 
            text="Check Score", 
            command=self.check_score
        )
        check_score.grid(
            row=5, 
            column=0, 
            columnspan=2, 
            pady=15
        )

        self.label_result = Label(
            self.main_frame, 
            text="Score: "
        )
        self.label_result.grid(
            row=6, 
            column=0, 
            columnspan=2
        )

    def check_score(self):
        score = 0
        for i in range(4):
            if self.user_vars[i].get() == self.correct_answers[i]:
                score += 1
        
        percent = (score / 4) * 100
        self.label_result.config(text=f"Score: {percent:.0f}%")


def main():
    table = TruthTable()
    table.run()

main()