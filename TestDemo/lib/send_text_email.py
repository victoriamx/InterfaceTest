import smtplib #用于建立smtp连接
from email.mime.text import MIMEText #邮件需要专门的MIME格式
import sys
sys.path.append('../Config/')
from config import *
##编写邮件内容
msg=MIMEText('hello world,for test!','plain','utf-8')
#plain：普通文本格式邮件内容

##组装邮件头
msg['From']=sender
msg['To']=receiver
msg['Subject']=subject

##连接smtp服务器，发送邮件
smtp=smtplib.SMTP(smtp_server)
smtp.login(smtp_user,smtp_password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()