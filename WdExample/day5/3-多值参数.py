# 作者: 王道 龙哥
# 2024年12月28日09时40分34秒
# xxx@qq.com

# 多值参数，就是参数个数不确定，必须是下面的写法

def demo2(*args, **kwargs):
    print(f'demo2-{args}')
    print(f'demo2-{kwargs}')


def demo(*args, **kwargs):
    # print(num)
    print(args)
    print(kwargs)
    demo2(*args,**kwargs)


demo(1, 2, 3, 4, name='小明', age=19)
