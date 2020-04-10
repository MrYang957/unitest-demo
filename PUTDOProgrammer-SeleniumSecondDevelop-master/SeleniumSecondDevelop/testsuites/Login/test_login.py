# coding=utf-8
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from frame.base import Base
from pageobject.BasicFramework.BasicFramework_001 import BasicFramework
from frame.BrowserDriver import BrowserDriver
from pageobject.Login.LoginPage import LoginPage
from frame.log import *

log = Log()

class Login(unittest.TestCase, Base):

    @classmethod
    def setUpClass(cls):
        browser = BrowserDriver(cls)
        cls.driver = browser.get_browser()
        cls.driver.get("http://www.guomao.foocaa.cn")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        cls.my_quit(cls)
        pass

    def test_1_login(self):
        login = LoginPage(self.driver)
        login.login_web()
        basic = BasicFramework(self.driver)
        basic.clickBasicFramework()

    def test_2_test_1_login(self):
        # login = LoginPage(self.driver)
        # login.login_web()
        # basic = BasicFramework(self.driver)
        # basic.clickBasicFramework()
        self.driver.find_element_by_xpath('.//*[@id="mainContainer"]/div[3]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr/td/span/a').click()
        time.sleep(2)
        self.driver.find_element_by_id('bind_mobile').clear()
        time.sleep(2)
        self.driver.find_element_by_id('bind_mobile').send_keys('15812341234')
        time.sleep(2)