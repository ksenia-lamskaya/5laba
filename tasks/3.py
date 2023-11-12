#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

for i in range(10, 100):
    tens = i // 10
    ones = i % 10
    if (tens + ones) + (tens + ones) ** 2 == i:
        print(i)
