from models.Address import Address
from models.Recipe import Recipe
from utils.PatientBuilder import PatientBuilder

class PatientRepository:

    _patient_repository = None

    def __init__(self):
        self._patients = {
            '950615/4455':
                PatientBuilder()
                .set_pin('950615/4455')
                .set_fname('Filip')
                .set_lname('Novák')
                .set_height(150)
                .set_weight(100)
                .set_insurance_pin(120)
                .set_insurance_number(123456789)
                .set_phone(601452147)
                .set_email('filip.novak@gmail.com')
                .set_address(Address('Ostrava', 36, 73545, '17.listopadu'))
                .set_alergies(['Penicilin','Sun'])
                .set_recipes(
                    [
                        Recipe(1, 235147, 'Prestance', '1-1-1', '15/06/2018', '30/02/2019'),
                        Recipe(1, 225142, 'Accuzide', '1-1-1', '30/08/2018', '01/03/2019'),
                        Recipe(1, 365214, 'Dapril', '1-1-1', '15/01/2018', '18/02/2020'),
                    ])
                .build(),
            '985426/4477':
                PatientBuilder()
                .set_pin('985426/4477')
                .set_fname('Petra')
                .set_lname('Oloupaná')
                .set_height(125)
                .set_weight(50)
                .set_insurance_pin(130)
                .set_insurance_number(965874147)
                .set_phone(852147852)
                .set_email('p.oloupna@gmail.com')
                .set_address(Address('Praha', 36, 73545, '17.listopadu'))
                .set_recipes(
                [
                    Recipe(1, 235147, 'Prestance', '1-1-1', '15/06/2018', '30/02/2019'),
                ])
                .set_alergies(['Sun'])
                .build(),
            '941230/5555':
                PatientBuilder()
                .set_pin('941230/5555')
                .set_fname('Martin')
                .set_lname('Laosky')
                .set_height(180)
                .set_weight(120)
                .set_insurance_pin(220)
                .set_insurance_number(258452147)
                .set_phone(254445214)
                .set_email('martin.l@gmail.com')
                .set_address(Address('Olomouc', 36, 73545, '17.listopadu'))
                .set_recipes(
                [
                    Recipe(1, 235147, 'Prestance', '1-1-1', '15/06/2018', '30/02/2019'),
                    Recipe(1, 547852, 'Walmark', '1-1-1', '30/08/2018', '01/03/2019'),
                ])
                .set_alergies(['Penicilin'])
                .build(),
            '935212/8844':
                PatientBuilder()
                .set_pin('935212/8844')
                .set_fname('Marie')
                .set_lname('Terezie')
                .set_height(120)
                .set_weight(80)
                .set_insurance_pin(333)
                .set_insurance_number(254147411)
                .set_phone(963258741)
                .set_email('m.ter@gmail.com')
                .set_address(Address('Opava', 36, 73545, '17.listopadu'))
                .set_recipes(
                [
                    Recipe(1, 125478, 'Diacordin', '1-1-1', '15/06/2018', '30/02/2019')
                ])
                .set_alergies(['Penicilin'])
                .build()
            }

    def insert(self, patient):
        self._patients[patient.data["pin"]] = patient

    def update(self, patient):
        if patient.data["pin"] in self._patients:
            self._patients.update({patient.data["pin"]: patient})
        else:
            raise Exception("Patient not found")

    def get_by_pin(self, pin):
        return self._patients[pin]

    def get_all(self):
        return list(self._patients.values())

    def remove(self, pin):
        del self._patients[pin]

    def remove_recipe(self, pin, code):
        for key, patient in self._patients.items():
            if key == pin:
                for recipe in patient.data['recipes']:
                    if recipe.data['code'] == code:
                        patient.data['recipes'].remove(recipe)
                        break

    def add_recipe(self, pin, recipe):
        self._patients[pin].data['recipes'].append(recipe)

    @staticmethod
    def get_instance():
        if PatientRepository._patient_repository is None:
            PatientRepository._patient_repository = PatientRepository()
        return PatientRepository._patient_repository
