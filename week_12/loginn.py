from tkinter import Tk, Frame, Label, Entry, Button, StringVar
from sign_up import SignUpWindow, load_login_details

class LoginApp:

    def __init__(self):
        self.win = Tk()
        self.win.title("Employee Login")
        self.win.geometry("300x140")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.username = StringVar()
        self.password = StringVar()
        self.message = StringVar()
        self.message.set("Enter username and password.")

        self.login_details = load_login_details()

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        Label(self.main_frame, textvariable=self.message, width=30).grid(column=0, row=0, columnspan=2)

        Label(self.main_frame, text="Username:").grid(column=0, row=1)
        Entry(self.main_frame, width=25, textvariable=self.username).grid(column=1, row=1)

        Label(self.main_frame, text="Password:").grid(column=0, row=2)
        Entry(self.main_frame, width=25, textvariable=self.password, show="*").grid(column=1, row=2)

        Button(self.main_frame, text="Sign In", command=self.authenticate).grid(column=0, row=3)
        Button(self.main_frame, text="Cancel", command=self.win.destroy).grid(column=1, row=3)

        Button(self.main_frame, text="Sign Up", command=self.open_signup).grid(column=0, row=4, columnspan=2, pady=5)

    def refresh_details(self):
        self.login_details = load_login_details()
        self.message.set("Account created. You can log in.")

    def open_signup(self):
        SignUpWindow(self.win, self.refresh_details)

    def authenticate(self):
        username = self.username.get().strip()
        password = self.password.get()

        if username not in self.login_details:
            self.message.set("Username not found.")
        elif self.login_details[username] != password:
            self.message.set("Incorrect password.")
        else:
            self.message.set("Login successful!")


def main():
    app = LoginApp()
    app.run()


if __name__ == "__main__":
    main()
