# import random

# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# sum = 0
# for x in range(0, 101, 2):
#     sum += x
# print(sum)


# answer = random.randint(1, 100)
# hit = False
# counter = 0
# while(not hit):
#     counter += 1
#     userInput = int(input('猜数字: '))
#     if(userInput == answer):
#         hit = True
#     if(userInput < answer):
#         print('小了')
#     else:
#         print('大了')
# print('猜中了, 用了%d次' % counter)


# x = 100
# while(x < 1000):
#     hundred = x // 100
#     ten = x // 10 % 10
#     single = x % 10
#     num = hundred ** 3 + ten ** 3 + single ** 3
#     if (num == x):
#         break
#     x += 1
# print(x)

x = 1
y = 1
print(x)
print(y)
for i in range(3, 21):
    sum = x + y
    print(sum)
    x = y
    y = sum

