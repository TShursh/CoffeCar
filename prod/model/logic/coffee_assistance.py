from prod.model.entity import *
from util import *


class CoffeeAssistance:

    @staticmethod
    def calculate_total_price(coffee_list):
        if not isinstance(coffee_list, CoffeeCar):
            return -1

        total = 0

        for cb in coffee_list:
            if isinstance(coffee_list, CoffeeCar):
                total += cb

        return total




