a = 76
b = 3.14
c = 'hello world'
d = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(len("Maksim"))
print(c[1:2:1])
name = "Maxim"
print(name, "!", sep=" ")   #defolt
print(name, "!", end="\n")  #defolt
print(name, "!", end="")
print("Hello\nZabik\nMaks")
for i in range(0, 5, 2):        # от 0 до 5 с шагом 2
    if i % 2 == 0: continue # пропуск хода при выполнении условия
    print(i)
t = tuple()     # кортеж
p = ("word", 3, True, 3.21)
m = {}      # множество без повторений
e = {4, True, "word", 4}
print(e)     # выводит только оригинальные значения
f = set()
m = {1, 2, 3, 4}
n = {3, 4, 5}
print(m|n, m&n)
print(3 in m)
print(sum(m))
print(len(m))
m.add(6)
m.remove(2)
g = {1: "january", 2:"february"}     # словари
h = dict()
i = {"a": 25, "b": 56}
g[3] = ("march")
a = ["abc", 3, 3.14, True, 1, 2]    # список
a.append(0)     # добавляем одно
a.extend(list("abc"))   # добавляет сразу несколько
a.remove(1)     # удаляет только одну единицу
del a[1]    # удаляет по индексу
a.clear()   # очищение списка
a.sort()    # сортировка по возрастанию
a.sort(reverse=True)    # сортировка по убыванию
a.append(input())   # добавляем через ввод в консоль
print(max(a), min(a), sum(a), len(a), 1 in a, a*3, a.count(2), sorted(a), sorted(a, reverse=True))

