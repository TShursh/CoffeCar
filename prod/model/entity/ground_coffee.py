from prod.model.entity import *


class GroundCoffee(CoffeeBean):
    def __init__(self, country_of_origin, variety, degree_of_roast, grain_size,
                 degree_of_grinding, weight, price_for_1kg):
        super().__init__(country_of_origin, variety, degree_of_roast, grain_size, weight, price_for_1kg)
        self._degree_of_grinding = degree_of_grinding

    @property
    def degree_of_grinding(self):
        return self._degree_of_grinding

    @degree_of_grinding.setter
    def degree_of_grinding(self, degree_of_grinding):
        self._degree_of_grinding = degree_of_grinding

    @degree_of_grinding.deleter
    def degree_of_grinding(self):
        del self._degree_of_grinding

    def __str__(self):
        return (f"Ground box: country - {self._country_of_origin}; "
                f"variety - {self._variety}; "
                f"degree of roast - {self._degree_of_roast}; "
                f"grain size - {self._grain_size}; "
                f"grinding - {self._degree_of_grinding}; "
                f"weight = {self._weight}; "
                f"price for 1 kg = {self._price_for_1kg}.")
