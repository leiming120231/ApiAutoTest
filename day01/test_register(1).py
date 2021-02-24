'''
测试注册功能
'''
import requests

# 验证参数手机号为空时，接口返回结果是否正确。

def test_register_phonenull():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "", "pwd": "123456", "regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20103"
    assert rjson["msg"] == "手机号不能为空"

# 验证不传手机号码时，接口返回结果是否正确。
def test_register_phonemiss():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = { "pwd": "123456", "regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20103"
    assert rjson["msg"] == "手机号不能为空"

# 验证参数手机号超长时，接口返回结果是否正确。
def test_register_phonelong():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "1888888888888", "pwd": "123456", "regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20109"
    assert rjson["msg"] == "手机号码格式不正确"

# 验证参数手机号位数不足时，接口返回结果是否正确。
def test_register_phoneshort():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "188", "pwd": "123456", "regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20109"
    assert rjson["msg"] == "手机号码格式不正确"

# 验证参数手机号已注册时，接口返回结果是否正确。
def test_register_phoneexist():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "15129938653", "pwd": "123456", "regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20110"
    assert rjson["msg"] == "手机号码已被注册"

# 验证密码未传，接口返回结果是否正确。
def test_register_passwordmiss():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "19999999999", "regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20103"
    assert rjson["msg"] == "密码不能为空"

# 验证密码为空，接口返回结果是否正确。
def test_register_passwordnull():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "19999999999", "pwd": "","regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20103"
    assert rjson["msg"] == "密码不能为空"

# 验证密码超长，接口返回结果是否正确。
def test_register_passwordlong():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "19999999999", "pwd": "123456789012345678", "regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20108"
    assert rjson["msg"] == "密码长度必须为6~18"

# 验证密码位数不足，接口返回结果是否正确。
def test_register_passwordshort():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "19999999999", "pwd": "123","regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20108"
    assert rjson["msg"] == "密码长度必须为6~18"

# 验证手机号、密码为空，接口返回结果是否正确。
def test_register_pwdnull():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "18888888888", "pwd": "", "regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20103"
    assert rjson["msg"] == "密码不能为空"

# 验证不传手机号、密码，接口返回结果是否正确。
def test_register_pwdpnemiss():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"regname": "leiming001"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 0
    assert rjson["code"] == "20103"
    assert rjson["msg"] == "手机号不能为空"

# 验证用户名为空，接口返回结果是否正确。
def test_register_rnamenull():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "18889098765", "pwd": "123456", "regname": ""}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 1
    assert rjson["code"] == "10001"

# 验证不传用户名，接口返回结果是否正确。
def test_register_rnamemiss():
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "18886540987", "pwd": "123456"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    assert rjson["status"] == 1
    assert rjson["code"] == "10001"

# 验证正确注册，接口返回结果是否正确。
def test_register_success():
    # try:
    # 测试注册接口
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs = {"mobilephone": "14576987654", "pwd": "123456", "regname": "尼古拉斯赵四"}
    r = requests.post(url, data=cs)
    rjson = r.json()
    print(rjson)
    # except Exception as e:
    #     print(e)
    assert rjson["status"] == 1
    assert rjson["code"] == "10001"


