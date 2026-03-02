# 作者: 王道 龙哥
# 2024年12月26日16时10分28秒
# xxx@qq.com

my_list = [x for x in range(10)]

print(my_list)

# 2个for循环
a = [j for i in range(10) for j in range(i)]
print(a)
# 二维列表
a = [[col * row for col in range(5)] for row in range(5)]
print(a)
# print(a[1][2])
# 二维转一维
b = [j for x in a for j in x]
print(b)

# 使用if
c = [x for x in range(10) if x % 2 == 0]
print(c)

# 使用if else
d = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(d)
