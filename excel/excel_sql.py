import pymysql
import pandas as pd

eng = pymysql.connect(host="172.16.1.137", user="pig", db="test", charset="utf8")
# host: 主机IP
# user: 用户名
# password: 密码
# db: 数据库名
# charset: 字符集

# sql语句
sql = "select * from t1"

# 通过pandas模块查询，并将查询结果保存为dataFrame
df = pd.read_sql(sql, eng)
print(df.describe())
