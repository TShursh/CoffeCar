from prod.model.entity import *


class Finder:

    @staticmethod
    def find(car):
        DEFAULT_SEARCH = "Arabica"

        if isinstance(car, CoffeeCar):
            ls_find = []
            for i in range(len(car) - 1):
                if car[i].variety == DEFAULT_SEARCH:
                    ls_find.append(car[i])

            return ls_find

#Изменяя DEFAULT_SEARCH и параметр i-го элемента списка можно создать метод поиска по любому из параметров.