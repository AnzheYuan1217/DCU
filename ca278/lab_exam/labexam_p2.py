#!/usr/bin/env python3

name = input('What is your name?').split(' ')  # so name is a list of first name and last name.
phone_number = input('What is your phone number?')

while True:
    birthday = input('What is your date of birth (format is ddmmyyyy)?')
    if len(birthday) == 8:
        break
    print('Incorrect format')

first_name = name[0]
last_name = name[1]

patient_id = first_name[0].lower() + birthday + phone_number[-3:] + last_name[0].upper()
print(f'Your patient id is {patient_id}')
