class Navigo:
    def __init__(self,balance):
        self.balance = float(balance)
        self.distance = 0

    def take_ride(self, cost, ride_distance):
        self.cost = float(cost)
        self.balance -= self.cost
        self.distance += int(ride_distance)

    def __str__(self):
        return f"Your Navigo card has {self.balance} and has travelled {self.distance}"

def test():
    test1 = Navigo(50)
    test1.take_ride(3,10)
    test1.take_ride(2.5,10)
    print(test1)

test()

