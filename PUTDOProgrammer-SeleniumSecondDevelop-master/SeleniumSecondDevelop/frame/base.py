from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from frame.log import Log
from frame.report import *
from data.libs import HTMLTestReportCN

log = Log()

class Base:
    """
    重载方法
    """
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def isdisplayed(element):
        value = element.is_displayed()
        return value

    @staticmethod
    def my_sleep(secondes):
        time.sleep(secondes)
        log.info('暂停%d秒' % secondes)

    def screenshots(self):
        """
        获取图片，保存到对应报告目录下的screenshots文件夹
        :return:无
        """
        try:
            time.sleep(1)
            pic_info = HTMLTestReportCN.ReportDirectory.get_screenshot(self.driver)
            log.info('截图保存成功{}'.format(pic_info))
        except Exception as e:
            log.error('截图保存失败{}'.format(e))

    def find_element(self, selector):
        by = selector[0]
        value = selector[1]
        element = None
        wait = WebDriverWait(self.driver, timeout=15)  # timeout = 30
        if by in ['id', 'name', 'class', 'tag', 'link', 'xpath', 'css', 'plink']:
            try:
                if by == 'id':
                    # element = self.driver.find_element_by_id(value)
                    element = wait.until(EC.presence_of_element_located((By.ID, value)))
                elif by == 'name':
                    # element = self.driver.find_element_by_name(value)
                    element = wait.until(EC.presence_of_element_located((By.NAME, value)))
                elif by == 'class':
                    # element = self.driver.find_element_by_class_name(value)
                    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
                elif by == 'tag':
                    # element = self.driver.find_element_by_tag_name
                    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, value)))
                elif by == 'link':
                    # element = self.driver.find_element_by_link_text(value)
                    element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, value)))
                elif by == 'xpath':
                    # element = self.driver.find_element_by_xpath(value)
                    element = wait.until(EC.presence_of_element_located((By.XPATH, value)))
                elif by == 'css':
                    # element = self.driver.find_element_by_css_selector(value)
                    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
                elif by == 'plink':
                    # element = self.driver.find_element_by_partial_link_text(value)
                    element = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
                else:
                    log.error('元素定位失败')
                log.info('元素定位成功。定位方式:%s,使用的值%s' % (by, value))

                return element

            except Exception as e:
                log.error('报错信息：{}'.format(e))
                self.screenshots()
        else:
            log.error('输入的元素定位方式错误,参考[id, name, class, tag, link, plink, css,xpath]')

    def find_elements(self, selector):
        """定位多个元素
        Agrs:
         - by - 定位方式
         - value - 定位元素
         - num - 选择第几个元素  #  第一个元素是num=0
        Usage:
         self.find_elements(self.['id', 'firstMenu1', 0])
        """
        by = selector[0]
        value = selector[1]
        num = selector[2]
        els = None
        wait = WebDriverWait(self.driver, 15)  # timeout = 15
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            # noinspection PyBroadException
            try:
                if by == 'id':
                    els = wait.until(EC.presence_of_all_elements_located((By.ID, value)))[num]
                elif by == 'name':
                    els = wait.until(EC.presence_of_all_elements_located((By.NAME, value)))
                elif by == 'class':
                    els = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, value)))[num]
                elif by == 'tag':
                    els = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, value)))[num]
                elif by == 'link':
                    els = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, value)))[num]
                elif by == 'plink':
                    els = wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, value)))[num]
                elif by == 'css':
                    els = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, value)))[num]
                elif by == 'xpath':
                    els = wait.until(EC.presence_of_all_elements_located((By.XPATH, value)))[num]
                else:
                    log.error('没有找到元素')
                log.info('元素定位成功。定位方式：%s,使用的值:%s,第%s个元素' % (by, value, num+1))

                return els
            except NoSuchElementException as e:
                log.error("报错信息：{}" .format(e))
                self.screenshots()  # 调用截图
        else:
            log.error('输入的元素定位方式错误,参考[id, name, class, tag, link, plink, css,xpath]')


    def my_quit(self):
        self.driver.quit()
        log.info('关闭浏览器')

    def click(self, selector):
        element = self.find_element(selector)
        try:
            element.click()
            log.info('点击元素成功')
        except BaseException as e:
            display = self.isdisplayed(element)
            if display is True:
                self.my_sleep(2)
                element.click()
                log.info('点击元素成功')
            else:
                self.screenshots()
                log.error('点击元素报错:{}'.format(e))

    def click_num(self, selector):
        elements = self.find_elements(selector)
        try:
            elements.click()
            log.info('点击元素成功')
        except BaseException as e:
            display = self.isdisplayed(elements)
            if display is True:
                self.my_sleep(3)
                elements.click()
                log.info('点击元素成功')
            else:
                self.screenshots()
                log.error('点击元素报错:{}'.format(e))