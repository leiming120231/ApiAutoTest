import requests

# # 表单格式的数据：content-type：www-x-form-urlencoded,使用data传参
# # 登录接口
# url="http://jy001:8081/futureloan/mvc/api/member/login"
# cs = {
#     "mobilephone":"18012345678",
#      "pwd":"123456"
# }
# r=requests.post(url,data=cs)
# print(r.text)
# rjson = r.json()
# # assert rjson["status"] == 1
# # assert rjson["code"] == "10001"
# assert rjson["msg"] == "登录成功"
#
# print('============================================================')
# # json格式的数据：content-type：application,使用json传参.
#
# # httpbin.org是一个测试网站，不管发送什么类型的数据
# # 这个接口将发送的请求，封装成json格式返回
# url="http://www.httpbin.org/post"
# cs = {
#     "mobilephone":"18012345678",
#      "pwd":"123456"
# }
# r=requests.post(url,data=cs)
# print("data传参===",r.text)
# r=requests.post(url,json=cs)
# print("json传参===",r.text)

# 租车系统添加一辆车辆
url="http://127.0.0.1:8080/carRental/car/addCar.action"
cs = {"carnumber": "陕A922222",
    "carimg": "images/defaultcarimage.jpg",
     "cartype": "SUV",
      "color": "黑色",
      "description": "路虎行政版",
    "deposit": 49999,
      "price": 999999,
      "rentprice": 9999,
     "isrenting": 0,
}
head = {
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
# Fiddler 抓脚本的包，设置代理
proxy = {
    "http": "http://127.0.0.1:8888",  #http协议，使用这个代理
    "https": "http://127.0.0.1:8888"  #https协议，使用这个代理
}
r = requests.post(url, data=cs, headers=head)
print(r.text)

# {"code":0,"msg":"添加成功"}
rjson = r.json()
assert rjson["code"] == 0
assert rjson["msg"] == '添加成功'