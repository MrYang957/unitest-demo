# coding=utf-8
from selenium import webdriver
from config.config import *


class BrowserDriver():

    def __init__(self, driver):
        self.driver = driver

    #判断浏览器启动方式
    def get_browser(self):
        if browser_type == 'Firefox':
            driver = webdriver.Firefox(executable_path=driverPath)
        elif browser_type == 'IE':
            driver = webdriver.Ie(executable_path=driverPath)
        elif browser_type == 'Chrome':
            driver = webdriver.Chrome(executable_path=driverPath)
        elif browser_type == 'Edge':
            driver = webdriver.Edge(executable_path=driverPath)

        driver.maximize_window()
        driver.implicitly_wait(3)

        return driver
