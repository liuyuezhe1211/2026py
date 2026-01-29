# 作者: 王道 龙哥
# 2024年12月30日09时14分08秒
# xxx@qq.com

class Cat(object):
    """这是一个猫类"""

    def __init__(self, new_name):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")

    def __del__(self):
        print(f'{self.name}对象被销毁')

    def __str__(self):
        """
        对象的描述信息
        :return:
        """
        return f'对象{self.name}'

def main():

    tom = Cat('Tom')
    tom.drink()
    tom.eat()

    lazy_cat = Cat('懒猫')
    print(tom is lazy_cat)
    # tom.name = 'Tom'  #不规范的编程，不要在类外面给对象增加属性
    print(tom.name)
    print('-'*50)
    print(tom)


if __name__ == '__main__':
    main()
    print('程序结束')
