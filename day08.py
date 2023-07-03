# class Student(object):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def study(self, course):
#         print('%s正在学习: %s' % (self.name, course))

#     def watchMovie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s正在观看岛国爱情大电影.' % self.name)

# if __name__ == '__main__':
#     stu1 = Student('nick', 30)
#     stu1.study('haha')
#     stu1.watchMovie()
from time import sleep

class Clock(object):

    def __init__(self, hour, minute, second) -> None:
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        print(f'{self._hour} : {self._minute} : {self._second}')


if __name__ == '__main__':
    clk = Clock(11, 12, 13)
    while(True):
        clk.run()
        clk.show()
        sleep(1)
