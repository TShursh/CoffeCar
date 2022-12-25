import random
from prod.model.entity import *
from prod.model.logic.coffee_assistance import CoffeeAssistance
from util import *

def main():

   capacity = int(input("Input capacity car: "))

   cc = CoffeeCar(capacity)
   cc.add(InstantCoffeeBoxCreator.create())
   cc.add(CoffeeBeanBoxCreator.create())
   cc.add(InstantCoffeeBoxCreator.create())
   print(cc)


if __name__ == "__main__":
   main()

