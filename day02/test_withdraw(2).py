'''
# 使用注册完的用户登录
# 注册用户>>登录>>充值1000>>取现100
'''
import mock
import requests

cs = [
    # 注册数据
    {"data":
         {"url": "member/register", "register_data": {"mobilephone": 15277654321, "pwd": "123456"}},
     "expect":
         {"status": 1, "code": "10001"}},
    # 登录数据
    {"data":
         {"url": "member/login", "login_data": {"mobilephone": 15277654321, "pwd": "123456"}},
     "expect":
         {"status": 1, "code": "10001"}},
    # 充值数据
    {"data":
         {"url": "member/recharge", "recharge_data": {"mobilephone": 15277654321, "amount": 88888}},
     "expect":
         {"status": 1, "code": "10001"}},
    # 提现数据
    {"data":
         {"url": "member/withdraw", "withdraw_data": {"mobilephone": 15277654321, "amount": 9999}},
     "expect":
         {"status": 1, "code": "10001"}},

    ]

# post功能
def commonpost(url, data):
    r = requests.post("http://jy001:8081/futureloan/mvc/api/%s"%url, data)
    return r.json()

# 测试注册功能用例
def test_register():
    url = cs[0]['data']['url']
    register_data = cs[0]['data']["register_data"]
    # 调用注册功能并传参
    rjson = commonpost(url, register_data)
    # 断言response结果判别用例是否执行成功
    assert rjson['status'] == cs[0]['expect']['status']
    assert rjson['code'] == cs[0]['expect']['code']

# 测试登陆功能
def test_login():
    url = cs[1]['data']['url']
    login_data = cs[1]['data']["login_data"]
    rjson = commonpost(url, data=login_data)
    assert rjson['status'] == cs[1]['expect']['status']
    assert rjson['code'] == cs[1]['expect']['code']

# 测试充值功能
def test_recharge():
    url = cs[2]['data']['url']
    recharge_data = cs[2]['data']["recharge_data"]
    rjson = commonpost(url, data=recharge_data)
    assert rjson['status'] == cs[2]['expect']['status']
    assert rjson['code'] == cs[2]['expect']['code']

# 测试提现功能
def test_withdraw():
    url = cs[3]['data']['url']
    commonpost = mock.Mock(return_value={"status": 1, "code": "10001"})
    withdraw_data = cs[3]['data']["withdraw_data"]
    rjson = commonpost(url, data=withdraw_data)
    assert rjson['status'] == cs[3]['expect']['status']
    assert rjson['code'] == cs[3]['expect']['code']