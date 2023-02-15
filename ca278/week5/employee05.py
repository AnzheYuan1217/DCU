#!/usr/bin/env python3


class Employee:
    def __init__(self, name, job_desc, salary):
        self.name = name
        self.job_desc = job_desc
        self.salary = salary

    def net_salary(self):
        return self.salary * 0.8


print("Enter the employee name:")
a = input()
print("Enter the employee job description:")
b = input()
print("Enter the employee salary:")
c = int(input())

p = Employee(a, b, c)
print(f'Net Salary: {p.net_salary()}')
