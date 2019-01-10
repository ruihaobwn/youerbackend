var request = require('../../../utils/request.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    style: "width:100%;height:100%;background-color:rgb(255, 255, 255);",
    itemStyle: {
      "style": "width:160rpx",
      "pic_style": "height:82rpx;width:82rpx;",
      "text_style": "color:rgb(68, 68, 68);font-size:28rpx;"
    },
    cardTypeList: {
      count: 0,
      results: [{
        title:'',
        image_file: ''
        }]
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    const product_id = options.id
    request.sendRequest({
      url: '/card/card_type',
      data: {
        product: product_id
      },
      success: res => {
        console.log(res)
        this.setData({
          cardTypeList: res
        })
      }
    })
  },
  openCard: function (e){
    console.log(e)
    const cardType_id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: '/pages/subpage/card/card?id=' + cardType_id
    })
  }
})