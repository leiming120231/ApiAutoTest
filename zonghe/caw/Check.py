import pytest_check as check
'''
# 检查结果
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']
'''

def equla(real, expect, keys):
    '''
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']
    简化为
    Ckeck.equal(r.json(), fail_data['expect'], 'code,status,msg')
    检查两个字典中，key和value是否一致
    不推荐直接接判等，r.json()== fail_data['expect']
    1.不关键机械能
    :param real: 实际结果，字典格式
    :param expect: 预期结果，字典格式
    :param keys: 对比的key
    :return:
    '''
    ks = keys.split(",")  #字符串在，处切割
    for k in ks: # 遍历列表
        r = str(real.get(k))
        e = str(expect.get(k))
        try:
            check.equal(r,e)
            print(f"检验{k}成功")
        except Exception as e:
            print(f"检验{k}失败")