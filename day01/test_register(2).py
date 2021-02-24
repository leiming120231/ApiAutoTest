'''
测试注册功能
'''
import requests,random,pytest

cs = [
    {"data": {"mobilephone": 18766545678, "pwd": "123456", "regname": "leiming001"},
     "expect": {"status": 0,"code": "20108","data": None,"msg": "密码长度不必须为6~18"}
     },
    # 手机号码格式不正确
    {"data": {"mobilephone": 180123456, "pwd": "123456", "regname": "leiming001"},
     "expect": {"status": 0,"code": "20108","data": None, "msg": "密码长度不必须为6~18"}}
    ]

# 生成手机号
@pytest.fixture(params=cs)
def register_data(request):
    return request.param

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r

# 数据驱动的测试模型
# test_register 测试脚本、测试逻辑，测试数据与测试逻辑分离，相同的逻辑数据放到一起，实现一个脚本即可。
# 数据可以放到csv，xml，yaml..去维护
def test_register(register_data):
    # 测试注册接口
    print(f"测试数据: {register_data['data']}")
    print(f"测试数据: {register_data['expect']}")
    r = register(register_data['data'])
    print(f"实际结果:{r.text}")
    # rjson = r.json()
    # print(rjson)
    assert r.json()["status"] == register_data['except']['status']
    assert r.json()["code"] == register_data['except']['code']
    assert r.json()["msg"] == register_data['except']['msg']


# 注册用户>>登录>>充值1000>>取现100

