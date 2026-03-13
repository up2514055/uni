class PhotosApp:
    def __init__(self):
        self.photos = 0

    def take_photo(self):
        self.photos += 1
        
    def delete_photo(self):
        if self.photos <= 0:
            raise ValueError("No photos to delete")
        self.photos -= 1

    def calculate_storage_used(self):
        #each photo is 24 Megabytes
        used_mb = self.photos * 24
        used_gb = used_mb  / 1024
        return used_gb
    
    def num_photos(self):
        return self.photos

    def __str__(self):
        return f"Photos App - Photos: {self.photos}, Storage Used: {self.calculate_storage_used():.2f}GB"
    
def test_photos_app():
    app = PhotosApp()
    for _ in range(5):
        app.take_photo()
    print(app)
    app.delete_photo()
    app.delete_photo()
    print(app)
#test_photos_app()

class MailboxApp:
    def __init__(self):
        self.emails = {}

    def receive_email(self, sender, content):
        sender = str(sender)
        content = str(content)
    # create a unique email ID by counting existing emails and adding 1,
    # so each new email is stored separately and does not overwrite other emails.
        email_id = str(len(self.emails) + 1)
    # store email in dictionary
        self.emails[email_id] = (sender, content)

    def count_emails(self):
        return len(self.emails)
    
    def calculate_storage_used(self):
        storage_mb = len(self.emails) * 5
        return storage_mb / 1024
    # this converts the value from MB to GB

    def __str__(self):
        return f"Mailbox App - Emails: {self.count_emails()}, Storage Used: {self.calculate_storage_used()}GB"


def test_mailbox_app():
    mailbox = MailboxApp()
    print("Before:")
    print(mailbox)
    mailbox.receive_email("dylan.mazur@gmail.com", "test test")
    mailbox.receive_email("bob@gmail.com", "Coursework is due soon")
    mailbox.receive_email("mustafah@gmail.com", "We have to go gym soon")
    print("After:")
    print(mailbox)

#test_mailbox_app()

class SmartPhone:
    
    def __init__(self, storage_capacity):
        self.storage_capacity = int(storage_capacity)
        self.battery = int(100)
        self.battery_saver_mode = False
        self.photos_app = PhotosApp() 
        self.mailbox_app = MailboxApp()

    def use_battery(self, amount):
        amount = int(amount)

        if amount < 0:
            raise ValueError("Battery usage cannot be negative")
        
        if self.battery <= 0:
            self.battery = 0
            raise RuntimeError("Battery is dead")
        
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0

        return self.battery
        
    def charge_battery(self):
        if not self.battery_saver_mode:
            self.battery = int(100)
        elif self.battery_saver_mode and self.battery <= 80:
            self.battery = int(80)
        return self.battery
        
    def available_storage(self):
        used = self.photos_app.calculate_storage_used() + self.mailbox_app.calculate_storage_used()
        return self.storage_capacity - used
    
    def change_battery_mode(self):
        self.use_battery(2)
        if self.battery_saver_mode:
            self.battery_saver_mode = False
        elif not self.battery_saver_mode:
            self.battery_saver_mode = True
        return self.battery_saver_mode
    
    def __str__(self):

    # convert boolean to string here
        if self.battery_saver_mode:
            saver = "Enabled"
        else:
            saver = "Disabled"

        return f"BnL Smartphone - Storage: {self.storage_capacity}GB, Battery: {self.battery}%, Battery Saver Mode: {saver}"
    

    #GUi need to add - 2% of the battery each time a button is pressed
    def take_photo(self):
        if self.available_storage() < 24 / 1024:
            raise ValueError("Not enough storage to take a photo")
        self.use_battery(2)
        self.photos_app.take_photo()

    def delete_photo(self):
        if self.available_storage() <  5 / 1024:
            raise ValueError("Not enough storage to take a photo")
        self.use_battery(2)
        self.photos_app.delete_photo()

    def receive_email(self, sender, content):
        self.use_battery(2)
        self.mailbox_app.receive_email(sender, content)
    
def test_smartphone():
    phone = SmartPhone(512)
    phone.use_battery(30)
    print(phone)
    phone.battery_saver_mode = True
    phone.charge_battery()
    print(phone)
    
#test_smartphone()