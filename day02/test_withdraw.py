'''
# 使用注册完的用户登录
# 注册用户>>登录>>充值1000>>取现100
'''
import mock
import requests,random,pytest

# 注册18888899999
# register_data = [
#                     {
#                     {"data": {"mobilephone": 18888899999, "pwd": "123456", "regname": "leiming"},
#                      "expect": {"status": 1, "code": "10001"}
#                      }
#                 ]

# 注册并断言注册结果
def test_register():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    register_data={"mobilephone": 15288899999, "pwd": "123456"}
    r = requests.post(url, data=register_data)
    assert r.json()['status'] == 1
    assert r.json()['code'] == "10001"


# 登录数据，包含登录信息和预期结果信息
# login_data = [
#     {"data": {"mobilephone": 18888899999, "pwd": "123456"},
#      "expect": {"status": 1,"code": "10001"}}
#     ]
#
# @pytest.fixture(scope='function')
def test_login():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    # r = requests.post(url, data=login_data['data'])
    # assert r.json()['status'] == login_data['expect']['status']
    # assert r.json()['code'] == login_data['expect']['code']
    login_data ={"mobilephone": 15288899999, "pwd": "123456"}
    r = requests.post(url, data=login_data)
    assert r.json()['status'] == 1
    assert r.json()['code'] == "10001"


# 充值
# recharge_data = [
#     {"data": {"mobilephone": 18888899999, "amount": 88888},
#      "expect": {"status": 1,"code": "10001"}}
#     ]
def test_recharge():
    url = "http://jy001:8081/futureloan/mvc/api/member/recharge"
    # r = requests.post(url, data=recharge_data['data'])
    # assert r.json()['status'] == recharge_data['expect']['status']
    # assert r.json()['code'] == recharge_data['expect']['code']
    recharge_data = {"mobilephone": 15288899999, "amount": 88888}
    r = requests.post(url, data=recharge_data)
    assert r.json()['status'] == 1
    assert r.json()['code'] == "10001"


# 提现
# withdraw_data = [
#     {"data": {"mobilephone": 18888899999, "amount": 9999},
#      "expect": {"status": 1,"code": "10001"}}
#     ]



def test_withdraw():
    url = "http://jy001:8081/futureloan/mvc/api/member/withdraw"
    # r = requests.post(url, data=withdraw_data['data'])
    # assert r.json()['status'] == withdraw_data['expect']['status']
    # assert r.json()['code'] == withdraw_data['expect']['code']
    res = mock.Mock(return_value={"status": 1, "code": 10001})
    withdraw_data = {"mobilephone": 15288899999, "amount": 9999}
    r = requests.post(url, data=withdraw_data)

    assert res['status'] == 1
    assert res['code'] == "10001"