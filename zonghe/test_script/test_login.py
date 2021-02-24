'''
测试登录接口
'''

import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp


# 调取登录前的前置注册数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_setup.yaml"))
def setup_data(request):
    return request.param

# 调用读取login数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture()
def register(baserequest, url, setup_data, db_info):
    # 注册用户
    # # 初始化环境，避免环境中已有本次测试用到的数据
    # MySqlOp.delete_user(db_info, setup_data['data']['mobilephone'])
    # 发请求注册用户
    r = Member.register(baserequest, url, setup_data['data'])
    yield
    # 删除注册用户
    MySqlOp.delete_user(db_info, setup_data['data']['mobilephone'])

def test_login(register, baserequest, url,login_data):
    # 下发登录的请求
    print(login_data)
    r = Member.login(baserequest, url, login_data['data'])
    # 检查结果
    # 断言
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']