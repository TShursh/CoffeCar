class CoffeeBox:
    def __init__(self, country_of_origin, variety, weight, price_for_1kg=0):
        self._country_of_origin = country_of_origin
        self._variety = variety
        self._weight = weight
        self._price_for_1kg = price_for_1kg

    @property
    def price_box(self):
        return self._price_for_1kg * self._weight

    @property
    def country_of_origin(self):
        return self._country_of_origin

    @country_of_origin.setter
    def country_of_origin(self, country_of_origin):
        self._country_of_origin = country_of_origin

    @country_of_origin.deleter
    def country_of_origin(self):
        del self._country_of_origin

    @property
    def variety(self):
        return self._variety

    @variety.setter
    def variety(self, variety):
        self._variety = variety

    @variety.deleter
    def variety(self):
        del self._variety

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight >= 0:
            self._weight = weight
        else:
            if not hasattr(self, "_weight"):
                self._weight = 0
            else:
                raise ValueError("Coffee weight was wrong")

    @property
    def price_for_1kg(self):
        return self._price_for_1kg

    @price_for_1kg.setter
    def price_for_1kg(self, price_for_1kg):
        if price_for_1kg >= 0:
            self._price_for_1kg = price_for_1kg
        else:
            if not hasattr(self, "_price_for_1kg"):
                self._price_for_1kg = 0
            else:
                raise ValueError("Coffee price was wrong")

    @price_for_1kg.deleter
    def price_for_1kg(self):
        del self._price_for_1kg

    def __str__(self):
        return (f"Coffee box: country of origin - {self._country_of_origin}; "
                f"variety - {self._variety}; "
                f"weight - {self._weight}; "
                f"price for 1kg - {self._price_for_1kg}")

