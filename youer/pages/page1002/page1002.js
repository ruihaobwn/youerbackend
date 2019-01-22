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
        "indicatorColor": "rgba(0, 0, 0, .3)",
      }
    },
    "bookType": {
      "style": "width:682rpx; margin-left:auto;margin-right:auto;margin-top:18rpx;",
      "content": []
    },
    "scroll_data": {
      "style": "width:750rpx",
      "item_style": "margin-left:50rpx;width:300rpx;height:300rpx",
      "image_style": "height:300rpx;width:300rpx;",
      "text_style": "color:rgb(68, 68, 68);font-size:28rpx;",
      "content": []
    }
  },

  onLoad: function () {
    request.sendRequest({
      url: '/poster',
      data: {
        type: 'Library'
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
      url: '/library/book_type',
      data: {
        limit: 8
      },
      success: res => {
        const results = res.results
        const types = results.map(item => {
          const oneItem = {
            "style": "width:160rpx",
            "pic_style": "height:82rpx;width:82rpx;",
            "text_style": "color:rgb(68, 68, 68);font-size:28rpx;"
          }
          oneItem.pic = item.image_file
          oneItem.text = item.title
          oneItem.itemIndex = item.id
          return oneItem
        })
        this.setData({
          'bookType.content': types
        })
      }
    })
  },
  getBooks: function(e){
    var data = e.currentTarget.dataset
    var type_id = data.typeid
    request.sendRequest({
      url: '/library/volume',
      data: {
        book_type: type_id
      },
      success: res => {
        const results = res.results
        const types = results.map(item => {
          const oneItem = {}
          oneItem.image = item.picture
          oneItem.text = item.name
          oneItem.itemIndex = item.id
          oneItem.has_subbook = item.has_subbook
          return oneItem
        })
        this.setData({
          'scroll_data.content': types
        })
      }
    })
  },
  openBook: function(e){
    var data = e.currentTarget.dataset
    var book_id = data.bookid
    var has_subbook = data.subbook
    var name = data.name
    if(!has_subbook){
      wx.navigateTo({
        url: '/pages/subpage/bookPage/bookPage?from=volume&id='+book_id
      })
    }
    else{
      wx.navigateTo({
        url: '/pages/subpage/subBook/subBook?id=' + book_id + '&name=' + name
      })
    }
  }
})