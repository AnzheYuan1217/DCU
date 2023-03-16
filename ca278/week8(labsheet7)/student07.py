#!/usr/bin/env python3

import sys

class Student: 

    id_counter = 1
    def __init__(self, name, exam_mark, ca_mark):
        self.name = name
        self.exam_mark = int(exam_mark)
        self.ca_mark = int(ca_mark)
        self.id = Student.id_counter
        Student.id_counter += 1


    def get_average(self):
        return (self.exam_mark + self.ca_mark) / 2

    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Average: {self.get_average()}'


# filename = sys.argv[1]

with open('students.txt') as f:
    for i in f.readlines():
        line = i.strip().split(',')
        temp = Student(line[0], line[1], line[2])
        print(temp)
