# 作者: 王道 龙哥
# 2024年12月30日09时57分16秒
# xxx@qq.com
class HouseItem:
    def __init__(self, name, area):
        """
        初始化方法
        :param name: 家具名字
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        """
        房子初始化方法
        :param house_type:
        :param area:
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 剩余可用面积
        self.items_list = []  # 家具列表

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.items_list))

    def add_item(self, item:HouseItem):#通过冒号:对象类型,加注解
        if item.area>self.free_area:
            print('房子没空间了，放家具失败')
            return
        # 2. 计算剩余面积
        self.free_area-=item.area
        # 3. 将家具的名称追加到名称列表中
        self.items_list.append(item.name)


if __name__ == '__main__':
    bed = HouseItem('席梦思', 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)
    print(bed)
    print(chest)
    print(table)
    house=House("二室一厅", 30)
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    print(house)