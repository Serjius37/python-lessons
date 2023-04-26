#!/usr/bin/python3
'''
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое 
простое число большее числа num.
Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
'''

def is_prime(a):
    i = 2
    while i < a:
        if a % i == 0:
            return False
        i += 1
    return True
    
def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))