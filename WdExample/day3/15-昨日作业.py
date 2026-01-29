# 作者: 王道 龙哥
# 2024年12月26日16时47分53秒
# xxx@qq.com

def homework4():
    """
    实现从1到100之间的奇数求和
    :return:
    """
    print(sum([x for x in range(101) if x % 2 == 1]))


def homework5():
    """
    九九乘法表
    :return:
    """
    for i in range(1, 10):  # 外层控制行
        for j in range(1, i + 1):  # 内层控制列
            print(f'{j}*{i}={j * i:2}', end=' ')
        print()


def homework6():
    """
    统计1的个数
    :return:
    """
    s = int(input('请输入一个整数'))
    if s >= 0:
        # 正数补码=正数原码
        num = bin(s).count('1')
    else:
        # 对于负数
        num = 64 - bin(~s).count('1')
    print(num)


def homework6_2():
    """
    位运算实现,64位是为了做题做的限制
    :return:
    """
    s = int(input('请输入一个整数'))
    check_bit_flag = 1
    count = 0  # 统计数目
    while check_bit_flag < 2 ** 64:
        if check_bit_flag & s:
            count += 1
        check_bit_flag <<= 1
    print(count)


if __name__ == '__main__':
    # homework4()
    # homework5()
    # homework6()
    homework6_2()
