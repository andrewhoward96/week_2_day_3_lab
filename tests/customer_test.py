import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Bob", 50.00, 30)
        self.drink = Drink("Vodka", 3.00, 10)

    def test_has_name(self):
        self.assertEqual("Bob", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_customer_can_reduce_wallet(self):
        self.customer.reduce_wallet(5.00)
        self.assertEqual(45.00, self.customer.wallet)

    def test_drinks_start_at_0(self):
        self.assertEqual(0, self.customer.drink_count())

    def test_can_add_drink(self):
        self.customer.add_drink(self.drink)
        self.assertEqual(1, self.customer.drink_count())

    def test_increase_drunkness(self):
        self.customer.add_drink(self.drink)
        self.assertEqual(10, self.customer.drunkness)