'''
1.上传文件的接口，上传1M的文件，上传2G的文件，耗时不一样差别很大，默认的超时时间不用时，可以设置接口超时时间
2. 接口性能测试，看接口是否能在某个时间内返回。
'''

import requests

j=0
for i in range(10):
    try:
        r = requests.get("http://jy001:8081/futureloan/mvc/api/member/list", timeout=0.02) #0.01=10ms
        print(r.text)

    except Exception as e:
        print(e)
        j=j+1
print(j)

