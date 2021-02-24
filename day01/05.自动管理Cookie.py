'''
requests.session 来保持状态。自动管理过程中产生的cookie
'''

import requests

# requests.get 不用
#自动管理获取session，先requests获取session，后面全部用这个来访问
s = requests.Session()
print(s.cookies)
print("登录前的cookie：", requests.utils.dict_from_cookiejar(s.cookies))
# 登录接口
url = "https://www.bagevent.com/user/login"
cs = {
    "access_type": "1",
    "loginType": "1",
    "emailLoginWay": "0",
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": "1"
}
r = s.post(url, data=cs)
# print(r.text)
print('======================================================================================================================================')
print("登录后的cookie：", requests.utils.dict_from_cookiejar(s.cookies))

# dashboard接口
r = s.get("https://www.bagevent.com/account/dashboard")
print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

# 退出登录的接口
r = s.get("https://www.bagevent.com/user/login_out")
print("退出登录后的cookie：", requests.utils.dict_from_cookiejar(s.cookies))
