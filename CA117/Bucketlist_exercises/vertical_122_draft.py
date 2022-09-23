#!/usr/bin/env python3

import sys

def lower_case(s):
    return s.lower()

def line_to_virtical(line):
        vir = []

        a = len(line[0])  # 单词个数
        for i in range(a):
            vir.append([])

        for i in line:
            for j in range(a):
                vir[j].append(i[j])

        for i in range(a):
            vir[i] = "".join(vir[i])

        vir = sorted(vir, key=lower_case)
        return vir

def virtical_to_line(line):
        lines = []
        a = len(line[0])
        for i in range(a):
            lines.append([])

        for i in line:
            for j in range(a):
                lines[j].append(i[j])

        for i in range(a):
            lines[i] = "".join(lines[i])

        return lines

def main():
        line = []
        for i in sys.stdin:
            line.append(list(i.strip()))
        vir = line_to_virtical(line)
        vir = sorted(vir, key=lower_case)
        lines = (virtical_to_line(vir))
        for i in lines:
            print(i)


if __name__ == '__main__':
    main()
