# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/5/20 11:58
 Tool   : PyCharm
 Content: 通过传入一个有内网ip与带外IP的文件，批量更新zabbix中，该内网IP对应服务器的带外IP
"""
import re
import sys
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
            # 执行sql并返回查询到的行数
            effect_row = self.run_sql(cursor, sql)
            # print(f"总共返回{effect_row}行")
            if re.findall(pattern="^select.*", string=sql):
                print(f"I find select sql:{sql}")
                res = cursor.fetchall()
                # print(f"res is {res}")
                # 打印返回的结果
                # print(f"返回的结果如下:\n")
                # for item in res:
                #     print(item)
                list_res.append(res)
                print(f"查询结果返回{effect_row}行")
            if re.findall(pattern="^update.*", string=sql):
                # print(f"I find update sql:{sql}")

                res = cursor.fetchall()
                # print(f"res is {res}")
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
    host = '192.168.56.104'
    port = 3306
    username = 'root'
    password = 'Tcdn@2007'
    db = 'zabbix'
    return host, port, username, password, db


def show_info(list_res):
    # print(f"show_info的传入参数类型为{type(list_res)}")
    if len(list_res):
        for res in list_res:
            # print(f"拆到列表后，res的类型{type(res)}")
            if isinstance(res, tuple):
                for info in res:
                    if isinstance(info, tuple):
                        # 以元组的方式打印
                        print(info)
                        # 拆包打印
                        # for item in info:
                        #     print(item, end="\t")
                        # print("")
                    else:
                        print(info)
            else:
                for item in res:
                    print(item, end="\t")
                print("")
    else:
        print(list_res)


def gen_sql(file):
    server_dic = {}
    sql_list = []
    with open(file, 'r', encoding='utf-8') as fd:
        tt = fd.read().splitlines()
        # print(f"{tt=}")

    for item in tt:
        ip_inner, ip_bmc = item.split()
        sql = f"update interface set ip = '{ip_bmc}' where hostid=( " \
              f"select hostid from  (select hostid from interface where ip = '{ip_inner}' and type=1) ub) and type=3;"

        # ip_inner, ip_bmc = fd.read().splitlines()
        # print(f"{ip_inner=},{ip_bmc=}")
        server_dic[ip_inner] = ip_bmc
        # sql = f"update interface set ip = '{ip_bmc}' where hostid=( " \
        #       f"select hostid from  (select hostid from interface where ip = '{ip_inner}' and type=1) ub) and type=3;"
        sql_list.append(sql)
    # 最后添加查询语句，检查interface表
    sql = ['select * from interface;']
    sql_list.extend(sql)
    return sql_list


def main():
    host, port, username, password, db = get_info()
    mysql = MysqldbOp(host=host, port=port, username=username, password=password, db=db)
    # 读取传入的文件名，用于生成sql
    sqls = gen_sql(sys.argv[1])
    # print(f"{sqls=},数目为{len(sqls)}")
    list_result = mysql.run_sqls(sqls)
    show_info(list_result)


if __name__ == "__main__":
    main()
