class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    def sell_drink_to_customer(self, drink_name, customer):
        drink = self.find_drink_by_name(drink_name)
        if drink != None:
            customer.reduce_wallet(drink.price)
            self.increase_till(drink.price)

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def check_drunkness(self, customer):
        if customer.age > 40:
            return True
        else:
            return False