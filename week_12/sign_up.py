from tkinter import Toplevel, Frame, Label, Entry, Button, StringVar
import csv
import os

CSV_FILE = "login_details.csv"


def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password"])


def load_login_details():
    ensure_csv()
    details = {}
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            details[row["username"]] = row["password"]
    return details


def append_login(username, password):
    ensure_csv()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])


def valid_password(pw):
    if len(pw) < 5:
        return False, "Password must be at least 5 characters."
    if not any(ch.isalpha() for ch in pw) or not any(ch.isdigit() for ch in pw):
        return False, "Password must contain a letter and a number."
    return True, ""


class SignUpWindow:
    def __init__(self, parent, on_close):
        self.on_close = on_close

        self.win = Toplevel(parent)
        self.win.title("Sign Up")
        self.win.geometry("320x160")

        frame = Frame(self.win)
        frame.grid(padx=10, pady=10)

        self.message = StringVar(value="Create a new account.")
        Label(frame, textvariable=self.message).grid(column=0, row=0, columnspan=2, sticky="w")

        self.username = StringVar()
        self.password = StringVar()

        Label(frame, text="Username:").grid(column=0, row=1, sticky="w")
        Entry(frame, textvariable=self.username, width=22).grid(column=1, row=1)

        Label(frame, text="Password:").grid(column=0, row=2, sticky="w")
        Entry(frame, textvariable=self.password, width=22, show="*").grid(column=1, row=2)

        Button(frame, text="Create", command=self.create).grid(column=0, row=3, pady=10, sticky="w")
        Button(frame, text="Cancel", command=self.win.destroy).grid(column=1, row=3, pady=10, sticky="e")

    def create(self):
        u = self.username.get().strip()
        p = self.password.get()

        if u == "":
            self.message.set("Username cannot be empty.")
            return

        details = load_login_details()
        if u in details:
            self.message.set("Username already exists.")
            return

        ok, msg = valid_password(p)
        if not ok:
            self.message.set(msg)
            return

        append_login(u, p)
        self.win.destroy()
        self.on_close()  # tell login window to reload CSV
