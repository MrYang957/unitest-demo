#coding = utf-8
import smtplib
from email._header_value_parser import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from idna import unicode

from frame.report import *
from config.config import *


def send_email(newfile):
    """
    发送邮件
    :return:
    """

    file = open(newfile , "rb")
    mail_body = file.read()
    file.close()

    #发送邮箱主题
    subject = "自动化测试报告"
    msg = MIMEMultipart("mixed")

    # msg_html1 = MIMEText(mail_body , "html" , "utf-8")
    # msg.attach(msg_html1)

    msg_html = MIMEText(mail_body , "html" , "utf-8")
    msg_html["Content-Disposition"] = 'attachment;filename="' + reportName + '"'
    print("msg_html[\"Content-Disposition\"]=" + msg_html["Content-Disposition"])
    msg.attach(msg_html)

    msg['From'] = senderEmailAccount
    msg['To'] = ";".join(reccederEmailAccount)
    # msg['Subject'] = Header(subject , 'utf-8')
    # print("subject="+subject)
    msg['Subject'] = subject

    #连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpServer , 25)
    smtp.login(senderEmailAccount , senderEmailPassword)
    smtp.sendmail(senderEmailAccount , reccederEmailAccount , msg.as_string())
    smtp.quit()
    print("测试完成，测试报告已经发送到邮箱中，注意查收。")

