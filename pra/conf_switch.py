#!/usr/bin/env python
import paramiko
import time
import getpass
import sys
import socket

from pip._vendor.distlib.compat import raw_input



def run_commands(ip_file,cmd_file,username,password):
    switch_with_authentication_issue = []
    switch_not_reachable = []

    f = open(ip_file, 'r')
    for line in f.readlines():
        try:
            ip = line.strip()
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
            print("你已经成功连接到： ", ip)
            command = ssh_client.invoke_shell()
            cmdlist = open(cmd_file, 'r')
            cmdlist.seek(0)
            for line in cmdlist.readlines():
                command.send(line + "\n")
            time.sleep(2)
            cmdlist.close()
            output = command.recv(65535)
            print(output)
        except paramiko.ssh_exception.AuthenticationException:
            print("用户认证失败的" + ip + ".")
            switch_with_authentication_issue.append(ip)
        except socket.error:
            print(ip + "不可达，请检查网络.")
            switch_not_reachable.append(ip)
    f.close()
    ssh_client.close()

    print(' 以下交换机认证失败:')
    for i in switch_with_authentication_issue:
        print(i)
    print('\n 以下交换机网络不可达:')
    for i in switch_not_reachable:
        print(i)


if __name__ == '__main__':
    username = raw_input("用户名:")
    password = getpass.getpass("密码:")
    ip_file = sys.argv[1]
    cmd_file = sys.argv[2]
    run_commands(ip_file,cmd_file,username,password)