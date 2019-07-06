import time
import hashlib
import requests
import json

CLOUDKEY = 'f2d6b833ac487ae0a839556af48b2145'
CLOUDSECRET = 'HxsiuQ4CEfsiTL3IleoA2rNw69C3X3xEM8Me9PvTYP8NDqAEhqyLE7X0JU6SuIYtgzR6t70mXwQL1Ed9du5wB3lvIq9y4hBm6xxkWr5mWBy3wk4EkJSLxjCoaWccLzLt'
CLOUDSERVERURL = 'http://6f8c562281cf9307f60e6ca7cb5de830.cn1.crs.easyar.com:8888'
CLOUDCLIENTURL = 'http://6f8c562281cf9307f60e6ca7cb5de830.cn1.crs.easyar.com:8080'


def _signature(params):
    params['timestamp'] = int(time.time() * 1000)
    params['appKey'] = CLOUDKEY
    params = {k: params[k] for k in sorted(params.keys())}
    tmp = []
    for key, value in params.items():
        tmp.append('{}{}'.format(key, value))
    string = ''.join(tmp)
    m = hashlib.sha256()
    m.update(string.encode('utf-8'))
    m.update(CLOUDSECRET.encode('utf-8'))
    params['signature'] = m.hexdigest()
    return params


class CRS:
    TARGET = '/targets'
    TARGET_TARGETID = '/target/%(id)s'

    def __init__(self):
        pass

    def create_target(self, params):
        params = _signature(params)
        url = CLOUDSERVERURL + self.TARGET
        try:
            res = requests.post(url, headers={'Content-Type': 'application/json', 'charset': 'utf-8'},
                                data=json.dumps(params))
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as e:
            print(e)

    def delete_target(self, target_id):
        params = _signature({})
        url = CLOUDSERVERURL + self.TARGET_TARGETID
        url = url % {"id": target_id}
        try:
            res = requests.delete(url, params=params)
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as e:
            print(e)
