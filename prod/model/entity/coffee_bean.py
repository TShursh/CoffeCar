from prod.model.entity import *


class CoffeeBean(CoffeeBox):
    def __init__(self, country_of_origin, variety, degree_of_roast, grain_size, weight, price_for_1kg=0):
        super().__init__(country_of_origin, variety, weight, price_for_1kg)
        self._degree_of_roast = degree_of_roast
        self._grain_size = grain_size

    @property
    def degree_of_roast(self):
        return self._degree_of_roast

    @degree_of_roast.setter
    def degree_of_roast(self, degree_of_roast):
        self._degree_of_roast = degree_of_roast

    @degree_of_roast.deleter
    def degree_of_roast(self):
        del self._degree_of_roast

    @property
    def grain_size(self):
        return self._grain_size

    @grain_size.setter
    def grain_size(self, grain_size):
        self._grain_size = grain_size

    @grain_size.deleter
    def grain_size(self):
        del self._grain_size

    def __str__(self):
        return (f"Coffee bean box: country of origin - {self._country_of_origin}; "
                f"variety - {self._variety}; "
                f"degree of roast - {self._degree_of_roast}; "
                f"grain size - {self._grain_size}; "
                f"weight - {self._weight}; "
                f"price for 1 kg - {self._price_for_1kg}.")


