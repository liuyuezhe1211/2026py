# 作者: 刘悦喆
# 2026年01月21日11时46分42秒
# liuyuezhe1211@163.com

import random


class Sort:
    def __init__(self, n):
        """
        n是排序数的数量
        :param count:
        """
        self.arr = [0] * n
        self.len = n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):
        arr = self.arr
        i = k = left
        ramdom_pos=random.randint(left,right)
        arr[ramdom_pos],arr[right]=arr[right],arr[ramdom_pos]
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pov = self.partition(left, right)
            self.quick_sort(left, pov - 1)
            self.quick_sort(pov + 1, right)


if __name__ == '__main__':
    my_sort = Sort(10)
    print(my_sort.arr)
    my_sort.quick_sort(0, 9)
    print(my_sort.arr)
