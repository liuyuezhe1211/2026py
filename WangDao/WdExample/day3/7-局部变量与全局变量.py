# 作者: 王道 龙哥
# 2024年12月26日14时44分21秒
# xxx@qq.com

# 1、执行到需要全局变量时，全局变量必须被定义了
# 2、就近原则

def demo1():
    global num
    print(num)
    num = 2
    print(f'demo1函数里边 修改后{num}')


num = 10
print(f'函数调用前{id(num)}')
demo1()
print(f'函数调用后{num}，地址{id(num)}')
