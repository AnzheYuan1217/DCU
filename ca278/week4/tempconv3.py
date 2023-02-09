#!/usr/bin/env python3

print("""Welcome to the Temperature Converter
1 to convert from Celsius to Fahrenheit
2 to convert from Fahrenheit to Celsius
""")
print("Please enter the temperatures (comma-separated):")
lis = {}
temps = input().split(",")
print("Enter the direction of the conversion:")

while True:
    choice = input()
    if choice == '1' or choice == '2':
        break
    print("Please choose either 1 or 2:")

if choice == '1':
    for i in temps:
        lis[float(i)] = (float(i) * 1.8 + 32)
    print("Celsius Fahrenheit")

elif choice == '2':
    for i in temps:
        lis[float(i)] = ((float(i) - 32) / 1.8)
    print("Fahrenheit Celsius")

for k, v in lis.items():
    print(k, v)
