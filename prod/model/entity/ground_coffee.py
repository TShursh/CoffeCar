from prod.model.entity import *


class GroundCoffee(CoffeeBean):
    def __init__(self, country_of_origin, degree_of_roast, grain_size,
                 degree_of_grinding, variety, price_for_1kg=0):
        super().__init__(country_of_origin, degree_of_roast, grain_size, variety, price_for_1kg)
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
        return (f"Ground box: country of origin - {self._country_of_origin}; "
                f"variety - {self._variety}; "
                f"degree of roast - {self._degree_of_roast}; "
                f"grain size - {self._grain_size}; "
                f"degree of grinding - {self._degree_of_grinding}; "
                f"weight - {self._weight}; "
                f"price = {self._price_for_1kg}.")

