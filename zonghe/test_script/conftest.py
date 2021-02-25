'''
脚本层的公共前置、后置、整个执行过程执行一次。
不用import，通过conftest文件名找到
'''
import os
import sys

import pytest

# 跨目录导包路径会有问题，需获取当前文件的系统所在路径
# sys.path.append(os.getcwd())
# print(sys.path)
path = sys.path.append("D:\ApiAutoTest")
# print(path)

# curPath = os.path.abspath(os.path.dirname(__file__))
# print(curPath)
# rootPath = os.path.split(curPath)[0]
# print(rootPath)
# dir_path = os.path.dirname(rootPath)
# dir_path = os.path.dirname(dir_path)
# sys.path.append(dir_path)

# print(path)
#
# print(sys.path)
# os.pardir =os.path.realpath(__file__)
# print(os.pardir)
# path = sys.path.append(os.pardir)

from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests


@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(r"test_env\env.ini", "url")

@pytest.fixture(scope='session')
def db_info():
    return eval(DataRead.read_ini(r"test_env\env.ini", "db_info"))

@pytest.fixture(scope='session')
def baserequest():
    return BaseRequests()