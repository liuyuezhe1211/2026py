# 作者: 王道 龙哥
# 2024年12月26日10时51分47秒
# xxx@qq.com


def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")


def sum_2_num(num1, num2):
    """
    num1和num2是形参,类似于函数内的局部变量
    :param num1:
    :param num2:
    :return:
    """
    result = num1 + num2
    print(f'求和结果{result}')
    return result


# print('执行函数前')
# say_hello()
# print('执行函数后')
ret = sum_2_num('abc', 'efg')  # 3和5是实参
print(ret)
