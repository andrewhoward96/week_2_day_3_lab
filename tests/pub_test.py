import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("Vodka", 3.00, 10)
        self.drink_2 = Drink("Whiskey", 6.50, 15)
        self.drink_3 = Drink("Beer", 3.70, 5)

        drinks = [self.drink_1, self.drink_2, self.drink_3]
        self.pub = Pub("The Prancing Pony", 100.00, drinks)
        

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_can_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("Whiskey")
        self.assertEqual("Whiskey", drink.name)

    def test_can_sell_drink_to_customer(self):
        customer = Customer("Bob", 50.00, 30)
        self.pub.sell_drink_to_customer("Whiskey", customer)
        self.assertEqual(43.50, customer.wallet)
        self.assertEqual(106.50, self.pub.till)

    def test_check_age(self):
        customer = Customer("Bob", 50.00, 30)
        self.pub.check_age(customer)
        self.assertEqual(30, customer.age)

    def test_check_drunkness(self):
        customer = Customer("Bob", 50.00, 30)
        self.pub.check_drunkness(customer)
        self.assertEqual(0, customer.drunkness)