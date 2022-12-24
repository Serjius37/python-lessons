#!/usr/bin/python3
'''
Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.
'''

# объявление функции
def get_factors(a):
    i = 1
    array = [] 
    while a > i:
        if a % i == 0:
            array.append(i)
        i += 1
    array.append(a)        
    return array

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))