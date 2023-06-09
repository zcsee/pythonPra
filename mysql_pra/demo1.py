# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/20 11:58
 Tool  : PyCharm
"""
import re

import pymysql


class MysqldbOp:
    def __init__(self, host, username, password, db, port):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.port = port

    def get_connect(self):
        # 创建连接
        conn = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password, db=self.db)
        return conn

    def run_sqls(self, list_sql):
        conn = self.get_connect()
        cursor = conn.cursor()
        list_res = []

        for sql in list_sql:
            effect_row = self.run_sql(cursor, sql)
            # print(f"总共返回{effect_row}行")
            if re.findall(pattern="select.*", string=sql):
                print(f"I find select sql:{sql}")
                pass
                res = cursor.fetchall()
                print(f"res is {res}")
                # 打印返回的结果
                # print(f"返回的结果如下:\n")
                # for item in res:
                #     print(item)
                list_res.append(res)
        # 将连接进行提交
        conn.commit()
        # print(list_res)
        # 关闭游标和连接
        try:
            cursor.close()
            conn.close()
        except BaseException as e:
            print(e)
        if len(list_res):
            return list_res

    def run_sql(self, cursor, sql):
        return cursor.execute(sql)


def get_info():
    # 账号密码需要通过安全的方式进行输入，例如临时输入等，此处为测试
    host = '192.168.216.3'
    port = 3306
    username = 'root'
    password = '123456'
    db = 'test'
    return host, port, username, password, db


def show_info(list_res):
    print(f"show_info的传入参数类型为{type(list_res)}")
    if len(list_res):
        for res in list_res:
            print(f"拆到列表后，res的类型{type(res)}")
            if isinstance(res, tuple):
                for info in res:
                    if isinstance(info, tuple):
                        for item in info:
                            print(item, end="\t")
                        print("")
                    else:
                        print(info)
            else:
                for item in res:
                    print(item, end="\t")
                print("")
    else:
        print(list_res)


def main():
    host, port, username, password, db = get_info()
    mysql = MysqldbOp(host=host, port=port, username=username, password=password, db=db)
    sql = ["select * from student;", "select name from student limit 1;"]
    # sql = ["insert into student(id, name)values (1,'施志成');"]
    list_result = mysql.run_sqls(sql)
    print(f"发发{list_result[:]}")
    # show_info(list_result[1])


if __name__ == "__main__":
    main()
