#!/usr/bin/python3
'''
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.

Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
'''

def prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2
def palindrome(text):
    return text == text[::-1]
def valid_password(password):
    s = password.split(':')
    if len(s) != 3:
        return False
    return all([palindrome(s[0]), prime(int(s[1])), int(s[2]) % 2 == 0])
    
psw = input()

print(valid_password(psw))