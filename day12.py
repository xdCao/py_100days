import re


def test_qq():
    username = input('请输入用户名：')
    qq = input('请输入qq号：')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', qq)
    if not m1:
        print('请输入正确的用户名')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的qq号')
    if m1 and m2:
        print('success')


def test_mobile():
    pattern = re.compile(r'1[34578]\d{9}')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    my_list = re.findall(pattern, sentence)
    print(my_list)
    print('--------------------------------')
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------------------------------')
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


def test_sensitive():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)


def test_split():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == '__main__':
    # test_qq()
    # test_mobile()
    # test_sensitive()
    test_split()
