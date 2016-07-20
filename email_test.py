# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...\n form Roy', 'plain', 'utf-8')

from_addr = raw_input('登录邮箱：') # 输入Email地址和口令
password = raw_input('登录密码：')
smtp_server = raw_input('SMTP服务器地址（eg:smtp.qq.com）：') # 输入SMTP服务器地址
smtp_port = input("SMTP服务器端口(eg:587)：") # 输入SMTP服务器端口
to_addr = raw_input('收件人地址：') # 输入收件人地址

import smtplib
server = smtplib.SMTP(smtp_server, smtp_port) # SMTP协议默认端口是25
server.starttls()
server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password) # 登录
server.sendmail(from_addr, [to_addr], msg.as_string()) # 发送
server.quit() # 退出