#!/usr/bin/python3
'''
Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел палиндромов от 100100 до 10001000.
'''

palindromes = [i for i in range(100, 1000) if str(i)[-1] == str(i)]

print(palindromes)
