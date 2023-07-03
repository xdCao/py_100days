a = 100
b = 12.3
c = 1 + 5j
d = 'hello world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

# 类型转换
print('类型转换')
a = 1.2
print(type(a))
a = int(a)
print(type(a))

# 华氏度转摄氏度
f = float(input('华氏度 = '))
c = (f - 32) / 1.8