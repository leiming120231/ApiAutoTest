class TestLogin:
    def test_001(self,login): #login的前置
        print("注册用例1")
    def test_002(self,db,login):  #db的前置
        print("注册用例2")
    def test_003(self):
        print("注册用例3")   #login、db的后置