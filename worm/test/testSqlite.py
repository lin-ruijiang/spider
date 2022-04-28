# 林睿江
# 新的一天，新的活力，新的希望
import sqlite3

conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
print("opened database successfully")

c = conn.cursor()
sql = ""

c.execute(sql)
conn.commit()
conn.close()
print("成功建表")
