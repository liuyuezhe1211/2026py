# 作者: 刘悦喆
# 2026年01月21日11时46分42秒
# liuyuezhe1211@163.com

import random
import time

class Sort:
    def __init__(self, n):
        """
        n是排序数的数量
        :param n:
        """
        self.arr = [0] * n
        self.len = n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 9999999)

    # 交换法的快排
    def partition(self, left, right):
        arr = self.arr
        i = k = left
        ramdom_pos = random.randint(left, right)
        arr[ramdom_pos], arr[right] = arr[right], arr[ramdom_pos]
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

    # 408中写的快排
    def huafen(self, l, r):
        arr = self.arr
        mid = arr[l]
        while l < r:
            while arr[r] >= mid and l < r:
                r -= 1
            arr[l] = arr[r]
            while arr[l] <= mid and l < r:
                l += 1
            arr[r] = arr[l]
        arr[l] = mid
        return l

    def quick_sort_408(self, l, r):
        if l >= r:
            return
        mid = self.huafen(l, r)
        self.quick_sort_408(l, mid - 1)
        self.quick_sort_408(mid + 1, r)

    # 堆排序
    def heap_sort(self):
        # 将非叶节点，从下往上调整为大根堆，使得整棵树成为大根堆
        for i in range(self.len // 2, -1, -1):
            self.adjust_max_heap(i, self.len)
        arr = self.arr
        arr[0], arr[self.len - 1] = arr[self.len - 1], arr[0]
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, arr_len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

    def adjust_max_heap(self, pos, arr_len):
        """
        把某个子树调整为大根堆
        :param pos:被调整元素的位置
        :param arr_len:当时列表总长度
        :return:
        """
        arr = self.arr
        dad = pos
        son = dad * 2 + 1
        while son < arr_len:
            if son + 1 < arr_len and arr[son] < arr[son + 1]:
                son = son + 1
            if arr[dad] < arr[son]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def test_time_use(self,self_func,*args,**kwargs):
        """
        直接调用,回调函数
        :param self_func:
        :param args:
        :param kwargs:
        :return:
        """
        start = time.time()
        self_func(*args,**kwargs)
        end = time.time()
        print(f'总计用时{end - start}')

if __name__ == '__main__':
    sort_count=10000
    my_sort = Sort(sort_count)

    # start=time.time()
    # my_sort.quick_sort(0, sort_count-1)
    # my_sort.quick_sort_408(0, sort_count-1)
    # my_sort.heap_sort()
    # end=time.time()
    # print(f'总计用时{end-start}')

    # my_sort.test_time_use(my_sort.quick_sort,0,sort_count-1)
    my_sort.test_time_use(my_sort.quick_sort_408,0,sort_count-1)
    # my_sort.test_time_use(my_sort.heap_sort)

