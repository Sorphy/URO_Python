class PatientRepository:

    def __init__(self):
        self._patients = {}

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
