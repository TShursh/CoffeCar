from prod.model.entity import *


class Finder:

    @staticmethod
    def find(car):
        DEFAULT_SEARCH = "India"
        if isinstance(car, CoffeeCar):
            for i in range(len(car) - 1):
                if car[i].country_of_origin != DEFAULT_SEARCH:
                    car.__delitem__(i)

        return car
