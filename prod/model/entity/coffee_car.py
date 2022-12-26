from prod.model.entity import *


class CoffeeCar:
    DEFAULT_CAPACITY = 100

    def __init__(self, capacity=DEFAULT_CAPACITY):
        self._ls = []
        if capacity > 0:
            self._capacity = capacity
        else:
            self._capacity = CoffeeCar.DEFAULT_CAPACITY

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return len(self._ls)

    def add(self, coffee_box):
        if isinstance(coffee_box, CoffeeBox):
            self._ls.append(coffee_box)

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            return self._ls[index]
        else:
            raise Exception()

    def __setitem__(self, index, value):
        if (isinstance(index, int)
                and 0 <= index < len(self)
                and isinstance(value, CoffeeBox)):
            self._ls[index] = value
        else:
            raise Exception()

    def __delitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            del self._ls[index]
        else:
            raise Exception()

    def __str__(self):
        if not self._ls:
            return f"Coffee car is empty! You can load {self._capacity} kg of coffee."
        else:
            msg = "Coffee list:\n"
            for coffee_box in self._ls:
                msg += str(coffee_box) + "\n"
            return msg
