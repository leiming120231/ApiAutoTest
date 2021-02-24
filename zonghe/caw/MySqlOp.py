'''
操作Mysql数据库的方法
'''
import pymysql

from zonghe.caw.DataRead import read_ini


def connect(db_info):
    host = db_info['host']
    port = db_info['port']
    user = db_info['user']
    pwd = db_info['pwd']
    database = db_info['name']
    try:
        conn = pymysql.connect(host=host, user=user, password=pwd, database=database, port=port,charset='utf8')
        print("连接数据库成功")
        return conn
    except Exception as e:
        print(f"连接数据库失败，异常信息为：{e}")

def disconnect(conn):
    '''
    断开连接
    conn：
    :return:
    '''
    try:
        conn.close()
    except Exception as e:
        print(f"断开数据库连接失败，异常信息为：{e}")

def excute(conn, sql):
    try:
        cursor = conn.cursor() # 获取游标，类似java中的statment
        cursor.execute(sql) # 执行sql语句
        conn.commit() # 提交
        cursor.close() # 关闭游标
    except Exception as e:
        print(f"执行sql语句失败，异常信息为：{e}")

def delete_user(db_info, mobilephone):
    '''
    根据手机号码删除用户
    :param db_info:
    :param mobilephone:
    :return:
    '''
    # 连接数据库
    conn = connect(db_info)
    # 调用执行sql语句
    excute(conn, f"delete from member where mobilephone = {mobilephone};")
    # 断开数据库
    disconnect(conn)

# 测试代码，用完删除
if __name__ == '__main__':
    # 调用read_ini方法读取db_info
    # db_info = read_ini(r"\test_env\env.ini", "db_info")
    # print(db_info)
    # print(type(db_info))
    db_info = {"host": "192.168.1.64", "port": 3306, "name": "apple", "user": "root", "pwd": "123456"}
    # 连接数据库
    conn = connect(db_info)
    # 调用执行sql语句
    excute(conn, "delete from member where mobilephone = 18786754662;")
    #
    delete_user(db_info, "18786754662")
    # 断开数据库
    disconnect(conn)
    print("断开")
