// pages/super/english/english.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    typeList: [{
      key: 'color',
      title: '时间数字颜色',
      src: '../../../images/20171104101252_75632.png' 
    },{
      key: 'vegetable',
      title: '蔬果',
      src: '../../../images/20171116231617_95715.png'
    },{
      key: 'transport',
      title: '交通与地点',
      src: '../../../images/20171116231810_32173.png'
    },{
      key: 'animal',
      title: '动物',
      src: '../../../images/20171116231832_74374.png'
    },{
      key: 'food',
      title: '食物',
      src: '../../../images/20171116231847_88527.png'
    },{
      key: 'clothes',
      title: '身体与服装',
      src: '../../../images/20171116231912_21063.png'
    }]
  },
  getOneImg: function () {
    wx.redirectTo({
      url: '../singlepage/singlepage',
    })
  }
  
})