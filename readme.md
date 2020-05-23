# 智能停车场识别收费管理系统

> 作者：intLyc
>

### 项目文件夹

| 文件夹 | 内容                    |
| ------ | ----------------------- |
| app    | Web前后端               |
| other  | mysql数据库、微信小程序 |


### Web管理系统结构

```
├── app
│   ├── __init__.py
│   ├── static
│   │   ├── image                    #图片文件夹
│   │   ├── layui                    #layui库文件夹
│   │   ├── js 
│   │   │   └── ip_url.js            #存储路由ip的js
│   │   └── recmod                   #车牌识别模型文件夹
│   ├── templates                    #html文件夹
│   │   ├── index.html
│   │   ├── Lot                      #查询类页面
│   │   │   ├── lotCar.html
│   │   │   ├── record.html
│   │   │   ├── signUp.html
│   │   │   ├── user.html
│   │   │   └── user
│   │   │        ├── changeUser.html
│   │   │        ├── changeUserCar.html
│   │   │        └── chargeBalance.html
│   │   └── Regist                   #车辆进出类页面
│   │        ├── In.html
│   │        ├── Out.html
│   │        ├── autoIn.html
│   │        └── autoOut.html
│   └── views                        #py文件夹
│        ├── __init__.py
│        ├── database.py             #数据库信息
│        ├── html.py                 #html页面定位
│        ├── get_management.py       #管理系统后端路由
│        ├── get_miniapp.py          #小程序后端路由
│        ├── HyperLPRLite.py         #HyperLPR车牌识别
│        └── recognize.py            #车牌识别封装类
└── run.py                           #后端测试运行
```

### 微信小程序结构

```
├── app.js                           #全局js文件
├── app.json                         #微信小程序的管理json
├── app.wxss                         #全局样式
├── images                           #图片文件夹
├── pages                            #页面文件夹
│   ├── index                        #index页面
│   │   ├── index.js
│   │   ├── index.wxml
│   │   └── index.wxss
│   ├── search                       #search页面
│   │   ├── search.js
│   │   ├── search.wxml
│   │   └── search.wxss
│   └── user                         #user页面
│       ├── user.js
│       ├── user.wxml
│       ├── user.wxss
│       ├── cgInfo                   #修改信息页面
│       │   ├── cgInfo.j
│       │   ├── cgInfo.wxml
│       │   └── cgInfo.wxss
│       ├── cgCar                    #修改绑定车牌页面
│       │   ├── cgCar.js
│       │   ├── cgCar.wxml
│       │   └── cgCar.wxss
│       └── cgBalance                #充值页面
│            ├── cgBalance.js
│            ├── cgBalance.wxml
│            └── cgBalance.wxss
└── utils.js
```