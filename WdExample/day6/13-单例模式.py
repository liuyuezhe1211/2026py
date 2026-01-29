# 作者: 王道 龙哥
# 2024年12月30日15时25分24秒
# xxx@qq.com
class MusicPlayer(object):
    instance = None  # 用来保存对象的

    def __new__(cls, *args, **kwargs):
        # 1、创建对象，分配空间
        if cls.instance is None:
            cls.instance=super().__new__(cls)  #父亲的new类似于C的malloc
        return cls.instance

    def __init__(self,name):
        self.name=name

if __name__ == '__main__':
    player1 = MusicPlayer('七里香')
    player2 = MusicPlayer('东风破')
    print(id(player1))
    print(id(player2))
    print(player1.name)
    print(player2.name)