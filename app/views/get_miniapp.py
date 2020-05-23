# -*- coding:utf-8 -*-
# UerMiniAPP的路由

from flask import request
from app import app
from . import database
import pymysql
import json


@app.route('/signIn', methods=['POST', 'GET'])
def signIn():
    '''登陆'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    upswd = request.args.get("Upswd")
    # 数据库
    sql = "SELECT UID FROM User WHERE UID='%s' AND Upswd='%s'" % (uid, upswd)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        # 如果查询到数据
        if data:
            j = '{"result": true}'
            return j
        else:
            j = '{"result": false}'
            return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    '''注册'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    upswd = request.args.get("Upswd")
    # 数据库
    sql = "SELECT UID FROM User WHERE UID='%s'" % (uid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        # 如果查询到数据
        if data:  # 已注册
            j = '{"result": false}'
            return j
        else:
            sql = "INSERT INTO User (UID, Upswd, Balance) VALUES ('%s', '%s', '%s')" % (
                uid, upswd, '0')
            cursor.execute(sql)
            db.commit()
            j = '{"result": true}'
            return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/getLot', methods=['POST', 'GET'])
def getLot():
    '''获取车位库存'''
    db, cursor = database.connect_mysql()

    # 数据库
    sql = "SELECT Num FROM Lot WHERE LID='MAIN'"
    try:
        cursor.execute(sql)  # 执行
        data = cursor.fetchall()  # 获取查询结果
        if data:
            fields = cursor.description  # 获取字段名

            result = {}
            result[fields[0][0]] = data[0][0]

            j = json.dumps(result)  # 转为json
            return j
        else:
            return "false"
    finally:
        database.close_mysql(db, cursor)


@app.route('/getLotCar', methods=['POST', 'GET'])
def getLotCar():
    '''获取当前用户停车信息'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    # 数据库
    sql = "SELECT CID,Intime FROM LotCar WHERE CID=(SELECT CID FROM UserCar WHERE UID='%s')" % (
        uid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            fields = cursor.description  # 获取字段名

            result = {}
            result[fields[0][0]] = data[0][0]
            result[fields[1][0]] = str(data[0][1])

            j = json.dumps(result)  # 转为json
            return j
        else:
            return "false"
    finally:
        database.close_mysql(db, cursor)


@app.route('/getRecord', methods=['POST', 'GET'])
def getRecord():
    '''获取交易记录'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    # 数据库
    sql = "SELECT CID,Intime,Outtime,Cost FROM Record WHERE UID='%s'" % (uid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            fields = cursor.description  # 获取字段名
            name = []
            for i in fields:
                name.append(i[0])
            results = []
            for i in data:
                result = {}
                result[fields[0][0]] = i[0]
                result[fields[1][0]] = str(i[1])
                result[fields[2][0]] = str(i[2])
                result[fields[3][0]] = i[3]
                results.append(result)

            j = json.dumps(results)
            return j
        else:
            return "false"
    finally:
        database.close_mysql(db, cursor)


@app.route('/getUserCar', methods=['POST', 'GET'])
def getUserCar():
    '''获取当前用户绑定车牌号'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    # 数据库
    sql = "SELECT CID FROM UserCar WHERE UID='%s'" % (uid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            fields = cursor.description  # 获取字段名

            result = {}
            result[fields[0][0]] = data[0][0]

            j = json.dumps(result)  # 转为json
            return j
        else:
            return "false"
    finally:
        database.close_mysql(db, cursor)


@app.route('/getUser', methods=['POST', 'GET'])
def getUser():
    '''获取当前用户信息'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    # 数据库
    sql = "SELECT Uname,Uphone,Balance FROM User WHERE UID='%s'" % (uid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            fields = cursor.description  # 获取字段名

            result = {}
            result[fields[0][0]] = data[0][0]
            result[fields[1][0]] = data[0][1]
            result[fields[2][0]] = data[0][2]

            j = json.dumps(result)  # 转为json
            return j
        else:
            return "false"
    finally:
        database.close_mysql(db, cursor)


@app.route('/changeCar', methods=['POST', 'GET'])
def changeCar():
    '''修改车牌号'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    cid = request.args.get("CID")

    if cid == "undefined":  # 如果没有则删除
        sql = "DELETE FROM UserCar WHERE (UID = '%s')" % (uid)
        try:
            cursor.execute(sql)
            db.commit()
            j = '{"result": true}'
            return j
        finally:
            cursor.close()
            db.close()
    else:
        sql = "SELECT CID FROM LotCar WHERE CID = (SELECT CID FROM UserCar WHERE UID = '%s')" % (
            uid)
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:  # 正在车库
                j = '{"result": false}'
                return j
            else:
                # 查询车牌号是否存在
                sql = "SELECT CID FROM UserCar WHERE CID='%s'" % (cid)
                cursor.execute(sql)
                data = cursor.fetchall()
                if data:  # 已存在
                    j = '{"result": false}'
                    return j
                else:
                    sql = "SELECT UID FROM UserCar WHERE UID='%s'" % (uid)
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    # 如果查询到数据
                    if data:  # 已绑定，改变
                        sql = "UPDATE UserCar SET CID = '%s' WHERE (UID = '%s')" % (
                            cid, uid)
                        cursor.execute(sql)
                        db.commit()
                    else:  # 未绑定，添加
                        sql = "INSERT INTO UserCar (UID, CID) VALUES ('%s', '%s')" % (
                            uid, cid)
                        cursor.execute(sql)
                        db.commit()
                    j = '{"result": true}'
                    return j
        finally:
            cursor.close()
            db.close()


@app.route('/changeInfo', methods=['POST', 'GET'])
def changeInfo():
    '''修改用户信息'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    uname = request.args.get("Uname")
    uphone = request.args.get("Uphone")
    if uname == "undefined":
        uname = ""
    if uphone == "undefined":
        uphone = ""

    sql = "UPDATE User SET Uname = '%s', Uphone = '%s' WHERE (UID = '%s')" % (
        uname, uphone, uid)
    try:
        cursor.execute(sql)
        db.commit()
    finally:
        database.close_mysql(db, cursor)


@app.route('/charge', methods=['POST', 'GET'])
def charge():
    '''修改余额（充值）'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    balance = request.args.get("Balance")
    if balance == "undefined":
        balance = 0

    sql = "SELECT Balance FROM User WHERE (UID = '%s')" % (uid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            balance = float(balance) + float(data[0][0])

            sql = "UPDATE User SET Balance = '%f' WHERE (UID = '%s')" % (
                balance, uid)
            cursor.execute(sql)
            db.commit()
    finally:
        database.close_mysql(db, cursor)
