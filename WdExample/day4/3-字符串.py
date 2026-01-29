# 作者: 王道 龙哥
# 2024年12月27日11时00分54秒
# xxx@qq.com

def check_type():
    """
    判断字符串类型
    :return:
    """
    s1 = 'abc*'
    print(s1.isalnum())
    s2 = '123'
    print(s2.isdecimal())


def str_find():
    """
    字符串查找与替换
    :return:
    """
    s1 = 'abcdefgcdef'
    print(s1.find('cd', 4))  # 返回找到字符串的起始下标
    s2 = s1.replace('cd', 'CD', 1)  # 第三个参数是控制替换次数的
    print(s2)


def str_split_join():
    """
    分割与连接
    :return:
    """
    s1 = 'abc bcd 我很帅'
    print(s1.split())
    s1 = 'abc,bcd,我很帅'
    print(s1.split(','))
    s2 = 'abc\nbcd\nefg'
    print(s2.splitlines())

    print('-' * 50)
    s3 = 'abc\r\nbcd\r\nefg'
    print(s3.splitlines(True))
    print('-' * 50)
    str_list = ['a', 'b', 'c', 'd']
    print(','.join(str_list))


def study_r():
    """
    \r和\n区别
    :return:
    """
    s = 'abc\r\nd'
    print(s)


def str_slice():
    """
    字符串的切片
    :return:
    """
    num_str = "0123456789"
    # 1. 截取从 2 ~ 5 位置 的字符串
    print(num_str[2:6])

    # 2. 截取从 2 ~ `末尾` 的字符串
    print(num_str[2:])

    # 3. 截取从 `开始` ~ 5 位置 的字符串
    print(num_str[:6])

    # 4. 截取完整的字符串
    print(num_str[:])

    # 5. 从开始位置，每隔一个字符截取字符串
    print(num_str[::2])

    # 6. 从索引 1 开始，每隔一个取一个
    print(num_str[1::2])

    # 倒序切片
    # -1 表示倒数第一个字符
    print(num_str[-1])

    # 7. 截取从 2 ~ `末尾 - 1` 的字符串
    print(num_str[2:-1])

    # 8. 截取字符串末尾两个字符
    print(num_str[-2:])

    # 9. 字符串的逆序（面试题）
    print(num_str[::-1])


def list_slice():
    my_list = list("0123456789")
    print(my_list)
    print(my_list[2:6])


def index_count():
    hello_str = "heallo hello"

    # 1. 统计字符串长度
    print(len(hello_str))

    # 2. 统计某一个小（子）字符串出现的次数
    print(hello_str.count("llo"))
    print(hello_str.count("abc"))

    # 3. 某一个子字符串出现的位置
    print(hello_str.index("llo"))
    # 注意：如果使用index方法传递的子字符串不存在，程序会报错！
    # print(hello_str.index("abc"))

if __name__ == '__main__':
    # check_type()
    # str_find()
    # str_split_join()
    # study_r()
    # str_slice()
    # list_slice()
    index_count()