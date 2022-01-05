# __*__ coding:utf-8 __*__

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


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

# 邮件对象
msg = MIMEMultipart()
# 邮件正文内容, src="cid:0"可以把附件图片展示在正文中
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
   #  '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('admin管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open(r'D:\1.jpg', 'rb') as f:
    #设置附件的MIME和文件名，这里是jpg类型
    mime = MIMEBase('image', 'jpg', filename='1.jpg')
    #加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='1.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id','0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

# SMTP协议默认端口是25,
server = smtplib.SMTP(smtp_server, 25)
# 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接ssl
server.starttls()

# 打印和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登录smtp服务器
server.login(from_addr, password)
# 发邮件.as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
# 退出
server.quit()


