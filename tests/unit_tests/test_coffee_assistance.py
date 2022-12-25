import unittest
from prod.model.entity import *
from prod.model.logic import *


class TestShopAssistance(unittest.TestCase):

    def test_calculate_total_price_basic(self):
        car = CoffeeCar(10)
        car.add(CoffeeBean("America", "arabica", "height", "small", 10, 5))
        car.add(CoffeeBean("America", "arabica", "height", "small", 2, 4))
        expected = 58

        actual = CoffeeAssistance.calculate_total_price(car)

        self.assertEqual(expected, actual)

    def test_calculate_total_weight_basic(self):
        car = CoffeeCar(10)
        car.add(CoffeeBean("America", "arabica", "height", "small", 10, 5))
        car.add(CoffeeBean("America", "arabica", "height", "small", 2, 4))
        expected = 12

        actual = CoffeeAssistance.calculate_total_weight(car)

        self.assertEqual(expected, actual)
