import random
from prod.model.entity import *
from prod.model.logic import *
from util import *


def main():
    capacity = int(input("Input capacity car: "))

    coffee_ls = CoffeeCar(capacity)

    while CoffeeAssistance.calculate_total_weight(coffee_ls) <= capacity - 10:
        # тут можно было обратиться к константной переменной MAX_WEIGHT из CoffeeBeanCreator, но я не догадалась как,
        # поэтому хардкод -10, чтобы не было перегруза))
        ls_creator = [InstantCoffeeBoxCreator.create(), CoffeeBeanBoxCreator.create(), GroundCoffeeBoxCreator.create()]
        coffee_ls.add(random.choice(ls_creator))

    Sorter.sort(coffee_ls)

    print(coffee_ls)
    print(f"The total price of coffee is {CoffeeAssistance.calculate_total_price(coffee_ls)} $")
    print(f"The total weight of coffee is {CoffeeAssistance.calculate_total_weight(coffee_ls)} kg")

    print(Finder.find(coffee_ls))


if __name__ == "__main__":
    main()
