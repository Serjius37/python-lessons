'''
На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
Формат входных данных 
На вход программе подается строка.
Формат выходных данны
Программа должна вывести «YES» если имя и фамилия начинаются с заглавной буквы и «NO» в противном случае.
'''

s = input()
if s == s.title():
    print("YES")
else:
    print("NO")
