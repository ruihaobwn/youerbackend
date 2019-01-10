var request = require('../../../utils/request.js')
var recorderManager = wx.getRecorderManager()
var innerAudioContext = wx.createInnerAudioContext()

Page({
  data: {
    card_type_id: null,
    all_card_titles: [],
    turn_page: {
      style: "position:absolute;right:40rpx;top:40rpx",
      text: '翻页关'
    },

    pagination: {
      limit: 10,
      offset: 0
    },
    // 发音点击区域
    voice_area: {
      // 单词发音
      word_style: "position:absolute;height:540rpx;width:510rpx; left:120rpx;top:140rpx;",
      sentence_style: "position:absolute;height:130rpx;right:50rpx; left:50rpx;top:740rpx;"
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
        card_type_id: this.data.card_type_id,
        limit: this.data.pagination.limit,
        offset: this.data.pagination.offset
      },
      success: res => {
        var results = []
        for (var j = 0; j < res.results.length; ++j){

          var card = res.results[j]
          var card_audio = {}
          var audio_array = card.card_audio
          for (var i = 0; i < audio_array.length; ++i) {
            var key = audio_array[i].type
            card_audio[key] = audio_array[i].url
          }
          card.card_audio = card_audio
          results.push(card)
        }
        var card_list = this.data.card_data.results.concat(results)
        var card_data = {}
        card_data.results = card_list
        card_data.count = res.count
        console.log(card_data)
        this.setData({
          card_data: card_data
        })
        if(this.load){
          const card_audio = this.data.card_data.results[0].card_audio
          this.playWord(card_audio.Word)
          this.load=false
        }
      }
    }) 
  },

  onLoad: function (options) {
    const card_type_id = options.id
    this.setData({card_type_id: card_type_id})
    this.load = true
    request.sendRequest({
      url: '/card/card',
      data: {
        title: true,
        card_type: card_type_id
      },
      success: res => {
        const results = res.results
        const count = res.count
        this.setData({
          all_card_titles: results
        })
        this.getCard()
      }
    })
    innerAudioContext.onPlay(() => {
      console.log('开始播放')
    })
    innerAudioContext.onError((res) => {
      console.log(res.errMsg)
      console.log(res.errCode)
    })
    innerAudioContext.onEnded(() => {
      if(this.data.swiper_props.autoplay && this.data.swiper_props.current<this.data.card_data.count-1){
        this.data.swiper_props.current++
        this.setData({
          swiper_props: this.data.swiper_props
        })
      }
    })
  },

  changeCurrent: function(e){
    const current = e.detail.current
    // auto play word when change card
    const url = this.data.card_data.results[current].card_audio.Word
    this.playWord(url)
    
    const length = this.data.card_data.results.length
    const all_card_count = this.data.card_data.count
    const limit = this.data.pagination.limit
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
      this.data.swiper_props.autoplay = false
    }else{
      this.data.turn_page.text = '翻页关'
      this.data.swiper_props.autoplay = true
    }
    this.setData({
      turn_page: this.data.turn_page,
      swiper_props: this.data.swiper_props
    })
    if (this.data.swiper_props.autoplay && this.data.swiper_props.current < this.data.card_data.count - 1) {
      this.data.swiper_props.current++
      this.setData({
        swiper_props: this.data.swiper_props
      })
    }
  },
  play_word: function(e){
    console.log(e.currentTarget)
    var dataset = e.currentTarget.dataset
    this.playWord(dataset.url)
  },

  playWord: function(url){
    if (!!url) {
      innerAudioContext.src = url
      innerAudioContext.play()
    }
  },
  play_sentence: function(e){
    var dataset = e.currentTarget.dataset
    if(!!dataset.url){
      innerAudioContext.src = dataset.url
      innerAudioContext.play()
    }
  },
  startRecord: function (e) {
    const action = e.currentTarget.dataset.action
    if (action == '录音') {
      this.setData({ record_text: '停止' })
      recorderManager.start()
    }
    else if (action == '停止') {
      this.setData({ record_text: '录音' })
      recorderManager.stop()
      recorderManager.onStop((res) => {
        this.tempFilePath = res.tempFilePath
      })
    }
  },
  playRecord: function(e){
    innerAudioContext.src = this.tempFilePath
    console.log(this.tempFilePath)
    // innerAudioContext.autoplay = true
    innerAudioContext.play()
  },
  openVideo: function(e){
    const index = this.data.swiper_props.current
    const videosrc = this.data.card_data.results[index].video
    const url = '/pages/video/video?videosrc=' + videosrc
    wx.navigateTo({ url: url })
  }
})