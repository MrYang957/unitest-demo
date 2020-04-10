#coding = utf-8

from util.commonPath import *
from util.usualTime import *
import os

#设置测试报告
reportPath = os.path.join(rootPath, "report", currentDateTime)#报告绝对路径
reportName = 'TestReport{}.html'.format(currentDateTime)    #只带报告名称和后缀
report_name = os.path.join(reportPath, reportName)#带路径+报告名称和后缀，报告文件绝对路径
screenshotPathAbs = os.path.join(reportPath, "screenshots")#截图绝对路径
screenshotPath = "./screenshots/"  # 截图相对路径，相对与报告html文件

def setReport():
    if (os.path.exists(reportPath) != True):
        os.makedirs(reportPath)
    return True