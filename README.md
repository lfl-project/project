调用paramiko连接linux服务器
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import paramiko
host = ""
port = 
user = ""
root = ""
pwd = ""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,user,pwd,timeout=10)
stdin,stdout,stder = ssh.exec_command("ifconfig")
orig_result = stdout.read()
str_result = orig_result.decode("UTF-8")
print(str_result)
