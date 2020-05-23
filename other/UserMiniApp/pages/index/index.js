//index.js
var app = getApp()

Page({
  data: {
    
  },
  //事件处理函数
  onLoad: function() {

  },
  modalChange: function(e) {
    this.setData({
      modalHidden: true
    })
  },
  bindUidInput: function(e) {
    app.globalData.UID = e.detail.value
  },
  bindUpswdInput: function(e) {
    app.globalData.Upswd = e.detail.value
  },
  bindButtonLogin: function() {
    if (app.globalData.UID && app.globalData.Upswd) { // 当ID和密码都有内容时
      wx.request({
        url: app.globalData.ipname +'signIn',
        method: 'GET',
        header: {
          'Content-Type': 'application/json'
        },
        data: { //发送的数据
          UID: app.globalData.UID,
          Upswd: app.globalData.Upswd
        },
        success: function(res) {
          //success
          var result = res.data.result
          console.log(result); //打印请求返回的结果
          if (result) { //结果为true
            wx.showModal({
              title: '成功！',
              content: '用户名和密码正确',
              success(res) {
                if (res.confirm) {
                  wx.switchTab({
                    url: '../search/search'
                  })
                } else if (res.cancel) {
                  console.log('用户点击取消')
                }
              }
            })
          } else {
            wx.showModal({
              title: '失败！',
              content: '用户名或密码错误',
            })
          }
        },
        fail: function(res) {
          //failed
          wx.showModal({
            title: '失败！',
            content: '请求失败',
          })
        },
        complete: function(res) {
          //complete
        }
      })
    } else {
      wx.showModal({
        title: '失败！',
        content: '请输入ID和密码',
      })
    }
  },
  bindButtonLogout: function() {
    if (app.globalData.UID && app.globalData.Upswd) { //当ID和密码都有内容时
      wx.request({
        url: app.globalData.ipname +'signUp',
        method: 'GET',
        header: {
          'Content-Type': 'application/json'
        },
        data: { //发送的数据
          UID: app.globalData.UID,
          Upswd: app.globalData.Upswd
        },
        success: function(res) {
          //success
          var result = res.data.result
          console.log(result); //打印请求返回的结果
          if (result) { //结果为true
            wx.showModal({
              title: '成功！',
              content: '注册成功',
              success(res) {
                if (res.confirm) {
                  wx.switchTab({
                    url: '../search/search'
                  })
                } else if (res.cancel) {
                  console.log('用户点击取消')
                }
              }
            })
          } else {
            wx.showModal({
              title: '失败！',
              content: '用户名已存在',
            })
          }
        },
        fail: function(res) {
          //failed
          wx.showModal({
            title: '失败！',
            content: '请求失败',
          })
        },
        complete: function(res) {
          // complete
        }
      })
    } else {
      wx.showModal({
        title: '失败！',
        content: '请输入ID和密码',
      })
    }
  },
})