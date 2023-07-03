# python的函数支持定义参数的默认值

import random

def roll(n = 2):
    total = 0
    for _ in range(n):
        total += random.randint(1, 6)
    return total


# 可变参数
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

# 模块： python中每个py文件就是一个模块，这样可以在不同模块中使用相同的函数名


# 变量作用域
# a是全局变量
# b和c都是局部变量

# 下面的代码能够顺利的执行并且打印出100、hello和True，但我们注意到了，
# 在bar函数的内部并没有定义a和b两个变量，那么a和b是从哪里来的。
# 我们在上面代码的if分支中定义了一个变量a，这是一个全局变量（global variable），
# 属于全局作用域，因为它没有定义在任何一个函数中。在上面的foo函数中我们定义了变量b，
# 这是一个定义在函数中的局部变量（local variable），属于局部作用域，在foo函数的外部并不能访问到它；
# 但对于foo函数内部的bar函数来说，变量b属于嵌套作用域，在bar函数中我们是可以访问到它的。
# bar函数中的变量c属于局部作用域，在bar函数之外是无法访问的。
# 事实上，Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，
# 前三者我们在上面的代码中已经看到了，所谓的“内置作用域”就是Python内置的那些标识符，我们之前用过的input、print、int等都属于内置作用域。


# 局部作用域 -》 嵌套作用域 -》 全局作用域 -》 内置作用域

def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b) # 这里的b对于bar函数来说就是嵌套作用域
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()

# 如何修改全局变量
def foo():
    global a # 必须要声明为全局变量， 不然就会认为是函数内部的一个新的局部变量， 虽然和外面的a同名
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200

# global关键字来指示foo函数中的变量a来自于全局作用域，如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域。
# 同理，如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域