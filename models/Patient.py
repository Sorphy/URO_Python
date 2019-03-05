class Patient:

    def __init__(self, pin, fname, lname, birthday, gender, height, weight, phone, email, address, insurance_pin, insurance_number, alergies):
        self._fields = {
            "pin": pin,
            "fname": fname,
            "lname": lname,
            "birthday": birthday,
            "gender": gender,
            "height": height,
            "weight": weight,
            "phone": phone,
            "email": email,
            "address": address,
            "insurance_pin": insurance_pin,
            "insurance_number": insurance_number,
            "alergies": alergies
        }

    @property
    def data(self):
        return self._fields

    def __str__(self):
        return "Patient: " + self._fields["fname"] + " " + self._fields["lname"] + "(" + self._fields["gender"] + ") has height "\
               + str(self._fields["height"]) + " and weight" + str(self._fields["weight"]) + ".\nContact :\n\t"\
               + str(self._fields["phone"]) + "\n\t" + self._fields["email"] + "\nInsurance:\n\t" \
               + str(self._fields["insurance_number"]) + "(" + str(self._fields["insurance_pin"]) + ")\n"\
               + "Address: \n\t" + str(self._fields["address"])
