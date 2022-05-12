import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Vodka", 3.00, 10)

    def test_has_name(self):
        self.assertEqual("Vodka", self.drink.name)

    def test_has_price(self):
        self.assertEqual(3.00, self.drink.price)

    def test_has_alcohol_level(self):
        self.assertEqual(10, self.drink.alcohol_level)