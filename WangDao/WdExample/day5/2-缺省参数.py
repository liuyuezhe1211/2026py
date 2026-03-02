# 作者: 王道 龙哥
# 2024年12月28日09时32分28秒
# xxx@qq.com
def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s%s 是 %s" % (title, name, gender_text))


# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
print_info("老王", title="班长")
print_info("小美", '学习委员',False)
print('-'*50)
print_info("小美", gender=False,title='学习委员')

