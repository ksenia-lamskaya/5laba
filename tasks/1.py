#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    n = int(input("Введите количество экзаменов: "))

    if n == 1:
        print(f"Мы успешно сдали {n} экзамен")
    elif n == 2 or n == 3 or n == 4:
        print(f"Мы успешно сдали {n} экзамена")
    elif n >= 5 and n <= 20:
        print(f"Мы успешно сдали {n} экзаменов")
    else:
        print("Ошибка! Введите число меньше 21", file=sys.stderr)
        exit(1)

    