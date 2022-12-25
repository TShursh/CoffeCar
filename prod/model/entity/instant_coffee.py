from prod.model.entity import *


class InstantCoffee(CoffeeBox):
    def __init__(self, country_of_origin, variety, mode_of_production, weight, price_for_1kg):
        super().__init__(country_of_origin, variety, weight, price_for_1kg)
        self._mode_of_production = mode_of_production

    @property
    def mode_of_production(self):
        return self._mode_of_production

    @mode_of_production.setter
    def mode_of_production(self, mode_of_production):
        self._mode_of_production = mode_of_production

    @mode_of_production.deleter
    def mode_of_production(self):
        del self._mode_of_production

    def __str__(self):
        return (f"Instant box: country - {self._country_of_origin}; "
                f"variety - {self._variety}; "
                f"mode of production - {self._mode_of_production}; "
                f"weight = {self._weight}; "
                f"price for 1 kg = {self._price_for_1kg}.")


