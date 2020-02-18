#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import paramiko
host = "192.168.33.9"
port = 22
user = "root"
pwd = "admin"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,user,pwd,timeout=10)
stdin,stdout,stder = ssh.exec_command("ifconfig")
orig_result = stdout.read()
str_result = orig_result.decode("UTF-8")
print(str_result)