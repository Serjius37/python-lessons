'''
На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет является ли оно палиндромом.
Формат входных данных
На вход программе подается одно слово в нижнем регистре.
Формат выходных данных
Программа должна вывести «YES», если слово является палиндромом и «NO» в противном случае.
Примечание. Палиндром читается одинаково в обоих направлениях, например слово «потоп».
'''

s = input()
a = s[::-1]
if s in a:
    print("YES")
else:
    print("NO")
