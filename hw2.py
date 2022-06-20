# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все

# def todolist(todo):
#     tdlist = []
#
#     def add(todo):
#         nonlocal tdlist
#         tdlist.append(todo)
#         return ', '.join(tdlist)
#
#     return add
#
#
# tasks = todolist('')
# # print(tasks('cleanup'))
# tasks('cleanup')
# # print(tasks('pyhon hw'))
# tasks('pyhon hw')
# # print(tasks('watch a movie'))
# tasks('watch a movie')
# # print(tasks('go for a walk'))
# tasks('go for a walk')
# print(tasks('cook dinner'))


# 2) протипизировать первое задание

# from typing import Callable
#
#
# def todolist(todo: str) -> Callable[[str], str]:
#     tdlist: list = []
#
#     def add(todo):
#         nonlocal tdlist
#         tdlist.append(todo)
#         return ', '.join(tdlist)
#
#     return add
#
#
# tasks = todolist('')
#
# tasks('cleanup')
# tasks('python hw')
# tasks('watch a movie')
# tasks('go for a walk')
# print(tasks('cook dinner'))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)

# num = 7000
# print(len(str(num)))

#
# def expanded_form(num):
#     strNum = str(num)
#     lng = len(strNum)
# num = 70304
# strNum = str(num)
# lng = len(strNum)
# lastN = str(strNum[-1])
# last = int(strNum[-1])
# print(last)
# revN = strNum[::-1]
# lsN = strNum.split('0')
# lN=[]
# for n in lsN:
#     if lsN.index(n) == len(lsN)-1 and n.isdigit():
#         lN.append(n)
#     elif len(n)==1:
#         nMz= n + '0' * ((lsN.index(n) * 2) - 2)
#         lN.append(nMz)
#
# print(lN)
# print(lng)
# print(lsN)
# biggestN = lsN[0] + '0'*(lng - 1)
# print(biggestN)


# создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функции

# def decor(func):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(f"{'*' * 10}\n{count}")
#
#     return inner
#
#
# @decor
# def func1():
#     print('func1')
#
# @decor
# def func2():
#     print('func2')
#
#
# func1()
# func1()
# func1()
# func1()
# func2()
# func1()
# func2()

# сделайте функцию на замыкания которая будет возвращать декоратор который будет считать
# общее количество запущенных  функций декорированных этим декоратором

# g_count = 0
#
#
# def decor2(func):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         global g_count
#         g_count += 1
#         print(f"{'*' * 10}\n{count}\n{g_count}")
#
#     return inner
#
#
# @decor2
# def func1():
#     print('func1')
#
#
# @decor2
# def func2():
#     print('func2')
#
#
# func1()
# func1()
# func1()
# func1()
# func2()
# func1()
# func2()


# some solutions i found online :

# from functools import wraps
#
#
# def count_check(function, count = {}):
#
#     count[function] = 0
#
#     @wraps(function)
#     def increase_count(*args, **kwargs):
#         count[function] += 1
#         return function(*args, **kwargs), count[function], sum(count.values())
#
#     return increase_count


# @count_check
# def foo():
#     return 42
#
#
# print(foo(), foo(), foo())
#
#
# @count_check
# def bar():
#     return 23
#
#
# print(bar(), bar(), bar())
# print(foo(), foo(), foo())


# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
# (число з послідовності - це сума попередніх двох чисел)

# def fibb():
#     n = input('2 numbers: ')
#     x = int(n[-1]) + int(n[0])
#     l = []
#     l.append(x)
#     while x <= 100:
#         l.append(x)
#         x += l[-2]
#     print(l)
#
# fibb()


# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3


# def even_odd(num):
#     s = str(num)
#     lEven = []
#     for i in s:
#         if int(i) % 2 == 0:
#             lEven.append(i)
#     print(f"Evens: {len(lEven)} Odds: {len(s) - len(lEven)}")
#
# even_odd(225688)
# even_odd(33294)

# прога, що виводить кількість кожного символа з введеної строки,
#   наприклад:
#   st = 'as 23 fdfdg544' #введена строка
#
#   'a' -> 1  #вивело в консолі
#   's' -> 1
#   ' ' -> 2
#   '2' -> 1
#   '3' -> 1
#   'f' -> 2
#   'd' -> 2
#   'g' -> 1
#   '5' -> 1
#   '4' -> 2


# def duplicates(st):
#     l = [i for i in st]
#     dic = {x: l.count(x) for x in l}
#     for key in dic:
#         print(f"'{key}':{dic[key]}")
#
# duplicates('as 23 fdfdg544')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
#
# l_odds = [i for i in range(20) if i%2!=0]
# c = 1
# lst=[]
# while c<=4:
#     for n in range(0, 20, c):
#         if n%2!=0:
#             lst.append([n])
#     # print([[i for i in range(20) if i%2!=0] for n in range(0, 20, c)])
#     c+=1
#         # lst.append()
# print(lst)
# print(l_odds)

i_list = range(0,84)
r = 21
res = [i_list[i:i+r] for i in range(0,len(i_list),r)]
