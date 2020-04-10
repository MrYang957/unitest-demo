#coding = utf-8
from util.usualTime import *
import os

#项目路径
rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(rootPath)

#当前文件所在路径
currentPath = os.sys.path[0]
# print(rootPath)

#获取上级目录
upPath = os.path.abspath(os.path.dirname(os.getcwd()))