# 作者: 王道 龙哥
# 2024年12月30日11时00分35秒
# xxx@qq.com
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # 子类对象调用父亲的init
        self.color = color

    def bark(self):
        print(f'{self.name}汪汪叫{self.color}--')

    def run(self):
        super().run()
        print(f'{self.name}跑的快')


class XiaoTianQuan(Dog):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age

    def fly(self):
        print(f'{self.name}飞天--{self.color}--{self.age}')


if __name__ == '__main__':
    wangcai = Dog('旺财', '黄色')
    wangcai.bark()
    wangcai.run()
    xiaotianquan = XiaoTianQuan('哮天犬', '黑色', 20)
    xiaotianquan.fly()
