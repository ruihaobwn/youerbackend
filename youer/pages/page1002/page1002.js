var app = getApp();
var request = require('../../utils/request.js')

Page({
  data: {
    "carousel1": {
      "style": "height:370rpx;width:750rpx;",
      "content": [{
        "pic": "https: \/\/img.zhichiwangluo.com\/zcimgdir\/album\/file_5b6bf89c6233c.png",
        "name": "轮播1"
      }, {
        "pic": "https: \/\/img.zhichiwangluo.com\/zcimgdir\/album\/file_5b6bf89c6233c.png",
        "name": "轮播2"
      }],
      "customFeature": {
        "autoplay": true,
        "interval": 2,
        "indicatorActiveColor": "#000000",
        "indicatorColor": "rgba(0, 0, 0, .3)",
      }
    },
    "free_vessel2": {
      "style": "width:682rpx;box-shadow:rgba(153, 153, 153, 0.24) 0rpx 0rpx 7rpx;margin-bottom:auto;margin-left:auto;margin-right:auto;margin-top:18rpx;",
      "content": [{
        "style": "width:160rpx",
        "pic_style": "height:82rpx;width:82rpx;",
        "pic": "http:\/\/img.zhichiwangluo.com\/zcimgdir\/album\/file_5b287cfed6c25.png",
        "text": "蔬菜与水果",
        "text_style": "color:rgb(68, 68, 68);font-size:28rpx;",
        "itemIndex": 0,
      }]
    }
  },

  onLoad: function () {
    request.sendRequest({
      url: '/poster',
      data: {
        type: 'youershuo'
      },
      success: res => {
        const carousel = res.map((item) => {
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
  }
})