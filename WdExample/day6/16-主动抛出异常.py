# 作者: 王道 龙哥
# 2024年12月30日16时52分14秒
# xxx@qq.com
def input_password():

    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    raise Exception("密码长度必须大于等于8位！")

if __name__ == '__main__':
    # try:
    #     print(input_password())
    # except Exception as result:
    #     print(result)
    try:
        assert 1==1,'你的程序在这里发生了什么xxxx异常'
    except Exception as e:
        print(e)
    while True:
        pass