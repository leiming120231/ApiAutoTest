import requests
# 租车系统，删除车辆
url = "http://127.0.0.1:8080/carRental/car/deleteBatchCar.action"
# 接口文档中对接口描述不清晰
# 通过界面操作接口对应的功能，抓包（Fiddler、浏览器的F12）看
# cs = {
#     "ids": "陕A522222", 'code': 0, 'msg': '删除成功'
# }

cs = {
    "ids": "陕A622222", 'code': 0, 'msg': '删除成功'
}
# 使用脚本添加的车辆，中文字符乱码，但是用界面添加的车辆，不会有乱码
# 分别抓脚本的包与界面的包，对比差异。界面设置了charset=UTF-8，但是脚本未设置导致。
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}

# Fiddler 抓脚本的包，设置代理
proxy = {
    "http": "http://127.0.0.1:8888", #http协议，使用这个代理
    "https": "http://127.0.0.1:8888" #https协议，使用这个代理
}
def test_deleteBatchCar():
    r = requests.post(url, data=cs, headers=head, proxies = proxy)
    rjson = r.json()
    print(rjson)
    assert  rjson['code'] == cs['code']
    assert rjson['msg'] == cs['msg']