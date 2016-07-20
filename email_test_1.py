# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import getpass


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \

        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('登录邮箱：') # 输入Email地址和口令
#password = raw_input('登录密码：')
password = getpass.getpass('登录密码：')
smtp_server = raw_input('SMTP服务器地址（eg:smtp.qq.com）：') # 输入SMTP服务器地址
smtp_port = input("SMTP服务器端口(eg:587)：") # 输入SMTP服务器端口
to_addr = raw_input('收件人地址：') # 输入收件人地址

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Roy<%s>' % from_addr)
msg['To'] = _format_addr(u'feng.yang<%s>' % to_addr)
msg['Subject'] = Header(u'测试Python Email', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password) # 登录
server.sendmail(from_addr, [to_addr], msg.as_string()) # 发送
server.quit() # 退出