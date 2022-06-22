# есть вот такой файл с email, ваша задача записать в новый текстовый файл только почты от gmail.com

# try:
#     with open('emails.txt') as file:
#         for line in file.readlines():
#             if 'gmail.com' in line:
#                 with open('gmails.txt', 'a') as file2:
#                     file2.write(line)
#
# except Exception as err:
#     print(err)
# finally:
#     file.close()
#     file2.close()


# 2) для хранения и чтения данных использовать файлы
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

#
# while True:
#     input_msg = input(
#         f'{"*" * 10}\nPlease type in one of the following:\nCreate\nGetAll\nShoppingSum\nMostExpensive\nName of '
#         f'purchase '
#         'you want to find\nClose\n').lower()
#
#     if input_msg == 'create':
#         name = input('Name of the purchase: ')
#         price = input('Price of the purchase: ')
#         try:
#             with open('shopping_list.txt', 'a') as file_append:
#                 file_append.write(f'{name} {price}'+'\n')
#         except Exception as err:
#             print(err)
#         finally:
#             file_append.close()
#     elif input_msg == 'getall':
#         try:
#             with open('shopping_list.txt') as file_read:
#                 print(file_read.read())
#         except Exception as err:
#             print(err)
#         finally:
#             file_read.close()
#     elif input_msg == 'shoppingsum':
#         prices = []
#         try:
#             with open('shopping_list.txt') as file_sum:
#                 for l in file_sum.read():
#                     if l.isdigit():
#                         prices.append(l)
#                     else:
#                         prices.append(' ')
#             prices_s = ' '.join(''.join(prices).split()).split()
#             print(sum(list(map(int, prices_s))))
#             # print(sum([int(i) for i in prices_s]))
#         except Exception as err:
#             print(err)
#         finally:
#             file_sum.close()
#
#     elif input_msg == 'mostexpensive':
#         prices = []
#         try:
#             with open('shopping_list.txt') as file_me:
#                 for l in file_me.read():
#                     if l.isdigit():
#                         prices.append(l)
#                     else:
#                         prices.append(' ')
#             prices_s = ' '.join(''.join(prices).split()).split()
#             with open('shopping_list.txt') as file_me:
#                 for line in file_me.readlines():
#                     if str(max([int(i) for i in prices_s])) in line:
#                         print(line)
#         except Exception as err:
#             print(err)
#         finally:
#             file_me.close()
#     elif input_msg == 'close':
#         break
#     else:
#         try:
#             with open('shopping_list.txt') as file_read:
#                 for line in file_read.readlines():
#                     if input_msg in line:
#                         print(line)
#         except Exception as err:
#             print(err)
#         finally:
#             file_read.close()

def create_purchase():
    name = input('Name of the purchase: ')
    price = input('Price of the purchase: ')
    try:
        with open('shopping_list.txt', 'a') as file_append:
            file_append.write(f'{name} {price}' + '\n')
    except Exception as err:
        print(err)
    finally:
        file_append.close()


def get_all():
    try:
        with open('shopping_list.txt') as file_read:
            print(file_read.read())
    except Exception as err:
        print(err)
    finally:
        file_read.close()


def shopping_list():
    while True:
        input_msg = input(
            f'{"*" * 10}\nPlease type in one of the following:\nCreate\nGetAll\nClose\n').lower()
        if input_msg == 'create':
            create_purchase()
        elif input_msg == 'getall':
            get_all()
        elif input_msg == 'close':
            break


shopping_list()
