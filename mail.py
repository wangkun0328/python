#!/usr/bin/env python
#encoding=utf-8
import smtplib,sys
from email.mime.text import MIMEText


class send_mail:
    def __init__(self,e,c,status):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.smtp_server = 'smtp.163.com'
        self.smtp_port = '25'
        self.to_user = 'xxxxx@xx'
        self.username = 'xxxxxx@163.com'
        self.password = 'xxxxxx'
        self.From = 'xxxxxx'

        self.e = e
        self.c = c
        self.status = status

    def error_mail(self):
        m = '<p>%s %s</p>' % (self.e,self.c)
        subject = '%s error' % self.status
        msg = MIMEText(m,_subtype='html',_charset='utf8')
        msg['Subject'] = subject
        msg['From'] = self.From
        msg['To'] = self.to_user


        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server,self.smtp_port)
            smtp.starttls()
            smtp.login(self.username,self.password)
            smtp.sendmail(self.username,self.to_user,msg.as_string())
            smtp.close()
            print 'success'
        except:
            print 'fail'
