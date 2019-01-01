# -*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import sys
sys.path.append('../Config/')
from config import *

def send_email(report_file):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(subject, 'utf-8')

    with open(report_file,encoding='utf-8') as f:
        content=f.read()
   
    with open(report_file,'rb') as f:
        att1=f.read()
    attachment=MIMEText(att1,'base64','utf-8')
    attachment['Content-Type']='application/octet-stream'
    attachment['Content-Disposition']='attachment;filename="{}"'.format(report_file)
    msg.attach(attachment)
    msg.attach(MIMEText(content,'plain','utf-8'))
    try:
        smtp=smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user,smtp_password)
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.info('successful send')
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

send_email(report_file)









