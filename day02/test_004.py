'''
fixture 级别：session、class、module、func
'''

import pytest

@pytest.fixture(scope='module')
def db():
    print("前置：连接数据库")
    yield
    print("后置：断开连接数据库")


@pytest.fixture(scope='module')
def login():
    print("前置：在首次调用login的地方执行前置")
    yield
    print("后置：模块所有用例执行完后执行后置")

def test_001():
    print("用例1")

def test_002(login, db):   # 这个用例前执行login、db前置
    print("用例2")

def test_003(db):
    print("用例3")

def test_004(login):  # 这个用例为最后一个用例，在这个用例后前置
    print("用例4")