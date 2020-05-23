# -*- coding:utf-8 -*-
# templates html文件定向

from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Lot/lotCar.html')
def lot_lotCar():
    return render_template('Lot/lotCar.html')


@app.route('/Lot/record.html')
def lot_record():
    return render_template('Lot/record.html')


@app.route('/Lot/user.html')
def lot_user():
    return render_template('Lot/user.html')


@app.route('/Lot/signUp.html')
def lot_singUp():
    return render_template('Lot/signUp.html')


@app.route('/Lot/user/changeUser.html')
def lot_user_changeUser():
    return render_template('Lot/user/changeUser.html')


@app.route('/Lot/user/changeUserCar.html')
def lot_user_changeUserCar():
    return render_template('/Lot/user/changeUserCar.html')


@app.route('/Lot/user/chargeBalance.html')
def lot_user_chargeBalance():
    return render_template('/Lot/user/chargeBalance.html')


@app.route('/Regist/in.html')
def regist_in():
    return render_template('/Regist/in.html')


@app.route('/Regist/out.html')
def regist_out():
    return render_template('/Regist/out.html')


@app.route('/Regist/autoIn.html')
def regist_autoIn():
    return render_template('/Regist/autoIn.html')


@app.route('/Regist/autoOut.html')
def regist_autoOut():
    return render_template('/Regist/autoOut.html')
