#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

EPS = 1e-10

if __name__=="__main__":
    x = float(input("Value of x?: "))
    if x < 0 and x > 2:
        print("Illegalvalue of x")
        exit(1)

    a = x
    S, k = a, 1

    while math.fabs(a) > EPS:
        a = (((-1)**k * (x - 1)**k)/k**2)
        S += a
        k += 1

    print(f'f(x) = {S}')
