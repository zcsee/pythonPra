# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/18 14:58
 Tool  : PyCharm
"""
import os.path

import paramiko
import re

CISCO_hosts_file = "CISCO_switch_ips.txt"
H3C_hosts_file = "H3C_switch_ips.txt"
hosts_files = [CISCO_hosts_file, H3C_hosts_file]

# 交换机类型的re库的patter
pat_h3c = re.compile("H3C")
pat_cisco = re.compile("CISCO")


def get_account():
    username = input("Please input your account:")
    password = input("Please input your password:")
    return username, password


def get_hosts(hosts_file):
    with open(hosts_file) as fd:
        host_ip = fd.read().splitlines()
    return host_ip


def save2file(switch_ip, config_content, switch_type):
    # 检测交换机类型的文件夹是否存在，不存在则创建
    if not os.path.exists(switch_type):
        os.makedirs(switch_type)
    file_name = switch_type + "-" + switch_ip + ".txt"
    # linux系统下的路径
    with open(switch_type + "/" + file_name, "w") as fd:
        fd.write(config_content)
    # windows系统下的路径
    # with open(switch_type + "\\" + file_name, "w") as fd:
    #     fd.write(config_content)


def get_switch_setting(switch_ip, switch_type, user_name, password):
    # 通过paramiko库连接交换机
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=switch_ip, port=22, username=user_name, password=password)
    except BaseException as e:
        print(e)
        return ''
    # 执行命令，获取命令回显
    if switch_type == "H3C":
        command = "display cu"
    elif switch_type == "CISCO":
        command = "show running-config"
    # 执行命令并获取回显内容
    stdin, stdout, stderr = client.exec_command(command)
    config_content = stdout.read().decode('utf-8')
    try:
        client.close()
    except BaseException as e:
        print(e)
    # 将配置存到单独的文件中
    save2file(switch_ip, config_content, switch_type)


def get_config(file):
    user_name, password = get_account()
    for item in file:
        # 通过re进行文件名匹配，识别交换机的类型
        if re.findall(pattern=pat_h3c, string=item):
            switch_type = "H3C"
        elif re.findall(pattern=pat_cisco, string=item):
            switch_type = "CISCO"
        # TODO
        # print(item)
        host_ip = get_hosts(item)
        if len(host_ip):
            print(host_ip)
            for ip in host_ip:
                get_switch_setting(ip, switch_type, user_name, password)
            # get_switch_setting(host_ip)
    print("获取完成.")


def main():
    get_config(hosts_files)
    pass


if __name__ == "__main__":
    main()
