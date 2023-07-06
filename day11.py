import json

import requests


def read_file():
    f = None
    try:
        f = open('test.txt', 'r', encoding='utf-8')
        print(f.read())
        f = open('test.txt', 'r', encoding='utf-8')
        for line in f:
            print(line, end='')
        print()
        f = open('test.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        print(lines)
    except FileNotFoundError:
        print('找不到文件')
    except LookupError:
        print('未知编码')
    except UnicodeDecodeError:
        print('编码错误')
    finally:
        f.close()


def write_file(content):
    try:
        with open('test.txt', 'a', encoding='utf-8') as f:
            f.write(content)
    except IOError as ex:
        print(ex)


def copy_pic(path):
    with open(path + '.jpeg', 'rb') as f:
        byte_data = f.read()
    with open(path + 'copy' + '.jpeg', 'wb') as f:
        f.write(byte_data)


def dump_api_json():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_obj = json.loads(resp.text)
    print(data_obj)
    with open('json.json', 'w', encoding='utf-8') as f:
        json.dump(data_obj, f)
    with open('json.json', 'r', encoding='utf-8') as f:
        load_data = json.load(f)
        print(load_data)


if __name__ == '__main__':
    # read_file()
    # write_file('testWrite\n')
    # read_file()
    # copy_pic('luffy')
    dump_api_json()
