#!/usr/bin/env python3

def cel_to_fahr(temps):
    lis = {}
    for i in temps:
        lis[float(i)] = (float(i) * 1.8 + 32)
    print("Celsius Fahrenheit")
    return lis


def fahr_to_cel(temps):
    lis = {}
    for i in temps:
        lis[float(i)] = ((float(i) - 32) / 1.8)
    print("Fahrenheit Celsius")
    return lis


print("""Welcome to the Temperature Converter
1 to convert from Celsius to Fahrenheit
2 to convert from Fahrenheit to Celsius
""")
print("Please enter the temperatures (comma-separated):")
temps = input().split(",")
print("Enter the direction of the conversion:")
while True:
    choice = input()
    if choice == '1':
        lis = cel_to_fahr(temps)
        break
    elif choice == '2':
        lis = fahr_to_cel(temps)
        break
    else:
        print("Please choose either 1 or 2:")

for k, v in lis.items():
    print(k, v)
