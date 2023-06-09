# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/8/24 21:50
 Tool   : PyCharm
 Content: 
"""
# coding=utf-8
import time

import paramiko


class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = 'root'
        self._password = 'jj'
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()

    # 建立连接
    def _connect(self):
        try:
            transport = paramiko.Transport((self._host, self._port),disabled_algorithms={"kex": ["diffie-hellman"
                                                                                                 "-group16-sha512"]})
            transport.connect(username=self._username, password=self._password)
        except paramiko.ssh_exception.SSHException as e:
            raise
        self._transport = transport

    # 下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    # 上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    # 执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport

        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print(data.strip())  # 打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print(err.strip())  # 输出错误结果
            return err

    def exec_commands(self, command_lst):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
            # self._client.set_missing_host_key_policy()
        comm = self._client.invoke_shell()
        for command in command_lst:
            comm.send(command + "\n")
            # comm.send(command)
        time.sleep(0.5)
        datas = comm.recv(1024).decode('utf-8').replace('\r', '')
        return datas

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()

    def mult_hosts_run(self, ips_lst, cmds_lst):
        datas = ''
        for ip in ips_lst:
            try:
                conn = SSHConnection(ip)
            except BaseException as e:
                print(e)
                continue
            data = conn.exec_commands(cmds_lst)
            datas += data
        return datas


def get_ips():
    ips = []
    ips = ['192.168.30.129','192.168.30.120']
    return ips


def get_cmds():
    cmds = []
    cmds = ['cd /tmp', 'pwd','exit']
    return cmds


def run_mult_hosts_mult_cmds(ips, cmds):
    datas = ''
    for ip in ips:
        try:
            conn = SSHConnection(ip, 22, 'root', 'jj')
        except paramiko.ssh_exception.SSHException as e:
            print(ip, '无法连通')
            continue
        datas += conn.exec_commands(cmds)
        conn.close()
    return datas


if __name__ == "__main__":
    # 实现在多个主机上执行多条命令
    datas = run_mult_hosts_mult_cmds(get_ips(), get_cmds())
    print(datas)

    # conn = SSHConnection('192.168.30.129', 22, 'root', 'jj')
    # localpath = 'hello.txt'
    # remotepath = '/tmp/hello.txt'
    # print('downlaod start')
    # conn.download(remotepath, localpath)
    # print('download end')
    # print('put begin')
    # conn.put(localpath, remotepath)
    # print('put end')

    # conn.exec_command('whoami')
    # conn.exec_command('cd /tmp && pwd')  # cd需要特别处理
    # conn.exec_command('pwd')
    # conn.exec_command('tree /tmp')
    # conn.exec_command('ls -l')
    # conn.exec_command('echo "hello python" > python.txt')
    # conn.exec_command('ls hello')  # 显示错误信息

    # 测试执行多条命令
    # datas= conn.exec_commands(['cd /tmp','pwd','ls /tt'])
    # conn.close()
    # print(datas)
    # print(f"{datas=}")

    # 测试chan
    # out = conn.exec_command('ll')
    # print(f"{out=}")
