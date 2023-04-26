#!/usr/bin/python3
'''
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:

    его длина не менее 88 символов; 
    он содержит как минимум одну заглавную букву (верхний регистр); 
    он содержит как минимум одну строчную букву (нижний регистр);
    он содержит хотя бы одну цифру.

'''

# объявление функции
def is_password_good(password):
    a = 0
    if len(password) >= 8:
        a += 1
    if password not in password.upper():
        a += 1
    if password not in password.lower():
        a += 1
    for i in password:
        if i.isdigit():
            a += 1
            break
    return True if a == 4 else False:
    
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))