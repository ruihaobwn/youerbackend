var app = getApp();
var request = require('../../utils/request.js')

Page({
  data: {
    "carousel1": {
      "style": "height:370rpx;width:750rpx;",
      "content": [],
      "customFeature": {
        "autoplay": true,
        "interval": 2,
        "indicatorActiveColor": "#000000",
        "indicatorColor": "rgba(0, 0, 0, .3)"
      }
    },
    "free_vessel3": {
      "style": "width:750rpx;height:105rpx;background-color:rgb(255, 255, 255);margin-top:12rpx;",
      "content": [{
        "style": "color:rgb(51, 51, 51);font-size:37.5rpx;font-weight:bold;height:45rpx;line-height:45rpx;position:absolute;left:50rpx;top:33rpx;",
        "content": "英语教具"
      }]
    },
    "free_vessel4": {
      "style": "width:640rpx;background-color:rgb(255, 255, 255);margin-left:55rpx;",
      "content": []
    },
    "free_vessel5": {
      "style": "width:750rpx;height:105rpx;background-color:rgb(255, 255, 255);margin-top:12rpx;",
      "content": [{
        "style": "color:rgb(51, 51, 51);font-size:37.5rpx;font-weight:bold;height:45rpx;line-height:45rpx;position:absolute;left:50rpx;top:33rpx;",
        "content": "汉字教具"
      }]
    },
    "free_vessel6": {
      "style": "width:640rpx;background-color:rgb(255, 255, 255);margin-left:55rpx;",
      "content": []
    }
  },

  // navigateTo Card Page
  openCard: function(event){
    const cardType_id=event.currentTarget.dataset.id
    wx.navigateTo({
      url: '/pages/subpage/cardType/cardType?id=' + cardType_id
    })
  },

  onLoad: function () {
    request.sendRequest({
      url: '/poster',
      data: {
        type: 'Card'
      },
      success: res => {
        const results = res.results
        const carousel = results.map((item) => {
          const oneItem = {};
          oneItem.pic = item.image;
          oneItem.name = item.name;
          return oneItem
        });
        this.setData({
          'carousel1.content': carousel
        })
      }
    })
    request.sendRequest({
      url: '/card/product_type',
      data:{
        sup_type: 'English'
      },
      success: res=>{
        const results = res.results
        const enType = results.map(item=>{
          const oneItem = {
            "style": "width:160rpx",
            "pic_style": "height:82rpx;width:82rpx;border-radius:20rpx",
            "text_style": "color:rgb(68, 68, 68);font-size:28rpx;"
          }
          oneItem.pic = item.image
          oneItem.text = item.sub_type
          oneItem.itemIndex = item.id
          return oneItem
        })
        this.setData({
          'free_vessel4.content': enType
        })
      }
    })
    request.sendRequest({
      url: '/card/product_type',
      data: {
        sup_type: 'Chinese'
      },
      success: res => {
        const results = res.results
        const cnType = results.map(item => {
          const oneItem = {
            "style": "width:160rpx",
            "pic_style": "height:82rpx;width:82rpx;",
            "text_style": "color:rgb(68, 68, 68);font-size:28rpx;"
          }
          oneItem.pic = item.image
          oneItem.text = item.sub_type
          oneItem.itemIndex = item.id
          return oneItem
        })
        this.setData({
          'free_vessel6.content': cnType
        })
      }
    })
  }
})