# -*- coding: utf-8 -*-
# File Name: transport_upload_download.py
# Description: use paramiko_switch to upload or download file

import paramiko

ip = "192.168.30.150"
port = 22

trans = paramiko.Transport((ip, port))
# 建立连接，指定SSHClient的_transport
trans.connect(username="root", password="jason")
ssh = paramiko.SSHClient()
ssh._transport = trans
# 执行命令，与传统方法一样
stdin, stdout, stderr = ssh.exec_command('echo `date` && ls -lrth')
print(stdout.read().decode('utf-8'))

# 实例化一个sftp对象，指定连接的通道
sftp = paramiko.SFTPClient.from_transport(trans)
# 发送文件
sftp.put(localpath='./transport_upload_download.py', remotepath='/tmp/transport_upload_download_tmp.py')
# 下载文件
# sftp.get(localpath='./transport_upload_download.py', remotepath='/tmp/transport_upload_download_tmp.py')
stdin, stdout, stderr = ssh.exec_command('ls -lrht /tmp')
print(stdout.read().decode('utf-8'))
# 关闭连接
ssh.close()

