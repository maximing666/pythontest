from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    print('name:' + name, 'addr:' + addr)
    return formataddr((Header(name, 'utf-8').encode(), addr),)


''''
# 输入SMTP服务器地址
smtp_server = input('SMTP server:')
# 输入Email地址和口令
from_addr = input('From:')
password = input('Password:')
# 输入收件人地址
to_addr = input('To:')
'''
smtp_server = 'smtp.qq.com'
from_addr = '61548681@qq.com'
password = 'kpjyuurcixxncaaj'
to_addr = 'maxm@cecurs.com'

# 邮件内容
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('admin管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25)

# 打印和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登录smtp服务器
server.login(from_addr, password)
# 发邮件.as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
# 退出
server.quit()


