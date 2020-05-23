# -*- coding:utf-8 -*-
# 数据库信息存储

import pymysql

# 服务器
# Loginfo = {
#     'USER': 'root',
#     'PSWD': 'tcqkjjhhh123',
#     'HOST': '172.16.0.5',
#     'PORT': 3306,
#     'DBNAME': 'ParkingLot'
# }

# 本地测试
Loginfo = {
    'USER': 'root',
    'PSWD': '0017',
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'DBNAME': 'ParkingLot'
}


def connect_mysql():
    '''连接数据库'''
    db = pymysql.connect(
        host=Loginfo['HOST'],
        port=Loginfo['PORT'],
        user=Loginfo['USER'],
        passwd=Loginfo['PSWD'],
        db=Loginfo['DBNAME'],
        charset='utf8')
    cursor = db.cursor()
    return db, cursor


def close_mysql(db, cursor):
    '''断开数据库'''
    cursor.close()
    db.close()
