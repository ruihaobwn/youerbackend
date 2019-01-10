var app = getApp();

function showLoading(param) {
  wx.showLoading({
    title: param.title,
    success: function (res) {
      typeof param.success == 'function' && param.success(res);
    },
    fail: function (res) {
      typeof param.fail == 'function' && param.fail(res);
    },
    complete: function (res) {
      typeof param.complete == 'function' && param.complete(res);
    }
  })
}
function hideLoading() {
  wx.hideLoading();
}

function sendRequest (param, customSiteUrl) {
  let that = this;
  let data = param.data || {};
  let header = param.header;
  let requestUrl;

  if (customSiteUrl) {
    requestUrl = customSiteUrl + param.url;
  } else {
    requestUrl = app.globalData.siteBaseUrl + param.url;
  }

  if (param.method) {
    if (param.method.toLowerCase() == 'post') {
      data = _modifyPostParam(data);
      header = header || {
        'content-type': 'application/x-www-form-urlencoded;'
      }
    }
    param.method = param.method.toUpperCase();
  }

  if (!param.hideLoading) {
    showLoading({
      title: '请求中...'
    });
  }
  wx.request({
    url: requestUrl,
    data: data,
    method: param.method || 'GET',
    header: header || {
      'content-type': 'application/json'
    },
    success: function (res) {
      if (res.statusCode && res.statusCode != 200) {
        that.hideToast();
        that.showToast({
          title: '' + res.errMsg,
          icon: 'none'
        });
        typeof param.successStatusAbnormal == 'function' && param.successStatusAbnormal(res.data);
        return;
      }
      if (res.data.status) {
        if (res.data.status == 2 || res.data.status == 401) {
          that.goLogin({
            success: function () {
              that.sendRequest(param, customSiteUrl);
            },
            fail: function () {
              typeof param.successStatusAbnormal == 'function' && param.successStatusAbnormal(res.data);
            }
          });
          return;
        }
        if (res.data.status == 5) {
          typeof param.successStatus5 == 'function' && param.successStatus5(res.data);
          return;
        }
        if (res.data.status != 0) {
          if (typeof param.successStatusAbnormal == 'function' && (param.successStatusAbnormal(res.data) === false)) {
            return;
          }
          that.hideToast();
          that.showModal({
            content: '' + res.data.data,
            confirm: function () {
              typeof param.successShowModalConfirm == 'function' && param.successShowModalConfirm(res.data);
            }
          });
          return;
        }
      }
      typeof param.success == 'function' && param.success(res.data);
    },
    fail: function (res) {
      console.log('request fail:', requestUrl, res.errMsg);
      that.addLog('request fail:', requestUrl, res.errMsg);
      that.hideToast();
      if (res.errMsg == 'request:fail url not in domain list') {
        that.showToast({
          title: '请配置正确的请求域名',
          icon: 'none',
          duration: 2000
        });
      }
      typeof param.fail == 'function' && param.fail(res.data);
    },
    complete: function (res) {
      param.hideLoading || hideLoading();
      typeof param.complete == 'function' && param.complete(res.data);
    }
  });
}

function _modifyPostParam(obj) {
  let query = '';
  let name, value, fullSubName, subName, subValue, innerObj, i;

  for (name in obj) {
    value = obj[name];

    if (value instanceof Array) {
      for (i = 0; i < value.length; ++i) {
        subValue = value[i];
        fullSubName = name + '[' + i + ']';
        innerObj = {};
        innerObj[fullSubName] = subValue;
        query += _modifyPostParam(innerObj) + '&';
      }
    } else if (value instanceof Object) {
      for (subName in value) {
        subValue = value[subName];
        fullSubName = name + '[' + subName + ']';
        innerObj = {};
        innerObj[fullSubName] = subValue;
        query += _modifyPostParam(innerObj) + '&';
      }
    } else if (value !== undefined && value !== null) {
      query += encodeURIComponent(name) + '=' + encodeURIComponent(value) + '&';
    }
  }

  return query.length ? query.substr(0, query.length - 1) : query;
}

function showToast(param) {
  wx.showToast({
    title: param.title,
    icon: param.icon,
    duration: param.duration || 1500,
    success: function (res) {
      typeof param.success == 'function' && param.success(res);
    },
    fail: function (res) {
      typeof param.fail == 'function' && param.fail(res);
    },
    complete: function (res) {
      typeof param.complete == 'function' && param.complete(res);
    }
  })
}

function hideToast() {
  wx.hideToast();
}



module.exports = {
  sendRequest: sendRequest
}
