#!/usr/bin/python3
'''
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.
'''

# объявление функции
def is_prime(a):
    i = 1
    array = [] 
    while a > i:
        if a % i == 0:
            array.append(i)
        i += 1
    array.append(a)
    if len(array) ==  2:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))