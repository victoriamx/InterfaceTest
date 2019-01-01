# -*-coding:utf-8 -*-
import logging
import os

#项目路径
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(proj_path,'data')
test_path = os.path.join(proj_path,'test')

log_file = os.path.join(proj_path,'log','log.txt')
report_file = os.path.join(proj_path,'report','report.html')

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s,%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file,
                    filemode='a')#追加模式

#邮件配置
smtp_server='smtp.163.com'
smtp_user='linminxia3@163.com'
smtp_password='linminxia163'

sender=smtp_user
receiver='linminxia3@163.com'
subject='接口测试报告'






