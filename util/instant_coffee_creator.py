import random
from util.converter import *


class InstantCoffeeBoxCreator:

    @staticmethod
    def create():
        COUNTRY_OF_ORIGIN = ("Honduras", "Guatemala", "India", "Indonesia", "Vietnam",
                             "Tanzania", "Ethiopia", "Australia", "Oceania")

        VARIETY = ("Arabica", "Canephora", "Liberica", "Excelsa")

        MODE_OF_PRODUCTION = ("powder", "granular", "sublimated", "ground in soluble")

        MIN_WEIGHT = 1
        MAX_WEIGHT = 10

        MIN_PRICE_FOR_1KG = 10
        MAX_PRICE_FOR_1KG = 100

        country_of_origin = random.choice(COUNTRY_OF_ORIGIN)
        variety = random.choice(VARIETY)
        weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
        mode_of_production = random.choice(MODE_OF_PRODUCTION)
        price_for_1kg = random.randint(MIN_PRICE_FOR_1KG, MAX_PRICE_FOR_1KG)
        instant_coffee_box = InstantCoffee(country_of_origin, variety, mode_of_production, weight, price_for_1kg)

        return instant_coffee_box
