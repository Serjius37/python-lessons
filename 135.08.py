#!/usr/bin/python3
'''
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.

Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
'''

# объявление функции
def is_valid_password(password):
    count = 0
    password = password.split(':')
    if len(password) != 3:
        return False
    else:
        if password[0] in password[0][::-1]:
            count += 1 
        password[1] = ''.join(password[1])
        a = int(password[1])
        i = 1
        array = [] 
        while a > i:
            if a % i == 0:
                array.append(i)
            i += 1
        array.append(a)
        if len(array) ==  2: 
            count += 1
        password[2] = ''.join(password[2])
        b = int(password[2])  
        if b % 2 == 0:
            count += 1
        if count == 3:
            return True
        else: 
            return False
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))