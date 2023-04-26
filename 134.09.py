#!/usr/bin/python3
'''
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.
'''

# объявление функции
def get_factors(a):
    count = 1
    i = 1
    while a > i:
        if a % i == 0:
            count += 1
        i += 1      
    return count

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))