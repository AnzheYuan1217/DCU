#!/usr/bin/env python3


class Patient:
    def __init__(self, name, phone, dob):
        self.name = name
        self.phone = phone
        self.dob = dob  # date of birth

    def generate_id(self):
        f_name = self.name.split(' ')[0]
        l_name = self.name.split(' ')[1]
        patient_id = f_name[0].lower() + self.dob + self.phone[-3:] + l_name[0].upper()
        return patient_id

    def get_age_bracket(self):
        year = int(self.dob[4:8])
        if year > 2006:
            return 'minor'
        elif year < 1959:
            return 'senior'
        else:
            return 'adult'
