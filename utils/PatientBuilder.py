from models.Patient import Patient


class PatientBuilder:

    def __init__(self):
        self._pin = None
        self._fname = None
        self._lname = None

        self._birthday = None
        self._gender = None

        self._height = None
        self._weight = None

        self._phone = None
        self._email = None

        self._address = None

        self._insurance_pin = None
        self._insurance_number = None

        self._alergies = ()

        self._recipes = []

    def set_fname(self, fname):
        self._fname = fname
        return self

    def set_lname(self, lname):
        self._lname = lname
        return self

    def set_birthday(self, day):
        self._birthday = day

    def set_gender(self, gender):
        self._gender = gender

    def set_pin(self, pin):
        self._pin = pin

        year = self._pin[0:2]

        if(int(self._pin[2:4]) > 50):
            month = str(int(self._pin[2:4]) - 50)
            self.set_gender("F")
        else:
            month = str(self._pin[2:4])
            self.set_gender("M")

        day = self._pin[4:6]
        self._birthday = day + "/" + month + "/" + year

        return self

    def set_height(self, height):
        self._height = height
        return self

    def set_weight(self, weight):
        self._weight = weight
        return self

    def set_address(self, address):
        self._address = address
        return self

    def set_phone(self, phone):
        self._phone = phone
        return self

    def set_email(self, email):
        self._email = email
        return self

    def set_alergies(self, alergies):
        self._alegries = alergies
        return self

    def set_insurance_number(self, number):
        self._insurance_number = number
        return self

    def set_insurance_pin(self, pin):
        self._insurance_pin = pin
        return self

    def set_recipes(self, recipes):
        self._recipes = recipes
        return self

    def build(self):
        if self._lname==None or self._fname==None or self._pin==None\
            or self._phone==None or self._insurance_number==None or self._insurance_pin==None:
            raise Exception("Not all required attributes")
        else:
            return Patient(self._pin, self._fname, self._lname, self._birthday, self._gender, self._height, self._weight,
                       self._phone, self._email, self._address, self._insurance_pin, self._insurance_number, self._alergies, self._recipes)

