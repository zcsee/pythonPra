# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/8/24 21:27
 Tool   : PyCharm
 Content: 
"""
#实例化SSHClient
import paramiko

ip='192.168.30.129'
user='root'
passwd='jj'
command='cd /tmp && pwd'

client = paramiko.SSHClient()
#自动添加策略，保存服务器的主机名和密钥信息
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接SSH服务端，，以用户名和密码进行认证
client.connect(ip,username=user,password=passwd)
#实例化Transport，并建立会话Session
ssh_session = client.get_transport().open_session(timeout=20)
if ssh_session.active:
    ssh_session.exec_command(command)
    print(ssh_session.recv(1024).decode())
if ssh_session.active:
    ssh_session.exec_command('pwd')
    print(ssh_session.recv(1024).decode())
client.close()