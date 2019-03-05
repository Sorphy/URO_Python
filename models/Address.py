class Address:
    def __init__(self, city, zip_code, postal_code, street=""):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._postal_code = postal_code

    @property
    def city(self):
        return self._city

    @property
    def street(self):
        return self._street

    @property
    def zip_code(self):
        return self._zip_code

    @property
    def postal_code(self):
        return self._postal_code

    def __str__(self):
        street = ""
        if self.street != "":
            street = " " + self.street
        else:
            street = ""

        return self._city + street + " " + str(self._zip_code) + " " + str(self._postal_code)
