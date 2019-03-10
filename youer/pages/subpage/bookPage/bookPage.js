var request = require('../../../utils/request.js')

Page({
  data: {
    book_id: null,
    from_type: 'volume',
    turn_page: {
      style: "position:absolute;right:40rpx;top:40rpx;width:60rpx",
      text: '翻页关',
      src: '/images/pageopen.png'
    },
    record_disable: true,
    pagination: {
      limit: 10,
      offset: 0
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
    record_text: '录音',
    record_disable: true
  },

  getCard: function () {
    var data = {
      limit: this.data.pagination.limit,
      offset: this.data.pagination.offset
    }
    if (this.data.from_type === 'volume'){
      data.volume = this.data.book_id
    }
    else{
      data.book = this.data.book_id
    }
    request.sendRequest({
      url: '/library/bookpage',
      data: data,
      success: res => {
        var results = []
        for (var j = 0; j < res.results.length; ++j) {
          var card = res.results[j]
          results.push(card)
        }
        var card_list = this.data.card_data.results.concat(results)
        var card_data = {}
        card_data.results = card_list
        card_data.count = res.count
        this.setData({
          card_data: card_data
        })
        if (this.load) {
          var card = this.data.card_data.results[0]
          if (card.audio_url){
            this.playWord(card.audio_url)
          } else{
            setTimeout(this.play_next, 2000)
          }
          this.load = false
        }
      }
    })
  },

  onLoad: function (options) {
    this.recorderManager = wx.getRecorderManager()
    this.innerAudioContext = wx.createInnerAudioContext()
    var book_id = options.id
    var from_type = options.from
    this.setData({ book_id: book_id, from_type: from_type })
    // 判断是否为第一次加载，第一次加载自动播放
    this.load = true
    this.getCard()
      
    this.innerAudioContext.onError((res) => {
      console.log(res.errMsg)
      console.log(res.errCode)
    })
    this.innerAudioContext.onEnded(() => {
      if (this.data.swiper_props.autoplay && this.data.swiper_props.current < this.data.card_data.count - 1) {
        this.data.swiper_props.current++
        this.setData({
          swiper_props: this.data.swiper_props
        })
      }
    })
  },

  changeCurrent: function (e) {
    var current = e.detail.current
    this.data.swiper_props.current = current
    // auto play word when change card
    var url = this.data.card_data.results[current].audio_url
    this.playWord(url)

    var length = this.data.card_data.results.length
    var all_card_count = this.data.card_data.count
    var limit = this.data.pagination.limit
    // when remain two card, get new card
    if (length < all_card_count && current < length - 3) {
      this.data.pagination.offset = current * limit
      this.getCard()
    }
  },
  changeTurnPage: function (e) {
    var dataset = e.currentTarget.dataset
    var text = dataset.text
    if (text === '翻页关') {
      this.data.turn_page.text = '翻页开'
      this.data.record_disable = false
      this.data.swiper_props.autoplay = false
    } else {
      this.data.record_disable = true
      this.data.turn_page.text = '翻页关'
      this.data.swiper_props.autoplay = true
    }
    this.setData({
      turn_page: this.data.turn_page,
      swiper_props: this.data.swiper_props,
      record_disable: this.data.record_disable
    })
    if (this.data.swiper_props.autoplay && this.data.swiper_props.current < this.data.card_data.count - 1) {
      this.data.swiper_props.current++
      this.setData({
        swiper_props: this.data.swiper_props
      })
    }
  },
  play_word: function (e) {
    var dataset = e.currentTarget.dataset
    this.playWord(dataset.url)
  },

  playWord: function (url) {
    if (!!url) {
      this.innerAudioContext.src = url
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
  playRecord: function (e) {
    if (!!this.tempFilePath) {
      this.innerAudioContext.src = this.tempFilePath
      this.innerAudioContext.play()
    }
  },
  onUnload: function (e) {
    this.innerAudioContext.destroy()
  },
  
  play_next: function(e) {
    if (this.data.swiper_props.autoplay && this.data.swiper_props.current < this.data.card_data.count - 1) {
      this.data.swiper_props.current++
      this.setData({
        swiper_props: this.data.swiper_props
      })
    }
  }
})