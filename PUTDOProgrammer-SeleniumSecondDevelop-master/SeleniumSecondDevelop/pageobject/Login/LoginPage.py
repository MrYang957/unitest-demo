#coding = utf-8

from frame.log import *
from frame.base import Base

log = Log()

class LoginPage(Base):
    """
    登陆页面
    """

    def login_web(self, username="qa-toby", password="123abc"):
        name = self.find_element(['id', "account"])
        pwd = self.find_element(['id', "password"])
        btn = self.find_element(['class', 'ant-btn-lg'])
        # btn = self.find_element(['class', 'ant-btn-l'])  # 错误的class
        name.send_keys(username)
        log.info('输入用户名：%s' % username)
        pwd.send_keys(password)
        log.info('输入密码：%s' % password)
        btn.click()
        log.info('登录')
        # try:
        #     name = self.find_element(['id', "account"])
        #     pwd = self.find_element(['id', "password"])
        #     # btn = self.find_element(['class', 'ant-btn-lg'])
        #     btn = self.find_element(['class', 'ant-btn-l'])#错误的class
        #     name.send_keys(username)
        #     log.info('输入用户名：%s' % username)
        #     pwd.send_keys(password)
        #     log.info('输入密码：%s' % password)
        #     btn.click()
        #     log.info('登录')
        # except Exception as e:
        #     log.error('报错信息：{}'.format(e))
        #     self.screenshots()
        #     raise