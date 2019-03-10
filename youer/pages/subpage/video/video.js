// pages/video/video.js
Page({
  data: {
    src: '',
    res: {}
  },

  onLoad: function (options) {
    this.setData({
      src: options.videosrc
    })
    
    wx.startDeviceMotionListening()
    var that = this
    var video_context = wx.createVideoContext("video_player")

    wx.onDeviceMotionChange(
      res => {
        var direction = 0
        if (res.gamma > 45){
          direction = 90
        }else if(res.gamma < -45){
          direction = -90
        }
        if (direction===0){
          video_context.exitFullScreen()
        }else{
          video_context.requestFullScreen({ direction: direction })
        }
      }
    )
  },

  onReady: function () {
  },

  videoErrorCallback: function (e) {
    console.log('视频错误信息:')
    console.log(e.detail.errMsg)
  }
})