from prod.model.entity import *


class CoffeeAssistance:

    @staticmethod
    def calculate_total_price(coffee_list):
        if not isinstance(coffee_list, CoffeeCar):
            return -1

        total = 0

        for cb in range(len(coffee_list)):
            if isinstance(coffee_list, CoffeeCar):
                total += coffee_list[cb].price_box

        return total

    @staticmethod
    def calculate_total_weight(coffee_list):
        if not isinstance(coffee_list, CoffeeCar):
            return -1

        total = 0

        for cb in range(len(coffee_list)):
            if isinstance(coffee_list, CoffeeCar):
                total += coffee_list[cb].weight

        return total
