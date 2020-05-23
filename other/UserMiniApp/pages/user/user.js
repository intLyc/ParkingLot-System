// pages/user/user.js
var app = getApp();
Page({
  data: {
    UID: app.globalData.UID,
    CID: '没有绑定',
    User: {},
  },
  onShow: function (options) {
    this.setData({
      UID: app.globalData.UID
    })
    this.bindCID();
    this.bindUser();
  },
  bindCID: function () {
    var that = this;
    wx.request({ //获取CID
      url: app.globalData.ipname +'getUserCar',
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      data: { //发送的数据
        UID: app.globalData.UID
      },
      success: function (res) {
        //success
        var result = res.data
        console.log(result); //打印请求返回的结果
        if (result) { //返回结果
          that.setData({
            CID: result.CID
          })
        } else {
          that.setData({
            CID: '没有绑定'
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
  bindUser: function () {
    var that = this;
    wx.request({ //获取车位
      url: app.globalData.ipname +'getUser',
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      data: { //发送的数据
        UID: app.globalData.UID
      },
      success: function (res) {
        //success
        var result = res.data
        console.log(result); //打印请求返回的结果
        if (result) { //返回结果
          that.setData({
            User: result
          })
        } else {
          that.setData({
            User: {}
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
  bindcgCar: function () {
      wx.navigateTo({
        url: './cgCar/cgCar'
      })
  },
  bindcgUser: function () {
    wx.navigateTo({
      url: './cgInfo/cgInfo'
    })
  },
  bindcgBalance: function () {
    wx.navigateTo({
      url: './cgBalance/cgBalance'
    })
  }
})