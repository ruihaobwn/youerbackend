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
    "videoType": {
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
        type: 'Video'
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
      url: '/video/video_type',
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
          'videoType.content': types
        })
      }
    })
    this.getVideoByType(0)
  },

  getVideoByType: function(type_id){
    var params = {}
    if (type_id > 0){
      params.video_type = type_id
    }
    request.sendRequest({
      url: '/video/video',
      data: params,
      success: res => {
        const results = res.results
        const types = results.map(item => {
          const oneItem = {}
          oneItem.image = item.image_file
          oneItem.text = item.title
          oneItem.itemIndex = item.id
          oneItem.videoUrl = item.video_url
          oneItem.has_subvideo = item.has_subvideo
          return oneItem
        })
        this.setData({
          'scroll_data.content': types
        })
      }
    })
  },

  getVideos: function (e) {
    var data = e.currentTarget.dataset
    var type_id = data.typeid
    this.getVideoByType(type_id)
  },

  openVideo: function (e) {
    var data = e.currentTarget.dataset
    var video_url = data.videourl
    var video_id = data.videoid
    var has_subvideo = data.subvideo
    var name = data.name
    if (!has_subvideo) {
      wx.navigateTo({
        url: '/pages/subpage/video/video?videosrc='+video_url
      })
    }
    else {
      wx.navigateTo({
        url: '/pages/subpage/subVideo/subVideo?id=' + video_id + '&name=' + name
      })
    }
  }
})