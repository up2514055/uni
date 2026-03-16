class GymMember:


    max_sessions = 20

    def __init__(self, name, membership_type):
        self.membership_type = membership_type
        self.name = name
        self._sessions_remaining = 10

    @property #getter
    def sessions_remaining(self):
        return self._sessions_remaining
    
    @sessions_remaining.setter ##setter must have the same name as the fucntuion in the getter
    def sessions_remaining(self,new_value):
        if 0 <= new_value <= GymMember.max_sessions:
            self._sessions_remaining = new_value
    

    def book_session(self):
        if self.sessions_remaining > 0:
            self._sessions_remaining -= 1

    def add_sessions(self, amount):
        self.sessions_remaining += amount

    def __str__(self):
        return f"{self.name} {self.membership_type} - {self.sessions_remaining} remaining"
    

def test_gym_member():
    num1 = GymMember("james", "gold")
    num2 = GymMember("Shayden", "Silver")
    print(num1)
    print(num2)

    num1.book_session()
    print(num1)
    num2.book_session()
    print(num2)
    num1.add_sessions(2)
    num2.add_sessions(5)
    print(num1)
    print(num2)

test_gym_member()