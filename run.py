# -*- coding:utf-8 -*-
# flask运行

from app import app

if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()  # 启动服务器
