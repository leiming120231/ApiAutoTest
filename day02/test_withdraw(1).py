'''
# 使用注册完的用户登录
# 注册用户>>登录>>充值1000>>取现100
'''
import mock
import requests

# post功能
def commonpost(url, data):
    r = requests.post("http://jy001:8081/futureloan/mvc/api/%s"%url, data)
    return r.json()

# 测试注册功能用例
def test_register():
    url = "member/register"
    register_data={"mobilephone": 15288877777, "pwd": "123456"}
    # 调用注册功能并传参
    rjson = commonpost(url, register_data)
    # 断言response结果判别用例是否执行成功
    assert rjson['status'] == 1
    assert rjson['code'] == "10001"

# 测试登陆功能
def test_login():
    url = "member/login"
    login_data ={"mobilephone": 15288877777, "pwd": "123456"}
    rjson = commonpost(url, data=login_data)
    assert rjson['status'] == 1
    assert rjson['code'] == "10001"

# 测试充值功能
def test_recharge():
    url = "member/recharge"
    recharge_data = {"mobilephone": 15288877777, "amount": 88888}
    rjson = commonpost(url, data=recharge_data)
    assert rjson['status'] == 1
    assert rjson['code'] == "10001"

# 测试提现功能
def test_withdraw():
    url = "member/withdraw"
    commonpost = mock.Mock(return_value={"status": 1, "code": 10001})
    withdraw_data = {"mobilephone": 15288877777, "amount": 9999}
    rjson = commonpost(url, data=withdraw_data)
    assert rjson['status'] == 1
    assert rjson['code'] == 10001