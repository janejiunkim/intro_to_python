class CoffeeCup():
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def fill(self):
        self.amount = self.capacity
    
    def empty(self): 
        self.amount = 0

    def drink(self, amount) :
        self.amount -= amount
        if (self.amount == 0):
            self.amount = 0

brad_cup = CoffeeCup(12)
brad_cup.fill()
brad_cup.empty()

class Phone():
    def __init__(self, camera, phone_number):
        self.camera = camera
        self.phone_number = phone_number
        self.smartphone = True

    def call(self, number):
        print(f"{self.phone_number} is calling ... {number}")

    def take_photo(self):
        if (self.camera):
            print("Capture photo")
        else:
            print("Buy a camera")

kasais_phone = Phone(True, 8188775309)

class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees= 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.amount -= amount
        if (self.amount < 0):
            self.overdraft_fees += 20
        return amount

