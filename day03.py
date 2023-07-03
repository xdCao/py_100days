# username = input('请输入用户名： ')
# password = input('请输入密码： ')
# if username == 'admin' and password == '123456':
#     print('身份验证成功')
# else:
#     print('身份验证失败')


x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('Function(%.2f) = %.2f' % (x, y))


