# coding=utf-8
import pymysql

database = pymysql.connect('localhost', 'root', 'zky26321119@', 'mysql', charset='utf8')
cursor = database.cursor()
# 初始化指针

# 增
"""sql = "INSERT INTO data (site, name, line_name, nature,class ,type, date, part, power) VALUES ('天下', '不知道什么公变','不知道什么线路', '公用', '箱变', 'S9', '2020-2-11', 'A', '1000');"
cursor.execute(sql)
database.commit()#修改数据后，需要commit
database.close()"""

# 改
"""sql_2="UPDATE data SET site='北京' WHERE site='天下';"
cursor.execute(sql_2)
database.commit()
database.close()"""

# 查询
"""sql_3="SELECT line_name,sum(power) FROM data WHERE site='五寨县' GROUP BY line_name;"
cursor.execute(sql_3)
result=cursor.fetchall()
print(result)"""

# 删除
sql_4="DELETE FROM data WHERE site='北京'"
cursor.execute(sql_4)
database.commit()
database.close()
