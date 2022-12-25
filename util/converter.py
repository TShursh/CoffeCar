from prod.model.entity import *


class Converter:

    @staticmethod
    def convert_to_string(ls):
        msg = "List of coffee box: \n"

        if not isinstance(ls, (list, tuple)):
            return "List is empty."

        for coffee_box in ls:
            if isinstance(coffee_box, CoffeeBox):
                msg += str(coffee_box) + "\n"

        return msg
