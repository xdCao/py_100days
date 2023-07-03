s1 = 'hello world'
s2 = "hello world"
s3 = """
hello 
world
"""
# 三个单引号的可以换行

print(s1, s2, s3)

# 转义
s1 = '\'hello, world\''
print(s1)

# 如果不希望字符串中的\表示转义， 可以在字符串最前面加上r
s1 = r'\'hello, world\''
print(s1)

# 可以使用+来实现字符串拼接
# 可以使用*来重复一个字符串的内容
# 可以使用in 和not in来判断一个字符串是否包含另外一个字符串
# 可以使用[]和[:]从字符串中取出某个字符或某些字符

s1 = 'hello' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)

s2 = 'abc123456'
print(s2[2])
print(s2[2:])
print(s2[2:5])
print(s2[2::2])
print(s2[::-1])
print(s2[-3:-1])
print(s2[-3::-1])


s1 = 'hello world'
print(len(s1)) # 长度
print(s1.capitalize()) # 首字母大写
print(s1.title()) # 每个单词首字母大写
print(s1.upper()) # 整体大写
print(s1.find('shit')) # 找子串
# print(s1.index('shit')) # 找子串, 找不到抛异常
print(s1.startswith('he'))
print(s1.endswith('ld'))
print(s1.center(50, '*')) # 以指定宽度居中并在两侧填充字符
print(s1.rjust(50, '*')) # 以指定宽度靠右防止并在左侧填充字符

s1 = 'abc123'
print(s1.isdigit()) # 判断是否为数字
print(s1.isalpha()) # 判断是否为纯字母
print(s1.isalnum()) # 判断是否是字母+数字

s1 = '  222@qq.com   '
print(s1.strip()) # 获取去除两侧空格后的拷贝

# 格式化
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} + {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')



# 列表
list1 = [1, 3, 5, 7, 100]
print(list1)
list2 = ['hello'] * 3
print(list2)
print(len(list1))
print(list1[0])
print(list1[-1])
list1[2] = 300
print(list1)

# 遍历列表元素, 三种方式
for index in range(len(list1)):
    print(list1[index])

for ele in list1:
    print(ele)

for index, ele in enumerate(list1):
    print('index = {0}, ele = {1}'.format(index, ele))

list1.append(1000)
list1.insert(1, 400)
list1.extend([2000, 3000])
list1 += [4000, 5000]
print(list1)

if 5000 in list1:
    list1.remove(5000)
print(list1)

list1.pop(0)
print(list1)

list1.clear()
print(list1)

list1 = [1, 5, 7, 6, 4, 3, 2]
print(sorted(list1))
print(sorted(list1, reverse=True))


list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print(sorted(list1, key=len))

# 生成列表
f = [x for x in range(1, 11)]
print(f)
f = [x + y for x in range(1, 11) for y in range(1, 11)]
print(f)
f = [x ** 2 for x in range(1, 10)]
print(f)
import sys
print(sys.getsizeof(f)) # 查看占用的字节数

# yield生成器

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

for ele in fibonacci(10):
    print(ele)


# 元组， 元组和列表的主要区别在于： 元组的元素不能修改
t = ('caohao', 38, True, '杭州')
print(t)
print(t[0])
for ele in t:
    print(ele)

# t[0] = '大锤' # 这一行会抛异常，因为元组的值不能修改
person = list(t) # 元组转列表
print(person)
person[0] = '李小龙'
print(person)

tuple1 = tuple(person) # 列表转元组
print(tuple1)

# 集合
set1 = {1, 2, 3, 4, 5 ,6}
print(set1)
print('Length = ', len(set1))
set2 = set(range(1, 10))
set3 = set((1, 3, 5))
print(set2)
print(set3)
set4 = {num for num in range(1, 100) if num % 3 == 0}
print(set4)

set1.add(7)
print(set1)
set1.update([11, 12])
print(set1)
set1.discard(5)
print(set1)
set1.remove(4)
print(set1)
set1.pop()
print(set1)

print('set1 = ', set1)
print('set2 = ', set2)
# 交集
print(set1 & set2)
# 并集
print(set1 | set2)
# 差集
print(set1 - set2)
# 对称差
print(set1 ^ set2)

# 判断子集
print(set1 <= set2)
# 判断超集
print(set1 >= set2)

# 字典
scores = {'a' : 90, 'b': 80, 'c': 70}
print(scores)
# 创建字典
dict1 = dict(one = 1, two = 2, three = 3)
# 使用zip函数将两个序列压成字典
dict2 = dict(zip(['a', 'b', 'c'], 'abc'))
print(dict1)
print(dict2)
print(dict1['one'])
# 遍历字典值
for keys in scores:
    print(f'{keys} : {scores[keys]}')

scores['haha'] = 100
print(scores)
scores.update(bbb=99, caohao=10000)
print(scores)
print(scores.get('caohao'))

# 删除元素
print(scores.popitem())
print(scores.pop('bbb'))
print(scores)
scores.clear()
print(scores)