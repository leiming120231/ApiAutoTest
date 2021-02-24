'''
接口测试；
    使用requests中的get、post方法调用接口，检查返回值是否正确。
'''

import requests
# # 获取用户列表
# url="http://jy001:8081/futureloan/mvc/api/member/list"
# # 发送get请求
# r=requests.get(url)
# # 打印响应,文本格式的响应
# print(r.text)
# # 检查结果是否与预期相同
# assert r.status_code == 200
# assert r.reason == "OK"
# rjson = r.json()
# assert rjson['status'] == 1
# assert rjson['code'] == '10001'
# assert rjson['msg'] == '获取用户列表成功'
# # 响应头
# print(r.headers)

print('+++++++++++++++++++++++++++++++++++get请求带参数++++++++++++++++++++++++++++++++++++++++++++++++++')
# # 注册接口参数拼接在URL后面，多个参数用&连接
# url = "http://jy001:8081/futureloan/mvc/api/member/register"
#
# # 发送get请求
# r = requests.get(url)
# # 打印响应，文本格式
# print(r.text)
#
# # 转json格式
# rjson =r.json()
# assert rjson['status'] == 1
# assert rjson['code'] == '10001'



# 注册接口，使用[param传参
# url= "http://jy001:8081/futureloan/mvc/api/member/register"
# cs = {
#     "mobilephone":"18012345678",
#     "pwd":"123456",
#     "regname":"requsts_test"
# }
# r = requests.get(url,params=cs)
# print(r.text)
# rjson =r.json()
# assert rjson['status'] == 0
# assert rjson['code'] =='20110'
# assert rjson["msg"] =="手机号已被注册"


url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
cs = {
    "tel": "18192326887"
}
r=requests.get(url, params=cs)
print(r.text)
# print(r.json()) # 报错，因为返回的结果不是json格式
print('============================================================')
assert '陕西移动' in r.text


# assertIn('陕西移动',r.text,'断言失败！')  assertIn是unitest里专用的



