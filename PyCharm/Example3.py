#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def cylinder():
    r = float(input("Ввести радиус цилин: "))
    h = float(input("Введите высоту цилиндра: "))
    s = 2 * math.pi * r ** 2
    def circle():
        s_circle = math.pi * r ** 2
        return s_circle
    check = int(input("1 - боковая площадь; 2 - полная площадь: "))
    if check == 1:
        print(f"Боковая площадь цилиндеа: {s}")
    else:
        full_s = s + circle() * 2
        print(f"Полная площадь цилиндра: {full_s}")
if __name__ == '__main__':
    cylinder()