from prod.model.entity import *


class Sorter:

    @staticmethod
    def sort(car):
        if isinstance(car, CoffeeCar):
            for i in range(len(car) - 1):
                for index in range(len(car) - 1 - i):
                    if car[index].country_of_origin > car[index + 1].country_of_origin:
                        temp = car[index]
                        car[index] = car[index + 1]
                        car[index + 1] = temp