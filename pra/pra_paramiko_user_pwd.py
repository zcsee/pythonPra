# -*- coding: utf-8 -*-
# File Name: pra_paramiko_user_pwd.py
# Description: 使用用户名密码来登录并远程执行命令
import paramiko

# 建立一个sshclient对象
ssh = paramiko.SSHClient()
# 将信任的主机自动加入到host_allow列表，须放在connect方法前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# 调用connect方法连接服务器
ssh.connect(hostname="192.168.30.129", port=22, username="root", password="jj")
# 执行命令
stdin, stdout, stderr = ssh.exec_command("echo `date` && ls -lrt && cd /tmp")
# 结果放到stdout中，如果有错误，就放到stderr中
print(stdout.read().decode('utf-8'))

stdin, stdout, stderr = ssh.exec_command("pwd")
# 结果放到stdout中，如果有错误，就放到stderr中
print(stdout.read().decode('utf-8'))
#
returnCode = stdout.channel.recv_exit_status()
print("returnCode:", returnCode)
# 关闭连接
ssh.close()
