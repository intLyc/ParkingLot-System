// pages/user/cgUser/cgUser.js
var app = getApp()

Page({
  data: {

  },
  //事件处理函数
  onLoad: function () {

  },
  modalChange: function (e) {
    this.setData({
      modalHidden: true
    })
  },
  bindUnameInput: function (e) {
    app.globalData.Uname = e.detail.value
  },
  bindUphoneInput: function (e) {
    app.globalData.Uphone = e.detail.value
  },
  bindButtonYes: function () {
    wx.request({
      url: app.globalData.ipname +'changeInfo',
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      data: { //发送的数据
        UID: app.globalData.UID,
        Uname: app.globalData.Uname,
        Uphone: app.globalData.Uphone
      },
      success: function (res) {
        //success
        wx.showModal({
          title: '成功！',
          content: '修改成功',
          success(res) {
            if (res.confirm) {
              wx.switchTab({
                url: '../user'
              })
            } else if (res.cancel) {
              wx.switchTab({
                url: '../user'
              })
            }
          }
        })
      },
      fail: function (res) {
        //failed
        wx.showModal({
          title: '失败！',
          content: '请求失败',
        })
      },
      complete: function (res) {
        //complete
      }
    })
  },
  bindButtonNo: function () {
    wx.switchTab({
      url: '../user'
    })
  },
})
