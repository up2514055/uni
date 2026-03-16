from tkinter import Tk, Frame, Entry, Button, Label, StringVar, messagebox
from backend import SmartPhone

class SmartphoneGUI:
    def __init__(self, smartphone):
        self.smartphone = smartphone
        self.photos_app = smartphone.photos_app
        self.mailbox_app = smartphone.mailbox_app
        self.win = Tk()
        self.win.title("BnL Smartphone")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.storage_capacity_var = StringVar(value = f"{self.smartphone.storage_capacity}GB")
        self.battery_used_var = StringVar(value = f"{self.smartphone.battery}%")
        self.battery_saver_var = StringVar(value = "Disabled")
        self.storage_left_var = StringVar(value = f"{self.smartphone.available_storage()}GB")
        self.number_photos_var = StringVar(value = f"{self.photos_app.num_photos()}")
        self.storage_used_photos_var = StringVar(value = f"{self.photos_app.calculate_storage_used()}")
        self.number_emails_var = StringVar(value = f"{self.mailbox_app.count_emails()}")
        self.storage_used_var = StringVar(value = f"{self.mailbox_app.calculate_storage_used()}")
        self.sender_var = StringVar()
        self.content_var = StringVar()

        self.create_widgets()


    def run(self):
        self.win.mainloop()
    #gui
    def create_widgets(self):

        #BnL Smartphone
        Label(self.main_frame, text="BnL Smartphone").grid(row=0, column=0, columnspan=3, sticky="w")


        Label(self.main_frame, text="Storage Capacity:").grid(row=1, column=0, columnspan=3, sticky="w")
        Label(self.main_frame, textvariable=self.storage_capacity_var).grid(row=1, column=2, columnspan=3, sticky="w")

        Label(self.main_frame, text="Battery:"). grid(row=2, column=0, columnspan=3, sticky="w")
        Label(self.main_frame, textvariable=self.battery_used_var).grid(row=2, column=2,columnspan=3, sticky="w")

        Label(self.main_frame, text="Battery Saver Mode:").grid(row=3, column = 0, columnspan=3, sticky="w")
        Label(self.main_frame, textvariable=self.battery_saver_var).grid(row=3, column=2, columnspan=5, sticky="w")

        Label(self.main_frame, text="Storage Left:").grid(row=4, column = 0, columnspan=3, sticky="w")
        Label(self.main_frame, textvariable=self.storage_left_var).grid(row=4, column=2, columnspan=3, sticky="w")

        #toggle battery savers and charge battery buttons

        Button(self.main_frame, text="Toggle Battery Saver", command=self.change_battery_mode).grid(row=5, column=0, pady=5, sticky="w")
        Button(self.main_frame, text="Charge Battery", command=self.charge_battery).grid(row=5, column=1, pady=5, sticky="we")

        #Photos app
        Label(self.main_frame, text="Photos App").grid(row=6, column=0, columnspan=3, sticky="w")

        Label(self.main_frame, text="Number of Photos:").grid(row=7, column = 0, columnspan=3, sticky="w")
        Label(self.main_frame, textvariable=self.number_photos_var).grid(row=7, column=1, columnspan=1, sticky="w")

        Label(self.main_frame, text="Storage Used:").grid(row=8, column = 0, columnspan=3, sticky="w")
        Label(self.main_frame, textvariable=self.storage_used_photos_var).grid(row=8, column=1, columnspan=3, sticky="w")

        Button(self.main_frame, text="Take Photo", command=self.take_photo).grid(row=9, column=0, pady=5, sticky="w")
        Button(self.main_frame, text="Delete Photo", command=self.delete_photo).grid(row=9, column=1, pady=5, sticky="e")

        #Mailbox App
        Label(self.main_frame, text="Mailbox App").grid(row=10, column=0, columnspan=3, sticky="w")     
        Label(self.main_frame, text="Number of Emails:").grid(row=11, column = 0, columnspan=3, sticky="w")
        Label(self.main_frame, textvariable=self.number_emails_var).grid(row=11, column=2, sticky="w")

        Label(self.main_frame, text="Storage Used:").grid(row=12, column = 0, columnspan=3, sticky="w")
        Label(self.main_frame, textvariable=self.storage_used_var).grid(row=12, column=2, sticky="w")
        
        #entry boxes for emails
        Entry(self.main_frame, textvariable=self.sender_var, width=20).grid(row=13, column=0, columnspan=2, sticky="w")
        self.sender_var.set("Write the sender here")

        Entry(self.main_frame, textvariable=self.content_var, width=20).grid(row=13, column=2, columnspan=2, sticky="w")
        self.content_var.set("Write the content here")

        Button(self.main_frame, text="Receive Email", command=self.receive_email).grid(row=15, column=0, pady=5, sticky="w")


    def charge_battery(self):
        battery = self.smartphone.charge_battery()
        self.battery_used_var.set(value=f"{battery}%")

    def change_battery_mode(self):
        try:
            battery_mode = self.smartphone.change_battery_mode()
            if battery_mode:

                self.battery_saver_var.set(value="Enabled")

            else:
                self.battery_saver_var.set(value="Disabled")
            self.battery_used_var.set(f"{self.smartphone.battery}%")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def take_photo(self):
        try:
            self.smartphone.take_photo()
            self.battery_used_var.set(f"{self.smartphone.battery}%")
            self.number_photos_var.set(str(self.smartphone.photos_app.num_photos()))
            self.storage_used_photos_var.set(f"{self.smartphone.photos_app.calculate_storage_used():.2f}GB")
            self.storage_left_var.set(f"{self.smartphone.available_storage():.2f}GB")

        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def delete_photo(self):
        try:
            self.smartphone.delete_photo()
            self.battery_used_var.set(f"{self.smartphone.battery}%")
            self.number_photos_var.set(str(self.smartphone.photos_app.num_photos()))
            self.storage_used_photos_var.set(f"{self.smartphone.photos_app.calculate_storage_used():.2f}GB")
            self.storage_left_var.set(f"{self.smartphone.available_storage():.2f}GB")
            #creates an error message box to show that if there are no photos available to delete it will bring up the error message

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def receive_email(self):
        try:
            sender = self.sender_var.get()
            content = self.content_var.get()
            self.smartphone.receive_email(sender, content)

            self.battery_used_var.set(f"{self.smartphone.battery}%")
            self.number_emails_var.set(
            str(self.smartphone.mailbox_app.count_emails()))
            self.storage_used_var.set(
            f"{self.smartphone.mailbox_app.calculate_storage_used():.4f}GB")
            self.storage_left_var.set(
            f"{self.smartphone.available_storage():.2f}GB")

        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    smartphone = SmartPhone(512)
    app = SmartphoneGUI(smartphone)
    app.run()


if __name__ == "__main__":
    main()