# coding=utf-8


#配置浏览器Driver
#类型有Chrome、IE、Firefox、Edge
browser_type = "Chrome"
#默认路径是项目Tools下的路径，如果不行，可换成绝对路径
driverPath = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"

#配置用例通过是否截图
isScreenshot = False

#配置用例执行失败是否重跑
isRerun = False

#配置断线是否重连
isReconnet = False

#配置是否发送邮件和地址
isEmail = False
smtpServer = 'smtp.foocaa.com'  #smtp服务器
senderEmailAccount = 'chen.gen.ji@foocaa.com'   #发送人邮箱
senderEmailPassword = 'chengenji'   #发送人密码
reccederEmailAccount = 'chen.gen.ji@foocaa.com'  #接收者邮箱

#配置用例路径
testsuitePath = "testsuites"
#路径为项目下存放用例的文件夹名称
