#!/usr/bin/env python3

import sys

def main():
    text = sys.stdin.read()    # 把输入保存下来

    a = text.strip().split("\n")    # 转换成list样式

    clubs = []     # 列出俱乐部
    for i in a:
        b = i.split()
        clubs.append(" ".join(b[1:-8]))

    length = 0     # 找出俱乐部里最长的名字
    for i in clubs:
        if len(i) > length:
            length = len(i)
    # 单独输出顶部一行
    print(
        f'{"POS":>3s} {"CLUB":<{length:d}s} {"P":>2s} {"W":>3s} {"D":>3s} '
        f'{"L":>3s} {"GF":>3s} {"GA":>3s} {"GD":>3s} {"PTS":>3s}')

    for i in a:     # 输出内容
        i = i.split()
        club = ' '.join(i[1:-8])
        print(
            f'{int(i[0]):3d} {club:{length:d}s} {int(i[-8]):2d} {int(i[-7]):3d} '
            f'{int(i[-6]):3d} {int(i[-5]):3d} {int(i[-4]):3d} {int(i[-3]):3d} '
            f'{int(i[-2]):3d} {int(i[-1]):3d}')
        """
        或者
        pos = int(i[0])
        club = ' '.join(i[1:-8])
        p = int(i[-8])
        w = int(i[-7])
        d = int(i[-6])
        l = int(i[-5])
        gf = int(i[-4])
        ga = int(i[-3])
        gd = int(i[-2])
        pts = int(i[-1])
        print(f'{pos:3d} {club:{length:d}s} {p:2d} {w:3d} {d:3d} {l:3d} {gf:3d} {ga:3d} {gd:3d} {pts:3d}')
        """
if __name__ == '__main__':
    main()
