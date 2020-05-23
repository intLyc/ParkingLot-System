// pages/user/cgBalance/cgBalance.js
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
  bindBalanceInput: function (e) {
    app.globalData.Balance = e.detail.value
  },
  bindButtonYes: function () {
    wx.request({
      url: app.globalData.ipname +'charge',
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      data: { //发送的数据
        UID: app.globalData.UID,
        Balance: app.globalData.Balance
      },
      success: function (res) {
        //success
        wx.showModal({
          title: '成功！',
          content: '充值成功',
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