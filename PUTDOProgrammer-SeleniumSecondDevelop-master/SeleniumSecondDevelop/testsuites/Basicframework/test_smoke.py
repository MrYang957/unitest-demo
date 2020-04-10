# coding=utf-8
import time
import unittest
from selenium.webdriver import ActionChains

from frame.base import Base
from pageobject.BasicFramework.BasicFramework_001 import BasicFramework
from frame.BrowserDriver import BrowserDriver
from pageobject.Login.LoginPage import LoginPage
from frame.log import *

log = Log()

class Basicframe(unittest.TestCase, Base):

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

    def test_1_serach_member(self):
        name = self.find_element(['id', "accountXXX"])
        name.send_keys("qa")
        login = LoginPage(self.driver)
        login.login_web()
        basic = BasicFramework(self.driver)
        basic.clickBasicFramework()

    def test_2_edit_member(self):
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

    # def test_3_edit_member(self):
    #     login = LoginPage(self.driver)
    #     login.login_web()
    #     basic = BasicFramework(self.driver)
    #     basic.clickBasicFramework()
        # self.driver.find_element_by_xpath('.//*[@id="mainContainer"]/div[3]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr/td/span/a').click()
        # time.sleep(2)
        # self.driver.find_element_by_id('bind_mobile').clear()
        # time.sleep(2)
        # self.driver.find_element_by_id('bind_mobile').send_keys('15812341234')
        # time.sleep(2)
        #
        # above_jzbm = self.driver.find_element_by_xpath('//form/div[4]/div[1]/div/div[2]/div/span/span/span')
        # ActionChains(self.driver).move_to_element(above_jzbm).perform()
        # time.sleep(2)
        # try:
        #     del_jzbm_btn = self.driver.find_element_by_xpath("//form/div[4]/div[1]/div/div[2]/div/span/span/span/span[1]/i")
        #     del_jzbm_btn.click()
        #     time.sleep(2)
        # except Exception as e:
        #     print("直接选择兼职部门", format(e))
        #     self.driver.find_element_by_xpath(
        #         "//form/div[4]/div[1]/div/div[2]/div/span/span/span").click()
        #     time.sleep(2)
        #     fxk = self.driver.find_elements_by_xpath(".//*[@class='ant-select-tree-title']")
        #     fxk[2].click()
        #     time.sleep(2)
        # else:
        #     self.driver.find_element_by_xpath(
        #         "//form/div[4]/div[1]/div/div[2]/div/span/span/span").click()
        #     time.sleep(2)
        #     fxk = self.driver.find_elements_by_xpath(".//*[@class='ant-select-tree-title']")
        #     fxk[2].click()
        #     time.sleep(2)
        #
        #
        # above = self.driver.find_element_by_xpath('.//*[@id="possec"]/div')
        # ActionChains(self.driver).move_to_element(above).perform()
        # time.sleep(2)
        # try:
        #     del_btn = self.driver.find_element_by_xpath('.//*[@id="possec"]/div/span/i')
        #     del_btn.click()
        # except Exception as ec:
        #     print("直接选择兼职岗位", format(ec))
        #     self.driver.find_element_by_xpath('.//*[@id="possec"]/div').click()
        #     time.sleep(2)
        #     self.driver.find_element_by_xpath('.//*[@role="listbox"]/li[1]').click()
        #     time.sleep(3)
        # else:
        #     self.driver.find_element_by_xpath('.//*[@id="possec"]/div').click()
        #     time.sleep(2)
        #     self.driver.find_element_by_xpath('.//*[@role="listbox"]/li[1]').click()
        #     time.sleep(3)
        #
        # self.driver.find_element_by_xpath("//button[2]").click()
        # time.sleep(3)
        # # try:
        # #
        # #     print("Test Pass.")
        # # except Exception as er:
        # #     print("Test Fail.", format(er))
        # mes = self.driver.find_element_by_xpath("//div[3]/div/span/div/div/div/div[1]").text
        # self.assertEqual(mes, "编辑")



