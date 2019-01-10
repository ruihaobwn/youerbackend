Page({
  data: {
    autoplay: true,
    sliderList: [
      {id: 'shichi', className: 'bg-red', name: '古诗词', page: '../super/shichi'},
      {id: 'phonics', className: 'bg-blue', name: 'PHONICS', page: '../super/phonics'},
      {id: 'english', className: 'bg-green', name: 'English', page: '../super/english/english'},
      {id: 'pinyin', className: 'bg-orange', name: '拼音', page: '../super/pinyin'}
    ]
  },
  play: function(){
    this.setData({
      autoplay: !this.data.autoplay
    });
  }
})
