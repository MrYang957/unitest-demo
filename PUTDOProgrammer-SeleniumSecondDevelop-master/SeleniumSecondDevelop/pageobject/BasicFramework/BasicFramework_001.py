from frame.base import Base
from frame.log import Log

log = Log()

class BasicFramework(Base):
    basicframeworkModule = ['xpath','//span[text()="基础框架"]',0]


    def clickBasicFramework(self):
        self.click_num(self.basicframeworkModule)
        log.info('点击基础框架模块')
