# 作者: 王道 龙哥
# 2024年12月27日16时09分50秒
# xxx@qq.com
def measure():
    """
    掌握返回多个值时，如何去处理
    :return:
    """

    print("开始测量...")
    temp = 39
    wetness = 10
    print("测量结束...")

    return temp, wetness


ret1 = measure()
print(ret1)
a=10
b=5
a,b=b,a
print(a,b)