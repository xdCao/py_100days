# @property, setter
# __slots__用来限定对象只能绑定某些属性


# class Person(object):

#     __slots__ = ('_name', '_gender', '_age')

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print(f'{self._name}正在玩飞行棋')
#         else:
#             print(f'{self._name}正在玩斗地主')

# if __name__ == '__main__':
#     person = Person('大锤', 12)
#     person.play()
#     person.age = 32
#     person.play()
#     person._gender = 1
#     person._isGay = 2


# from math import sqrt


# class Triangle(object):

#     def __init__(self, a, b, c) -> None:
#         self._a = a
#         self._b = b
#         self._c = c

#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b

#     def perimeter(self):
#         return self._a + self._b + self._c

#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) *
#                     (half - self._b) * (half - self._c))


# if __name__ == '__main__':
#     a, b, c = 3, 4, 5
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         print(t.area())
#     else:
#         print('无法构成三角形')


# from time import time, localtime, sleep


# class Clock(object):

#     def __init__(self, hour, minute, second) -> None:
#         self._hour = hour
#         self._minute = minute
#         self._second = second

#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0

#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)


# def main():
#     # 通过类方法创建对象并获取系统时间
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()


# if __name__ == '__main__':
#     main()


# 类的继承

from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):

    def __init__(self, nick):
        self._nickname = nick

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print('wangwang' + self._nickname)


class Cat(Pet):

    def make_voice(self):
        print('miaomiao' + self._nickname)


def main():
    pets = [Dog('gou'), Cat('mao')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
