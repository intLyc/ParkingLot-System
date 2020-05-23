// pages/search/search.js
var app = getApp();
Page({
  data: {
    background: ['green', 'red', 'blue', 'yellow', 'gray'],
    LotNum: 0,
    Car: {},
    items: {},
    opened: false
  },
  onShow: function(options) {
    this.bindLotNum();
    this.bindCarInfo();
  },
  bindLotNum: function() {
    var that = this;
    wx.request({ //获取车位
      url: app.globalData.ipname +'getLot',
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      data: { //发送的数据
      },
      success: function(res) {
        //success
        var result = res.data
        console.log(result); //打印请求返回的结果
        if (result) { //返回结果
          that.setData({
            LotNum: result.Num
          })
        } else {
          that.setData({
            LotNum: 0
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
  },
  bindCarInfo: function() {
    var that = this;
    wx.request({ //获取当前停车信息
      url: app.globalData.ipname +'getLotCar',
      method: 'GET',
      header: {
        'Content-Type': 'application/json'
      },
      data: { //发送的数据
        UID: app.globalData.UID
      },
      success: function(res) {
        //success
        var result = res.data
        console.log(result); //打印请求返回的结果
        if (result) { //返回结果
          that.setData({
            Car: result
          })
        } else {
          that.setData({
            Car: {}
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
  },
  bindRecordInfo: function() {
    var x = !this.data.opened;
    this.setData({
      opened: x
    })

    var that = this;
    wx.request({ //获取交易记录
      url: app.globalData.ipname +'getRecord',
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
            items: result
          })
        } else {
          that.setData({
            items: {}
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
  }
})