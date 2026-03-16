class Message:
    def __init__(self, text):
        self.text = text
        self.is_pinned = False

class User:

    user_count = 0

    def __init__(self, username):
        self.username = username
        User.user_count += 1
        self.user_id = User.user_count
        
        self.received_messages = []
        self.message_limit = 0

    def receive_message(self, message):
        self.received_messages.append(message)
        return True

    def get_inbox_view(self):
        output = "=" * 40 + "\n"
        output += f"{self.username}'s Inbox (ID: {self.user_id})"
        
        if len(self.received_messages) == 0:
            return output + "\nNo messages."

        for msg in self.received_messages:
            if msg.is_pinned == True:
                output += f"\n[PINNED] {msg.text}"
        
        for msg in self.received_messages:
            if msg.is_pinned == False:
                output += f"\n{msg.text}"
        
        output += "\n" + "=" * 40
                
        return output

class Unverified(User):
    def __init__(self, username):
        super().__init__(username)

    def send_message(self, recipient, text):
        return "Error: Unverified users cannot send messages."

class Verified(User):
    def __init__(self, username):
        super().__init__(username)
        self.message_limit = 100

    def send_message(self, recipient, text):
        if len(text) <= self.message_limit:
            new_msg = Message(text)
            recipient.receive_message(new_msg)
            return "Success: Message sent."
        return "Error: Message too long."

class Nitro(User):
    def __init__(self, username):
        super().__init__(username)

    def send_message(self, recipient, text):
        new_msg = Message(text)
        recipient.receive_message(new_msg)
        return "Success: Nitro message sent."

    def pin_message(self, index):
        if index >= 0 and index < len(self.received_messages):
            self.received_messages[index].is_pinned = True
            return "Success: Message pinned."
        return "Error: Invalid index."
    

def run_tests():
    u1 = Unverified("Newbie_Sam")
    u2 = Verified("Member_Alex")
    u3 = Nitro("Power_User_Zoe")
    print(f"Created: {u1.username} (ID:{u1.user_id}), {u2.username} (ID:{u2.user_id}), {u3.username} (ID:{u3.user_id})")

    # Unverified Tes
    result = u1.send_message(u2, "Hello world")
    print(f"Action: Send Message -> {result}")

    # Verified Test
    msg1 = "This is a short message."
    print(f"Action: Send Valid -> {u2.send_message(u3, msg1)}")
    
    long_msg = "This message is to test long messages. " * 10
    print(f"Action: Send Too Long -> {u2.send_message(u3, long_msg)}")

    # Nitro Test
    print(f"Action: Send Long Message -> {u3.send_message(u1, long_msg)}")
    
    u3.receive_message(Message("First basic message"))
    u3.receive_message(Message("IMPORTANT: PIN THIS ONE"))
    u3.receive_message(Message("Third basic message"))
    
    print(f"Action: Pinning -> {u3.pin_message(1)}")
    print(f"Action: Pinning -> {u3.pin_message(3)}")

    print(u1.get_inbox_view())
    print(u2.get_inbox_view())
    print(u3.get_inbox_view())

# Run the tests
run_tests()