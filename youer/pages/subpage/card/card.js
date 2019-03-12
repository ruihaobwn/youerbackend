var request = require('../../../utils/request.js')

Page({
  data: {
    card_type_id: null,
    all_card_titles: [],
    turn_page: {
      style: "position:absolute;right:40rpx;top:40rpx;width:60rpx;height:60rpx",
      text: '翻页关',
      src: '/images/pageopen.png'
    },
    
    page_number: {
      style: "position:absolute;top:0rpx;left:30rpx",
      current: 1
    },

    pagination: {
      limit: 10,
      offset: 0
    },
    // 发音点击区域
    voice_area: {
      // 单词发音
      word_style: "position:absolute;height:50vh;width:70vw;left:15vw;top:10vh",
      sentence_style: "position:absolute;height:10vh;width:90vw;left:5vw;top:63vh"
    },
    card_style: "height:80vh;width:100wh",
    swiper_props: {
      current: 0,
      autoplay: true
    },
    card_data: {
      count: 0,
      results: []
    },
    record_text: '录音'
  },

  getCard: function(){
    request.sendRequest({
      url: '/card/card',
      data: {
        card_type: this.data.card_type_id,
        limit: this.data.pagination.limit,
        offset: this.data.pagination.offset
      },
      success: res => {
        var card_list = this.data.card_data.results.concat(res.results)
        var card_data = {}
        card_data.results = card_list
        card_data.count = res.count
        this.setData({
          card_data: card_data
        })
        if(this.load){
          var word_voice = this.data.card_data.results[0].word_voice
          this.playWord(word_voice)
          this.load=false
        }
      }
    }) 
  },

  onLoad: function (options) {
    var card_type_id = options.id
    this.recorderManager = wx.getRecorderManager()
    this.innerAudioContext = wx.createInnerAudioContext()
    this.setData({card_type_id: card_type_id})
    this.load = true
    request.sendRequest({
      url: '/card/card',
      data: {
        title: true,
        card_type: card_type_id
      },
      success: res => {
        var results = res.results
        var count = res.count
        this.setData({
          
        })
        this.setData({
          all_card_titles: results
        })
        this.getCard()
      }
    })
    this.innerAudioContext.onError((res) => {
      console.log(res.errMsg)
      console.log(res.errCode)
    })
    this.innerAudioContext.onPlay((res) => {
      console.log('start play')
    })
    this.innerAudioContext.onEnded(() => {
      if(this.data.swiper_props.autoplay && this.data.swiper_props.current<this.data.card_data.count-1){
        this.data.swiper_props.current++
        this.setData({
          swiper_props: this.data.swiper_props,
        })
      }
    })
  },

  changeCurrent: function(e){
    var current = e.detail.current
    this.data.swiper_props.current = current
    this.setData({
      'page_number.current': current+1
    })
    // auto play word when change card
    var url = this.data.card_data.results[current].word_voice
    this.playWord(url)
    
    var length = this.data.card_data.results.length
    var all_card_count = this.data.card_data.count
    var limit = this.data.pagination.limit
    // when remain two card, get new card
    if (length<all_card_count && current<length-3){
      this.data.pagination.offset = current*limit
      this.getCard()
    }
  },
  changeTurnPage: function(e){
    var dataset = e.currentTarget.dataset
    var text = dataset.text
    if (text==='翻页关'){
      this.data.turn_page.text = '翻页开'
      this.data.turn_page.src = '/images/pageclose.png'
      this.data.swiper_props.autoplay = false
    }else{
      this.data.turn_page.text = '翻页关'
      this.data.turn_page.src = '/images/pageopen.png'
      this.data.swiper_props.autoplay = true
    }
    this.setData({
      turn_page: this.data.turn_page,
      swiper_props: this.data.swiper_props
    })
    if (this.data.swiper_props.autoplay && this.data.swiper_props.current < this.data.card_data.count - 1) {
      this.data.swiper_props.current++
      this.setData({
        swiper_props: this.data.swiper_props,
      })
    }
  },
  play_word: function(e){
    var dataset = e.currentTarget.dataset
    this.playWord(dataset.url)
  },

  playWord: function(url){
    if (!!url) {
      this.innerAudioContext.src = url
      this.innerAudioContext.play()
    }
  },
  play_sentence: function(e){
    var dataset = e.currentTarget.dataset
    if(!!dataset.url){
      this.innerAudioContext.src = dataset.url
      this.innerAudioContext.play()
    }
  },
  startRecord: function (e) {
    var action = e.currentTarget.dataset.action
    if (action == '录音') {
      this.setData({ record_text: '停止' })
      this.recorderManager.start()
    }
    else if (action == '停止') {
      this.setData({ record_text: '录音' })
      this.recorderManager.stop()
      this.recorderManager.onStop((res) => {
        this.tempFilePath = res.tempFilePath
      })
    }
  },
  playRecord: function(e){
    if(!!this.tempFilePath){
      this.innerAudioContext.src = this.tempFilePath
      this.innerAudioContext.play()
    }
  },
  openVideo: function(e){
    var index = this.data.swiper_props.current
    var videosrc = this.data.card_data.results[index].video
    var url = '/pages/subpage/video/video?videosrc=' + videosrc
    wx.navigateTo({ url: url })
  },
  onUnload: function (e) {
    this.innerAudioContext.destroy()
  }
})