'''
# 使用注册完的用户登录
# 注册用户>>登录>>充值1000>>取现100
'''
import mock
import requests,pytest

cs = [
    # 注册数据
    {"data":
         {"url": "member/register", "rundata": {"mobilephone": 15277650000, "pwd": "123456"}},
     "expect":
         {"status": 1, "code": "10001"}},
    # 登录数据
    {"data":
         {"url": "member/login", "rundata": {"mobilephone": 15277650000, "pwd": "123456"}},
     "expect":
         {"status": 1, "code": "10001"}},
    # 充值数据
    {"data":
         {"url": "member/recharge", "rundata": {"mobilephone": 15277650000, "amount": 88888}},
     "expect":
         {"status": 1, "code": "10001"}},
    # 提现数据
    {"data":
         {"url": "member/withdraw", "rundata": {"mobilephone": 15277650000, "amount": 9999}},
     "expect":
         {"status": 1, "code": "10001"}},
    ]

# 循环取cs中取数据，每次取一个
@pytest.fixture(params=cs)
def csdata(request):  # 固定写法
    return request.param  # 固定写法

# post功能
def commonpost(url, data):
    r = requests.post("http://jy001:8081/futureloan/mvc/api/%s"%url, data)
    return r.json()


def test_comm(csdata):
        rjson = commonpost(csdata['data']['url'], csdata['data']['rundata'])
        assert rjson['status'] == csdata['expect']['status']
        assert rjson['code'] == csdata['expect']['code']


def test_withdraw(csdata):
    # mock.Mock创建一个返回结果
    commonpost = mock.Mock(return_value={"status": 1, "code": "10001"})
    rjson = commonpost(csdata['data']['url'], csdata['data']['rundata'])
    assert rjson['status'] == csdata['expect']['status']
    assert rjson['code'] == csdata['expect']['code']
