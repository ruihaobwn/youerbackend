// pages/video/video.js
Page({
  data: {
    src: '',
  },

  onLoad: function (options) {
    this.setData({
      src: options.videosrc
    })
  },

  onReady: function () {
  },

  videoErrorCallback: function (e) {
    console.log('视频错误信息:')
    console.log(e.detail.errMsg)
  }
})