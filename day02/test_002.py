'''
测试前置和后置
    类和方法级别的
'''

class TestTClass:
    def setup_class(self):
        print("类里所有用例前执行一次")

    def teardown_class(self):
        print("类里所有用例后执行一次")

    def setup_method(self):
        print("每个方法前执行")

    def teardown_method(self):
        print("每个方法后执行一次")

    def test_001(self):# 不需要前置和后置 比如查询类的，不需要登陆退出
        print("用例1")

    def test_002(self): # 需要前置和后置 比如修改类的，需要登陆退出
        print("用例2")

    def test_003(self):
        print("用例3")

