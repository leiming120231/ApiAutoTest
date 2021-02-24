'''
Cookie 用来识别用户
'''

import requests

# 没有登录调用，返回跳转到登录页面
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)
# 发送请求head加上Cookie
head ={
    "Cookie": '_ga=GA1.2.1091715867.1611731457; _gid=GA1.2.1244177955.1611731457; __auc=d59cc29017742ae75587fe73de2; MEIQIA_TRACK_ID=1ndtqCEZ0nNR5iLmfhH02iGjhXu; MEIQIA_VISIT_ID=1ndtq8WVCA7rnJNKDTKF1U4YISc; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611731457,1611731979,1611818374; __asc=5702146d17747dc94f89d43280f; BAGSESSIONID=c0c8e2d4-5774-460e-8fb4-35b03b6e185f; JSESSIONID=7FC97B28C4CEE8B0212CE64B51418D26; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611818554'}
r = requests.get(url, headers=head)
print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

'''
缺点：
    1.Cooki会失效，失效后需要重新获取
    2.登录后的每个接口，都需要带着Cookie
'''
