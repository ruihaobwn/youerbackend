// pages/super/singlepage/singlepage.js
const recorderManager = wx.getRecorderManager()
Page({
  data: {
    imageList: [
      { src: '../../../images/maize.jpg', key: 'maize', audio: '/audio/maize.mp3', video: 'http://www.youershuo.net/uploadfile/file/video/ceshi1/177.maize_onekeybatch.mp4'},
      { src: '../../../images/carrot.jpg', key: 'carrot', audio: '/audio/carrot.mp3', video: 'http://www.youershuo.net/uploadfile/file/video/ceshi1/177.maize_onekeybatch.mp4'}
    ],
    record_text: '录音',
    
  },
  onSlideChange: function(e){
    this.current = e.detail.current
  },
  play: function(e){
    this.innerAudioContext.src = e.currentTarget.dataset.audio
    console.log(this.innerAudioContext.src)
    this.innerAudioContext.play()
  },
  onLoad: function(e){
    console.log('onload called')
    this.index = 0
    this.innerAudioContext = wx.createInnerAudioContext()
    this.innerAudioContext.onPlay(()=>{
      console.log('开始播放')
    })
    this.innerAudioContext.onError((res)=>{
      console.log(res.errMsg)
      console.log(res.errCode)
    })
  },
  openVideo: function(e){
    const index = this.current
    const videosrc = this.data.imageList[0].video
    const url = '/pages/video/video?videosrc=' + videosrc
    wx.navigateTo({ url: url})
  },
  startRecord: function(e){
    const action = e.currentTarget.dataset.action
    if (action == '录音'){
      this.setData({ record_text: '停止' })
      recorderManager.start()
    }
    else if(action == '停止'){
      this.setData({ record_text: '播放' })
      recorderManager.stop()
      recorderManager.onStop((res) => {
        this.tempFilePath = res.tempFilePath
      })
    }
    else if(action == '播放'){
      this.setData({ record_text: '录音' })
      this.innerAudioContext.src = this.tempFilePath
      this.innerAudioContext.play()
    }

  }
})
