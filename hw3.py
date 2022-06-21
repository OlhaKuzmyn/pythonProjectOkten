# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон


# class Shape:
#     def area(self):
#

# class Rectangle:
#     def __init__(self, x, y):
#         self.area = x * y
#         self.y = y
#         self.x = x
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return self.area - other.area
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.area < other.area
#
#     def __gt__(self, other):
#         return self.area > other.area
#
#     def __len__(self):
#         return self.x + self.y
#
#
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(10, 20)
#
# print(rect1 + rect2)
# print(rect1 - rect2)
# print(rect1 == rect2)
# print(rect1 != rect2)
# print(rect1 < rect2)
# print(rect1 > rect2)
# print(rect1.__len__())
# print(rect2.__len__())


# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество


# from typing import List
#
#
# class Human:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#         Cinderella.count += 1
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return self.__str__()
#
#     # @classmethod
#     # def inc_count(cls):
#     #     cls.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#
# class Prince(Human):
#     def __init__(self, name, age, found_shoe_size):
#         super().__init__(name, age)
#         self.found_shoe_size = found_shoe_size
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __eq__(self, other):
#         for o in other:
#             if o.shoe_size == self.found_shoe_size:
#                 return f'Cinderella {o.name} {o.get_count}'
#
#
# cinderellas: List[Cinderella] = [Cinderella('Christina', 22, 38), Cinderella('Gina', 21, 37),
#                                  Cinderella('Nina', 20, 36), Cinderella('Cinderella', 20, 35)]
# prince = Prince('Prince', 21, 35)
#
# print(cinderellas)
# for c in cinderellas:
#     print(c.get_count())
# print(prince)
# print(prince == cinderellas)


