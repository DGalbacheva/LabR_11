#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    num = int(input("Введите число: "))
    if num > 0:
        positive()
    elif num < 0:
        negative()
    else:
        print("Ваше число равно 0")

def positive():
    print("Ваше число положительное")

def negative():
    print("Ваше число отрицательное")

if __name__ == '__main__':
    test()