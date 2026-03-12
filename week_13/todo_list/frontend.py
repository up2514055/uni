from tkinter import Tk, Frame, Entry, StringVar, Button, Label, Toplevel
from backend import TaskList

class ToDoApp:
    def __init__(self, tasklist):
        self.tasklist = tasklist

        self.root = Tk()
        self.root.title("Todo List App")

        self.main_frame = Frame(self.root)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)

        self.new_task = StringVar()

        #stores the widgets
        self.task_widgets = []

    def run(self):
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.delete_all_task_widgets()

        num_tasks = self.tasklist.get_num_tasks()

        for i in range(num_tasks):
            msg = self.tasklist.get_task_message_by_index(i)

            task_label = Label(self.main_frame, text=msg, anchor="w")
            task_label.grid(row=i, column=0, sticky="w", padx=(0, 30), pady=8)
            self.task_widgets.append(task_label)

            edit_button = Button(
                self.main_frame,
                text="Edit",
                width=8,
                command=lambda index=i: self.open_edit_window(index)
            )
            edit_button.grid(row=i, column=1, padx=10, pady=8)
            self.task_widgets.append(edit_button)

            delete_button = Button(
                self.main_frame,
                text="Delete",
                width=8,
                command=lambda index=i: self.delete_task(index)
            )
            delete_button.grid(row=i, column=2, padx=10, pady=8)
            self.task_widgets.append(delete_button)

        bottom_row = num_tasks

        task_entry = Entry(self.main_frame, textvariable=self.new_task, width=35)
        task_entry.grid(row=bottom_row, column=0, sticky="w", pady=(15, 0))
        self.task_widgets.append(task_entry)

        add_button = Button(
            self.main_frame,
            text="Add",
            width=8,
            command=self.add_task_clicked
        )
        add_button.grid(row=bottom_row, column=1, padx=10, pady=(15, 0), sticky="w")
        self.task_widgets.append(add_button)

    def add_task_clicked(self):
        msg = self.new_task.get().strip()
        if not msg:
            return

        self.tasklist.create_new_task(msg)
        self.new_task.set("")
        self.create_widgets()

    def delete_task(self, index):
        self.tasklist.remove_task_at_index(index)
        self.create_widgets()

    def open_edit_window(self, index):
        edit_win = Toplevel(self.root)
        edit_win.title("Edit Task")

        edit_var = StringVar()
        edit_var.set(self.tasklist.get_task_message_by_index(index))

        entry = Entry(edit_win, textvariable=edit_var, width=35)
        entry.grid(row=0, column=0, padx=15, pady=15)

        confirm_button = Button(
            edit_win,
            text="Confirm",
            width=10,
            command=lambda: self.confirm_edit(index, edit_var, edit_win)
        )
        confirm_button.grid(row=0, column=1, padx=(0, 15), pady=15)

    def confirm_edit(self, index, edit_var, edit_win):
        self.tasklist.set_task_message_at_index(index, edit_var.get().strip())
        edit_win.destroy()
        self.create_widgets()

    def delete_all_task_widgets(self):
        for w in self.task_widgets:
            w.destroy()
        self.task_widgets = []


if __name__ == "__main__":
    tasks = TaskList()
    app = ToDoApp(tasks)
    app.run()