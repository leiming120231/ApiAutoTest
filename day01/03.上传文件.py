import requests

# 接口路径
url = "http://www.httpbin.org/post"
# 本地文件上传
file = "d:/test.png"
# rb 二进制只读方式打开
with open(file, mode='rb') as f:

    cs = {"filename": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    print(r.text)
print("================================================")

# 添加车辆上传图片接口路径
url = "http://127.0.0.1:8080/carRental/file/uploadFile.action"
# 本地文件上传
file = "d:/test.png"
# rb 二进制只读方式打开
with open(file, mode='rb') as f:

    cs = {"mf": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    print(r.text)
    # 获取图片的路径
    uploadPath = r.json()['data']['src']

# 租车系统，添加车辆
url = "http://127.0.0.1:8080/carRental/car/addCar.action"
# 接口文档中对接口描述不清晰
# 通过界面操作接口对应的功能，抓包（Fiddler、浏览器的F12）看
cs = {
    "carnumber": "陕A444444", "cartype": "比亚迪",
    "color": "白色", "carimg": uploadPath,
    "description": "2020年新车", "price": 200000,
    "rentprice": 1000, "deposit": 500,
    "isrenting": 0
}
# 使用脚本添加的车辆，中文字符乱码，但是用界面添加的车辆，不会有乱码
# 分别抓脚本的包与界面的包，对比差异。界面设置了charset=UTF-8，但是脚本未设置导致。
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
r=requests.post(url, data=cs, headers=head)
print(r.text)


 # http://127.0.0.1:8080/carRental/file/downloadShowFile.action