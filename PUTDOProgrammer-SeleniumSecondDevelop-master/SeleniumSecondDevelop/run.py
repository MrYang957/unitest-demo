import unittest
from data.libs import HTMLTestReportCN
from config.config import *
from frame.report import *
from frame.Email import *


def run():
    test_path = os.path.join(rootPath, testsuitePath)
    suite = unittest.defaultTestLoader.discover(start_dir=test_path, pattern='test*.py')

    #测试报告路径设置在report.py的report_name
    if( setReport() == True ):
        with open(report_name, 'wb') as f:  # encoding='UTF-8'
            runner = HTMLTestReportCN.HTMLTestRunner(
                stream=f,
            )
            runner.run(suite)
        time.sleep(3)

    send_email(report_name)

if __name__ == '__main__':
    run()


