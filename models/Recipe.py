class Recipe:
    def __init__(self, type, code, name, dosage, from_date, to_date):
        self._fields = {
            'type': type,
            'code': code,
            'name': name,
            'dosage': dosage,
            'from': from_date,
            'to': to_date
        }

    @property
    def data(self):
        return self._fields