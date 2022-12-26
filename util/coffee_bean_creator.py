# В теории понимаю, что можно было сделать один родительский класс CoffeeBoxCreator,
# а от него три штуки наследуемых, но на практике не осилила =)

import random
from util.converter import *


class CoffeeBeanBoxCreator:

    @staticmethod
    def create():
        COUNTRY_OF_ORIGIN = ("Honduras", "Guatemala", "India", "Indonesia", "Vietnam",
                             "Tanzania", "Ethiopia", "Australia", "Oceania")

        VARIETY = ("Arabica", "Canephora", "Liberica", "Excelsa")

        DEGREE_OF_ROAST = ("light", "medium", "dark")

        GRAIN_SIZE = ("very large", "large", "medium", "small", "very small")

        MIN_WEIGHT = 1
        MAX_WEIGHT = 10

        MIN_PRICE_FOR_1KG = 10
        MAX_PRICE_FOR_1KG = 100

        country_of_origin = random.choice(COUNTRY_OF_ORIGIN)
        variety = random.choice(VARIETY)
        degree_of_roast = random.choice(DEGREE_OF_ROAST)
        grain_size = random.choice(GRAIN_SIZE)
        weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
        price_for_1kg = random.randint(MIN_PRICE_FOR_1KG, MAX_PRICE_FOR_1KG)
        coffee_bean_box = CoffeeBean(country_of_origin, variety, degree_of_roast,
                                     grain_size, weight, price_for_1kg)

        return coffee_bean_box
