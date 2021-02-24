'''
测试注册功能
'''

import requests,random,pytest
cs = [
    # 密码长度为5
    {"data": {"mobilephone": 1801234567, "pwd": "12345"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    # 密码长度超过18
    {"data": {"mobilephone": 1801234567, "pwd": "12345678901234567890"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    # 密码为空
    {"data": {"mobilephone": 1801234567, "pwd": ""},
     "expect": {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
    # 手机号码格式不正确
    {"data": {"mobilephone": 180123456, "pwd": "123456"},
     "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}]

# 手机号 11位，10位，12位
@pytest.fixture(params= ["17658976542","17867865436","198798765433"])
def get_phone(request):
    return request.param

# 密码 5位 4位 6位 null
@pytest.fixture(params= ["123456","12345","1234567,"""])
def get_pwd(request):
    return request.param

# 用户名 leiming null
@pytest.fixture(params= ["leiming",""])
def get_regname(request):
    return request.param

# 生成用户名密码用户名字典
@pytest.fixture()
def register_data(get_phone, get_pwd, get_regname):
    return {"mobilephone": get_phone, "pwd": get_pwd, "regname": get_regname}


# 仅验证登录成功功能。
def test_register(register_data):
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    # cs = {"mobilephone": "18886540987", "pwd": "123456"}
    r = requests.post(url, data=register_data)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 1
    # assert rjson["code"] == "10001"













# # 验证正确注册，接口返回结果是否正确。
# def test_register_success():
#     # try:
#     # 测试注册接口
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {"mobilephone": "14576987654", "pwd": "123456", "regname": "尼古拉斯赵四"}
#     r = requests.post(url, data=cs)
#     rjson = r.json()
#     print(rjson)
#     # except Exception as e:
#     #     print(e)
#     assert rjson["status"] == 1
#     assert rjson["code"] == "10001"


