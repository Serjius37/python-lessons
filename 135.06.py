#!/usr/bin/python3
'''
Напишите функцию is_one_away(word1, word2), которая принимает в качестве
 аргументов два слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину и 
отличаются ровно в 1 символе и False в противном случае.
'''

# объявление функции
def is_one_away(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] in word2[i]:
            count +=1 
    if len(word1) - 1 == count:
        return True
    else:
        return False
# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))