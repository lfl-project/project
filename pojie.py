#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import paramiko
#创建python对象
ssh = paramiko.SSHClient()
#允许连接不在know_host文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.33.9', port=22, username='root', password='admin')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()
print(result.decode('utf-8'))
# 关闭连接
ssh.close()