var app = getApp();
var request = require('../../../utils/request.js')

Page({
  data: {
    "title": '',
    "book_list": {
      "content": []
    }
  },

  onLoad: function (options) {
    var volume_id = options.id
    this.setData({
      'title': options.name
    })
    request.sendRequest({
      url: '/library/book',
      data: {
        volume: volume_id
      },
      success: res => {
        const results = res.results
        const books = results.map((item) => {
          const oneItem = {};
          oneItem.pic = item.picture;
          oneItem.name = item.name;
          oneItem.url = '/pages/subpage/bookPage/bookPage?from=book&id='+ item.id
          oneItem.description = item.description
          return oneItem
        });
        this.setData({
          'book_list.content': books
        })
      }
    })
  }
})