import time
import hashlib
import requests
import json

CLOUDKEY = 'f25473e4761a423b380d16f2bd14ae9c'
CLOUDSECRET = 'fJ1Op3QnzVB63t8e5PvQR5QnN5hqIOLVHUqEuGOCNxzs8hfi95L0VjczPRXn01T736VWzErbShRQRjiJEe7kG9uDNzrQLUxFNr3tEMOUzzviJjgcO4u8piENTxWN8y7p'
CLOUDSERVERURL = 'http://b2a422864857b34713b22df239e35f1a.cn1.crs.easyar.com:8888'
CLOUDCLIENTURL = 'http://b2a422864857b34713b22df239e35f1a.cn1.crs.easyar.com:8080'


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
