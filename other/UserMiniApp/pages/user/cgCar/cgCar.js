// pages/user/cgCar/cgCar.js
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
  bindCarInput: function (e) {
    app.globalData.CarInput = e.detail.value
  },
  bindButtonYes: function () {
    wx.request({
      url: app.globalData.ipname + 'changeCar',
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      data: { //发送的数据
        UID: app.globalData.UID,
        CID: app.globalData.CarInput
      },
      success: function (res) {
        //success
        var result = res.data.result
        if (result) {
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
        } else {
          wx.showModal({
            title: '失败！',
            content: '车在库中，或该车牌号已被绑定',
          })
        }
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