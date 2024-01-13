
#HOMEWORK 2.11
# a = 'Python'
# print(a[2:])
# print(a.upper())
# b = 'ashley'
# print('A'*2 + b[2:])
# c = str(input("Enter a letter "))
# print(c.count(' ') + 1)
#
#
# Например, при вводе строки “Всем привет!” программа выведет “Вст!”.
#
# a = input("Enter your words ")
# b = []
# for i in range(0, len(a)):
#     if a[i] == 'e':
#         b.append(i)
# print(a[:(b[0])] + a[max(b)+1:len(a)])


#HOMEWORK 3.11

# a = int(input("Enter first nember "))
# b = int(input("Enter second number "))
# if a > b:
#     print("First one is bigger")
# elif a < b:
#     print("Second one is bigger")
# else:
#     print("They are the same!")


# a = input("What is your name? \n")
# print("Hello", a, ":) How do you feel right now?")
# b = input()
# print("I'm very glad that you are", b)


# a = int(input("Enter three-digit number "))
# if 99 < a < 1000:
#     b=a%10 + (a%100)//10
#     c=(a%100)//10 + a//100
#     if b > c:
#         print(str(b)+str(c))
#     elif c > b:
#         print(str(c)+str(b))
#     elif c == b:
#         print(str(c)+str(b))
# else:
#     print("Error")


# a = input("Enter your cell - ")
# b = input("Enter checking cell - ")
# c = a[0]
# d = b[0]
# e = int(a[1])
# f = int(b[1])
# if abs(ord(c)-ord(d)) == abs(e-f):
#     print("Yes, it's possible!")
# else:
#     print("No, can't be done!")





#HOMEWORK 5.11
# За каждой партой может сидеть не больше двух учеников.
# Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
# a = int(input("Enter 1 class "))
# b = int(input("Enter 2 class "))
# c = int(input("Enter 3 class "))
# x = a//2 + a%2 + b//2 + b%2 + c//2 + c%2
# print(x, "places")


# Напишите программу, которая по данным ненулевым числам x и y определяет,
# в какой из четвертей координатной плоскости находится точка (x,y)
# x = int(input("Enter X "))
# y = int(input("Enter Y "))
# if (x > 0) and (y>0):
#     print("1")
# elif (x<0) and (y<0):
#     print("3")
# elif (x<0) and (y>0):
#     print("2")
# elif (x>0) and (y<0):
#     print("4")


# Напишите программу, которая находит
# наибольшее из трёх целых чисел.
# a = int(input("Enter 1 number "))
# b = int(input("Enter 2 number "))
# c = int(input("Enter 3 number "))
# x = []
# x.append(a)
# x.append(b)
# x.append(c)
# print(max(x))


'''Шахматная ладья ходит по горизонтали или вертикали.
Даны две различные клетки шахматной доски, определите,
может ли ладья попасть c первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом
для второй клетки. Программа должна вывести ДА,
если из первой клетки ходом ладьи можно попасть во вторую
или НЕТ в противном случае.'''
# a = input("Enter your cell - ")
# b = input("Enter checking cell - ")
# c = a[0]
# d = b[0]
# e = int(a[1])
# f = int(b[1])
# if (abs(ord(c)-ord(d))==0) or (abs(e-f)==0):
#     print("Yes, it's possible!")
# else:
#     print("No, can't be done!")




# Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски,
# определите, может ли слон попасть с первой клетки на вторую одним ходом.
# Вводится четыре числа – числовые координаты двух клеток шахматной доски
# (вместо букв для обозначения используются числа).
# Если указанные клетки покрашены в один цвет, программа выведет ДА, а если в разные – НЕТ.
# a = input("Enter your cell - ")
# b = input("Enter checking cell - ")
# c = a[0]
# d = b[0]
# e = a[1]
# f = b[1]
# if abs(ord(c)-ord(d))==abs(ord(e)-ord(f)):
#     print("Yes, it's possible!")
# else:
#     print("No, can't be done!"






#HOMEWORK 5.11
# Напишите программу, которая будет запрашивать у пользователя два числа
# и операцию, которую нужно выполнить с этими числами (+, -, *, /).
# Программа должна выводить результат операции или сообщение об ошибке,
# если операция введена некорректно или происходит деление на ноль.

# com = input("Enter an operation (+-*/) ")
# if not(com in "+-/*"):
#     print("Error")
#     exit()
# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# if com == "+":
#     print(a+b)
# if com == "-":
#     print(a-b)
# if com == "*":
#     print(a*b)
# if com == "/":
#     if b == 0:
#         print("Error")
#     else:
#         print(a/b)


# Напишите программу, которая считает сумму цифр натурального трёхзначного числа.
# Программа должна вывести одно число – сумму цифр введённого пользователем
# трёхзначного числа.

# a = input("Enter three-digit number ")
# if int(a)<=99 or int(a)>=1000:
#     print("Error")
# else:
#     print(int(a[0]) + int(a[1]) + int(a[2]))



# Напишите программу, которая проверяет надёжность пароля пользователя.
# Программа должна проверять длину пароля (8 и более символов),
# наличие минимум одной цифры в пароле, пароль должен начинаться с заглавной буквы.
# Если введённый пароль НЕ соответствует требованиям, программа должна указать
# на исправление, в противном случае – вывести “Пароль принят”.


# a = str(input("Enter a password "))
# b = str(a[0])
# if not b.isupper():
#     print("Password is weak")
#     exit()
# if not (("1" in a) or ("2" in a) or ("3" in a) or ("4" in a) or ("5" in a) or ("6" in a) or ("7" in a) or ("8" in a) or ("9" in a) or ("0" in a)):
#     print("Password is weak")
#     exit()
# if len(a) < 8:
#     print("Password is weak")
#     exit()
# else:
#     print("Strong password!")




# Вводится четыре числа – числовые координаты двух клеток шахматной доски
# (вместо букв для обозначения используются числа). Если указанные клетки
# покрашены в один цвет, программа выведет “ДА”, а если в разные – “НЕТ”.

# print("Enter cells from a1 to h8")
# a = input("Enter your cell - ")
# b = input("Enter checking cell - ")
# c = a[0]
# d = b[0]
# e = int(a[1])
# f = int(b[1])
# if abs(ord(c)-ord(d)) == abs(e-f):
#     print("Yes, it's possible!")
# else:
#     print("No, can't be done!")


# Вводится четыре числа – числовые координаты двух клеток шахматной доски
# Если указанные клетки покрашены в один цвет, программа выведет “ДА”,
# а если в разные – “НЕТ”.


# print("Enter cells from a1 to h8, to check if they have same colours")
# a = input("Enter your first cell - ")
# b = input("Enter your second cell - ")
# c = a[0]
# d = b[0]
# e = int(a[1])
# f = int(b[1])
# if (abs(ord(c)-ord(d))%2==0 and abs(e-f)%2==0) or (abs(ord(c)-ord(d))%2!=0 and abs(e-f)%2!=0):
#     print("Yes")
# else:
#     print("No")


#HOMEWORK 6.11
# a = 0
# while a<=3:
#     a=a+1
# print(a)
#
# print('Text'.lower())

# m = 1
# n = 0
# while m<64:
#     m = m*2
#     n = n+1
# print(n)



#HOMEWORK 7.11
#Дано целое число, не меньшее 2. Выведите его наименьший натуральный
# делитель, отличный от 1.

# a = int(input())
# b = 2
# while a%b!=0:
#     b = b+1
# print("Divider is", b)


# Пользователь вводит натуральное число N.
# Программа должна вывести все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания.
# a = int(input())
# b = 1
# while b*b < a:
#     print(b*b)
#     b += 1


# Программа получает на вход последовательность из натуральных чисел,
# оканчивающуюся нулём (0 не входит в последовательность).
# Определите значение наибольшего элемента последовательности.
# a = int(input())
# b = []
# b.append(a)
# while a != 0:
#     a = int(input())
#     b.append(a)
# print(max(b))


# Программа получает на вход последовательность из натуральных чисел,
# оканчивающуюся нулём (0 не входит в последовательность). Определите,
# сколько элементов этой последовательности больше предыдущего элемента.
# a = int(input())
# b = []
# count = 0
# b.append(a)
# while a != 0:
#     a = int(input())
#     b.append(a)
# for i in range(1, len(b)):
#     if b[i-1] < b[i]:
#         count += 1
# print(count)



# HOMEWORK 12.11

# Напишите программу, которая находит сумму всех натуральных чисел от 1
# до введенного натурального числа n включительно (n > 1). Например,
# при вводе 12 программа выведет 78, а при вводе 99 программа выведет 4950.
# a = int(input())
# b = 0
# for i in range(1, a+1):
#     b += i
# print(b)


# Напишите программу, которая очищает введенную строку от цифр.
# Например, при вводе “4ud0 3o.1” программа выведет “ud o.”
# a = input()
# if "1" in a:
#     a = a.replace("1", "")
# if "2" in a:
#     a = a.replace("2", "")
# if "3" in a:
#     a = a.replace("3", "")
# if "4" in a:
#     a = a.replace("4", "")
# if "5" in a:
#     a = a.replace("5", "")
# if "6" in a:
#     a = a.replace("6", "")
# if "7" in a:
#     a = a.replace("7", "")
# if "8" in a:
#     a = a.replace("8", "")
# if "9" in a:
#     a = a.replace("9", "")
# if "0" in a:
#     a = a.replace("0", "")
# print(a)


# Пользователь вводит последовательность целых чисел, а затем 0 для окончания ввода
# 0 не входит. Программа должна вывести наибольшее число последовательности,
# которое кратно 2 или 3, но не оканчивается на 8.

# a = int(input())
# b = []
# b.append(a)
# c = 1
# while a != 0:
#     a = int(input())
#     b.append(a)
# for i in range(0, len(b)):
#     if b[i] > c and (b[i] % 2 == 0 or b[i] % 3 == 0) and b[i] % 10 != 8:
#         c = b[i]
# print(c)


#Создайте программу с циклами, которая нарисует в терминале следующую картину:
# *
# **
# ***
# **
# *
# a = int(input("Enter max count of stars: "))
# for i in range(0, a+1):
#     print("*"*i)
# for y in range(1, a):
#     print("*"*(a-y))


# HOMEWORK 13.11

# Например, при вводе “abadba” программа выведет 3.
# a = input()
# print(len(set(a)))

#Вводится две строки. Выведите все символы, которые входят как в первую, так и во вторую строку.
# m = set(input())
# n = set(input())
# print(m&n)

# Напишите программу, которая принимает на вход строку. Создайте из строки множество,
# содержащее все буквы, встречающиеся в строке в чётном количестве. Выведите множество.
#pizdec
# a = input()
# c = []
# for u in a:
#     c.append(u)
# print(c)
# b = set(a)
# print(b)
# f = []
# for o in b:
#     count = 0
#     for y in range(len(c)):
#         if c[y] == o:
#             count += 1
#     if count % 2 == 0:
#         f.append(o)
# print(set(f))

# Напишите программу, которая принимает на вход строку.
# Создайте из строки словарь, содержащий частоту встречаемости каждого символа в строке.
# a = input()
# c = []
# for u in a:
#     c.append(u)
# b = set(a)
# f = dict()
# for o in b:
#     count = 0
#     for y in range(len(c)):
#         if c[y] == o:
#             count += 1
#     f[o] = count
# print(f)


# HOMEWORK 13.11
# На вход программе поступает последовательность из натуральных чисел, оканчивающиеся нулём
# (0 не входит в последовательность). Программа должна вывести список из квадратов введённых чисел.
# s = []
# while True:
#     a = int(input())
#     s.append(a*a)
#     if a == 0:
#         break
# print(s)

# На вход программе поступает последовательность из натуральных чисел, оканчивающиеся нулём
# Программа должна вывести последовательность неповторяющихся чисел в порядке невозрастания.
# s = []
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     if a in s:
#         continue
#     s.append(a)
# print(sorted(s, reverse=True))

# На вход программе поступает слово S, количество N вводимых строк и N строк.
# Программа должна вывести количество повторений слова S в введённых N строках.
# a = str(input())
# b = int(input())
# count = 0
# while b != 0:
#     c = str(input())
#     b -= 1
#     count = count + c.count(a)
# print(count)

# Редакторы новостного портала создают заголовки для статей сайта. Напишите программу,
# которая сокращает длинные заголовки до требуемой длины и завершает их многоточием …
# при необходимости. На вход программе поступают два натуральных числа – необходимая
# длина заголовка и количество заголовков N, которые требуется сократить. В каждой из
# последующих N строк записано по одному заголовку.
# a = int(input())
# b = int(input())
# while b != 0:
#     c = str(input())
#     if len(c) <= 17:
#         print(c)
#     else:
#         for i in range(0, a-3):
#             print(c[i], end="")
#         print('...')
#     b -= 1


# HOMEWORK 14.11
# На вход программе поступает последовательность целых чисел, оканчивающиеся нулём
# (0 не входит в последовательность), программа должна вывести список, элементы
# которого отсортированы по убыванию их абсолютного значения (то есть несмотря на знак).
# b = []
# d = []
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     b.append(a)
#     d.append(a)
# c = []
# for y in b:
#     for i in d:
#         if abs(i) <= abs(y):
#             minb = i
#         c.append(minb)
#     d.remove(minb)
# print(c)
# На вход программе поступает последовательность целых чисел, оканчивающиеся нулём
# (0 не входит в последовательность). Введённые числа образуют список. Выведите на экран:
# количество всех элементов в списке, количество единиц в списке, индекс первого вхождения единицы в список.
# b = []
# c = 9999999999999999
# d = 0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     b.append(a)
# for i in range(len(b)):
#     if b[i] == 1:
#         if i < c:
#             c = i
#         d += 1
# print("Count all ", len(b))
# print("Count of 1 ", d)
# print("First 1 ", c)

#Дан список целых чисел, необходимо удалить все вхождения числа 17 в него и вывести его на экран.
# b = []
# count = 0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     b.append(a)
#     if a == 17:
#         count += 1
# for i in range(count):
#     b.remove(17)
# print(b)

# Напишите программу, которая возводит в заданную степень все числа, что передали пользователи.
# На вход программе поступает натуральная степень, количество строк N и сами N чисел.
# a = int(input())
# b = int(input())
# d = []
# for i in range(b):
#     c = int(input())
#     d.append(c)
# for i in range(len(d)):
#     print(d[i]**3)


# HOMEWORK 15.11

#Напишите функцию lenght, которая принимает одно целое число и возвращает его длину без учёта знака.
def lenght(n):
    x = 1
    k = 1
    if abs(n) < x:
        return 1
    if abs(n) > x:
        x *= 10
        k += 1
    else:
        return k

    for i in range():
        if n
            BLYA UBEYTE MENYA
            ;(




print(1%10)
print(1//10)
            