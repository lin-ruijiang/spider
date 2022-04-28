# 林睿江
# 新的一天，新的活力，新的希望
from bs4 import BeautifulSoup
import re

file = open("./1.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# print(bs.title)  # 标签及找到的第一个内容
# print(bs.a)

# print(bs.title.string)
# print(bs.a.attrs)

# print(type(bs))
# print(bs.name)
# print(bs.attrs)
# print(bs)
# print(bs.a.string)

# print(bs.head.contents)
# 字符串过滤，会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# t_list = bs.find_all(re.compile("a"))
# print(t_list)
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
#
# t_list = bs.find_all(name_is_exists)
# # print(t_list)
# for item in t_list:
#       print(item)

# t_list = bs.find_all(id="head")
# t_list=bs.find_all(class_=True)
# print(t_list)

# t_list = bs.find_all("a", limit=3)
# t_list = bs.select('title')
# t_list = bs.select(".mnav")

# t_list=bs.select("#u1")
# t_list=bs.select("a[class='bri']")
# t_list = bs.select("head > title")
t_list = bs.select(".mnav~.bri")

for item in t_list:
    print(item)
