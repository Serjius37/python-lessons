#!/usr/bin/python3
'''
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
'''

# объявление функции
def print_digit_sum(n):
    c = 0
    while n:
        c += n % 10
        n = n // 10
    print(c)    
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)