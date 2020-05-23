# -*- coding:utf-8 -*-
# ManagementSystem的路由

from flask import request
from app import app
from . import database
import pymysql
import json
from . import recognize

rec = recognize.Rec()  # 获取识别对象


@app.route('/getRecognize', methods=['POST', 'GET'])
def getRecognize():
    '''获取识别结果'''
    # 获取图片
    img = request.files['file']
    file_path = './app/static/image/' + img.filename  # 部署到服务器要改成绝对路径
    img.save(file_path)
    cid, confidence = rec.getPredict(file_path)
    j = {}
    j['CID'] = cid
    j['confidence'] = confidence
    j = json.dumps(j)
    return j


@app.route('/getLotNum', methods=['POST', 'GET'])
def getLotNum():
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


@app.route('/getLotCars', methods=['POST', 'GET'])
def getLotCars():
    '''获取库内车辆信息'''
    db, cursor = database.connect_mysql()

    # 数据库
    sql = "SELECT LotCar.CID,UserCar.UID,LotCar.Intime FROM LotCar LEFT JOIN UserCar ON LotCar.CID = UserCar.CID"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        fields = cursor.description  # 获取字段名
        results = []
        for i in data:
            result = {}
            result[fields[0][0]] = i[0]
            result[fields[1][0]] = i[1]
            result[fields[2][0]] = str(i[2])
            results.append(result)

        j = json.dumps(results)
        return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/getRecords', methods=['POST', 'GET'])
def getRecords():
    '''获取交易记录'''
    db, cursor = database.connect_mysql()

    # 数据库
    sql = "SELECT RID,CID,UID,Intime,Outtime,Cost FROM Record"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        fields = cursor.description  # 获取字段名
        results = []
        for i in data:
            result = {}
            result[fields[0][0]] = i[0]
            result[fields[1][0]] = i[1]
            result[fields[2][0]] = i[2]
            result[fields[3][0]] = str(i[3])
            result[fields[4][0]] = str(i[4])
            result[fields[5][0]] = i[5]
            results.append(result)

        j = json.dumps(results)
        return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/getUsers', methods=['POST', 'GET'])
def getUsers():
    '''获取用户信息'''
    db, cursor = database.connect_mysql()

    # 数据库
    sql = "SELECT User.UID, UserCar.CID, User.Uname, User.Uphone, User.Balance FROM User LEFT JOIN UserCar ON User.UID = UserCar.UID"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        fields = cursor.description  # 获取字段名
        results = []
        for i in data:
            result = {}
            result[fields[0][0]] = i[0]
            result[fields[1][0]] = i[1]
            result[fields[2][0]] = i[2]
            result[fields[3][0]] = i[3]
            result[fields[4][0]] = i[4]
            results.append(result)

        j = json.dumps(results)
        return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/getUpswd', methods=['POST', 'GET'])
def getUpswd():
    '''获取密码'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")

    sql = "SELECT Upswd FROM User WHERE (UID = '%s')" % (uid)
    try:
        cursor.execute(sql)  # 执行
        data = cursor.fetchall()  # 获取查询结果
        fields = cursor.description  # 获取字段名

        result = {}
        result[fields[0][0]] = data[0][0]

        j = json.dumps(result)  # 转为json
        return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/signUpUser', methods=['POST', 'GET'])
def signUpUser():
    '''用户注册'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    upswd = request.args.get("Upswd")
    uname = request.args.get("Uname")
    uphone = request.args.get("Uphone")
    balance = request.args.get("Balance")

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
            sql = "INSERT INTO User (UID, Upswd, Uname, Uphone, Balance) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
                uid, upswd, uname, uphone, balance)
            cursor.execute(sql)
            db.commit()
            j = '{"result": true}'
            return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/chargeBalance', methods=['POST', 'GET'])
def chargeBalance():
    '''充值'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    balance = request.args.get("Balance")

    sql = "SELECT UID, Balance FROM User WHERE (UID = '%s')" % (uid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            if not data[0][1]:
                nowBal = 0
            else:
                nowBal = float(data[0][1])
            balance = float(balance) + nowBal

            sql = "UPDATE User SET Balance = '%f' WHERE (UID = '%s')" % (
                balance, uid)
            cursor.execute(sql)
            db.commit()
            j = '{"result": true}'
            return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/changeUser', methods=['POST', 'GET'])
def changeUser():
    '''用户数据修改'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    upswd = request.args.get("Upswd")
    uname = request.args.get("Uname")
    uphone = request.args.get("Uphone")

    # 数据库
    sql = "UPDATE User SET Upswd = '%s', Uname = '%s', Uphone = '%s' WHERE (UID = '%s')" % (
        upswd, uname, uphone, uid)
    try:
        cursor.execute(sql)
        db.commit()
        j = '{"result": true}'
        return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/changeUserCar', methods=['POST', 'GET'])
def changeUserCar():
    '''修改车牌号'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    cid = request.args.get("CID")

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
        database.close_mysql(db, cursor)


@app.route('/delRecord', methods=['POST', 'GET'])
def delRecord():
    '''删除记录'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    rid = request.args.get("RID")
    # 数据库
    sql = "DELETE FROM Record WHERE (RID = '%s')" % (rid)
    try:
        cursor.execute(sql)
        db.commit()
        j = '{"result": true}'
        return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/delUser', methods=['POST', 'GET'])
def delUser():
    '''删除用户与车辆绑定'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    uid = request.args.get("UID")
    cid = request.args.get("CID")
    # 数据库
    sql = "SELECT CID FROM LotCar WHERE CID = '%s'" % (cid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:  # 正在车库
            j = '{"result": false}'
            return j
        else:
            sql = "DELETE FROM UserCar WHERE (UID = '%s')" % (uid)
            cursor.execute(sql)
            db.commit()
            sql = "DELETE FROM User WHERE (UID = '%s')" % (uid)
            cursor.execute(sql)
            db.commit()
            j = '{"result": true}'
            return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/letCarIn', methods=['POST', 'GET'])
def letCarIn():
    '''车辆入库'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    cid = request.args.get("CID")
    # 数据库
    sql = "SELECT CID FROM LotCar WHERE CID='%s'" % (cid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        # 如果查询到数据
        if data:  # 已在库中
            j = '{"result": false}'
            return j
        else:
            sql = "INSERT INTO LotCar (CID) VALUES ('%s')" % (cid)
            cursor.execute(sql)
            db.commit()
            j = '{"result": true}'
            return j
    finally:
        database.close_mysql(db, cursor)


@app.route('/letCarOut', methods=['POST', 'GET'])
def letCarOut():
    '''车辆出库'''
    db, cursor = database.connect_mysql()

    # 获取json数据
    cid = request.args.get("CID")
    cost = request.args.get("Cost")
    # 数据库
    sql = "SELECT CID FROM LotCar WHERE CID='%s'" % (cid)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        # 如果查询到数据
        if not data:  # 不在库中
            j = '{"result": false}'
            return j
        else:
            sql = "INSERT INTO Record (CID,Cost) VALUES ('%s','%s')" % (
                cid, cost)
            cursor.execute(sql)
            db.commit()
            j = '{"result": true}'
            return j
    finally:
        database.close_mysql(db, cursor)
