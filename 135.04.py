#!/usr/bin/python3
'''
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.
Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
'''

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
    
def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))