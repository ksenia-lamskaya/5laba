#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a1 = float(input("Введите a1: "))
    b1 = float(input("Введите b1: "))
    c1 = float(input("Введите c1: "))

    a2 = float(input("Введите a2: "))
    b2 = float(input("Введите b2: "))
    c2 = float(input("Введите c2: "))

    det = a1*b2 - a2*b1
    if det == 0:
        if a1*c2 == a2*c1 and b1*c2 == b2*c1:
            print("Прямые совпадают")
        else:
            print("Прямые параллельны")
    else:
        x = (b2*c1 - b1*c2)/det
        y = (a1*c2 - a2*c1)/det
        print(f"Точка пересечения прямых: ({x}, {y})")

    