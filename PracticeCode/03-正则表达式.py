# 作者: 刘悦喆
# 2026年01月22日15时12分29秒
# liuyuezhe1211@163.com

import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for ls in email_list:
    res1 = re.match(r"[0-9a-zA-Z]{4,20}@163\.com$", ls)
    print(res1)
