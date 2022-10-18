import pymysql

def Connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='quiz_app',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn

