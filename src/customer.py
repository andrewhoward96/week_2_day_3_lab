class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drinks = []
        self.drunkness = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def drink_count(self):
        return len(self.drinks)

    def add_drink(self, drink):
        self.drinks.append(drink)
        self.increase_drunkness(drink)

    def increase_drunkness(self, drink):
        self.drunkness += drink.alcohol_level