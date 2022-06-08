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
# list = [s for s in st]
# list2=[i for i in list if i.isdigit() or i == ' ']
#
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
