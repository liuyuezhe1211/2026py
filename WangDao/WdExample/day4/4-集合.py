# 作者: 王道 龙哥
# 2024年12月27日14时31分18秒
# xxx@qq.com

def use_set():
    set1 = set()  # 定义一个空集合
    print(type(set1))

    set2 = {1, 2, 3, 4, 5}  # 不支持随机访问

    fruits = {"apple", "banana", "cherry"}
    fruits.add("orange")
    print(fruits)

    fruits = {"apple", "banana", "cherry"}
    x = fruits.copy()
    print(id(x))
    print(id(fruits))

    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.difference(y)
    print(f'差集{z}')

    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.difference_update(y)
    print(x)
    print('-' * 50)
    fruits = {"apple", "banana", "cherry"}
    fruits.discard("banana")
    print(fruits)
    print('-' * 50)
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    result = x.intersection(y, z)
    print(result)
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y)
    print(z)
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.union(y)
    print(z)

    print('apple' in z)

    print(x - y)
    print(x | y)
    print(x & y)
    print(x ^ y)


def use_generator():
    """
    使用生成式
    :return:
    """
    my_tuple = tuple(x for x in range(10))  # 元祖生成式
    print(my_tuple)
    my_set={x for x in 'abracadabra' if x not in 'abc'}
    print(my_set)
    print(len(my_set))


if __name__ == '__main__':
    use_generator()
