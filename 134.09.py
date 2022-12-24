#!/usr/bin/python3
'''
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.
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
    return len(array)

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))