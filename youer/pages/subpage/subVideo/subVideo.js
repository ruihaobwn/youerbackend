var app = getApp();
var request = require('../../../utils/request.js')

Page({
  data: {
    "title": '',
    "video_list": {
      "content": []
    }
  },

  onLoad: function (options) {
    var video_id = options.id
    this.setData({
      'title': options.name
    })
    request.sendRequest({
      url: '/video/subvideo',
      data: {
        video: video_id
      },
      success: res => {
        const results = res.results
        const videos = results.map((item) => {
          const oneItem = {};
          oneItem.pic = item.image_url;
          oneItem.name = item.title;
          oneItem.url = '/pages/subpage/video/video?videosrc='+item.video_url
          oneItem.description = item.description
          return oneItem
        });
        this.setData({
          'video_list.content': videos
        })
      }
    })
  }
})