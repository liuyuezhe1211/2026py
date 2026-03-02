# 作者: 王道 龙哥
# 2024年12月30日14时36分56秒
# xxx@qq.com

# 多态：同一条指令，不同的对象，产生的行为是不一样的
class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog: Dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        dog.game()  # 多态


if __name__ == '__main__':
    zhangsan = Person('张三')
    wangcai = Dog('旺财')
    zhangsan.game_with_dog(wangcai)
    xiaotianquan=XiaoTianDog('哮天犬')
    zhangsan.game_with_dog(xiaotianquan)