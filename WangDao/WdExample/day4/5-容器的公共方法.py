# 作者: 王道 龙哥
# 2024年12月27日15时25分43秒
# xxx@qq.com

def list_set_slice():
    test_list = [1, 2, 3, 4, 5, 6]
    test_list[3:3] = ['x', 'y', 'z']  # 往列表中插入一个列表
    print(test_list)


def list_compare():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)
    print(a is b)  # is运算符是判断两个对象的地址是否一致的，一致是True


def use_method():
    """
    容器的一些方法
    :return:
    """
    a = (1, 2, 3)
    b = ('a', 'b', 'c')

    print(list(zip(a, b)))
    print(dict(zip(b, a)))
    # 如何使用enumerate
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list2=list(enumerate(seasons))
    print(list2)
    my_dict=dict(list2)
    print({v:k for k,v in my_dict.items()})


if __name__ == '__main__':
    # list_compare()
    use_method()
