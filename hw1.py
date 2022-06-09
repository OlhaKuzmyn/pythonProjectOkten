# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
# # 1 way
# ls = []
# for s in st:
#     if s.isdigit():
#         ls.append(int(s))
# print(ls)
# # 2 way
# l = [int(s) for s in st if s.isdigit()]
# print(l)

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
#
# list2=[i for i in st if i.isdigit() or i == ' ']
# print(list2)
# #
# notList = ((''.join(list2)).strip()).split()
# n = ','.join(notList)
# print(notList)
# print(n)


# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# gList = [s for s in greeting.upper()]
# print(gList)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# l = [i**2 for i in range(0,51) if i%2!=0]
# print(l)


# function
#
# - створити функцію яка виводить ліст

# def func ():
#     l = []
#     return l
#
# print(func())

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def func(a, b, c):
#     if b > a < c:
#         return a
#     elif a > b < c:
#         return b
#     elif a > c < b:
#         return c

# print(func(4, 10, 6))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def func(a, b, c):
#     if b < a > c:
#         return a
#     elif a < b > c:
#         return b
#     elif a < c > b:
#         return c
#
# print(func(11, 10, 20))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def func(*args):
#     print(max(args))
#     return min(args)
#
# print(func(11, 10, 20,25))

# - створити функцію яка повертає найбільше число з ліста

# l= [11, 45, 20,25, 30]
# def func(l):
#     return max(l)
# print(func(l))

# - створити функцію яка повертає найменьше число з ліста

# l= [11, 45, 5,25, 30]
# def func(l):
#     return min(l)
# print(func(l))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# l= [11, 45, 5,25, 30]
# def func(l):
#     return sum(l)
# print(func(l))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# l= [11, 45, 5,25, 30]
# def func(l):
#     return sum(l)/len(l)
# print(func(l))

# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"
#       0   1 2 3 4 5  6   7  8 9
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# # print(min(list))
# # print(set(list))
#
# list[::4] = ['X']*len(list[::4])
# print(list)

# the rest to this task dont work
# n=4
# #
# l = [[v if i!=3 and 0<i%i!=4 else 'X' for i,v in enumerate(list)] for n in list]
# print(l)

# for i, v in enumerate(list):
#     if i==3:
#         list[i] = 'X'
#     elif i+4:
#         list[i] = 'X'
# if i%i==4:
#     list[i]='X'



# n=3
# ln = len(list)-1
# # print(ln)
# for i, v in enumerate(list):
#     while i!=ln:
#         if i==n:
#             list[i] = 'x'
#     n+=4
#
# print(list)


# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# l = [n='*' for n in [i for i in range(0,11)]]
# l=[]
# b = []
# for i in range(0,10):
#     if i==0 or i==9:
#         b.append('*')
#     else:
#         b.append(' ')
#     l.append('*')
#
# b_s = ''.join(b)+'\n'
#
# print(f"{''.join(l)}\n{(b_s)*10}{''.join(l)}")

# print(l,b)










# saw the soution online
# 3) вывести табличку умножения с помощью цикла while


# c=1
# while c<10:
#     print('')
#     x = 1
#     while x<10:
#         print(c*x , end='\t')
#         x+=1
#     c+=1


# y = 1
# while y <= 12:
#      print('')
#      print(y,end='\t')
#      z = 1
#      while z <= 12:
#           print(y*z ,end='\t')
#           z += 1
#      y += 1

# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j)



# 4) переделать первое задание под меню с помощью цикла
# ??