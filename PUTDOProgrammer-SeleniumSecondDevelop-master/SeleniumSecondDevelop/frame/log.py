#coding = utf-8

import logging
import os, time
from frame.report import *

#log配置
class Log:

    def __init__(self):
        self.logname = os.path.join(reportPath, '{}.log'.format(time.strftime('%Y%m%d_%H%M%S')))

    def __printconsole(self, level, message):
        logger = logging.getLogger('root')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')#设置日志格式

        ch = logging.FileHandler(self.logname, encoding='utf-8')
        ch.setLevel(logging.DEBUG)#设置日志级别

        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)

        ch.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(sh)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(sh)
        # 关闭打开的文件
        ch.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)