import requests
import shutil

ACCESS_TOKEN = "27_Xq7GhPy7fhiErOvHQ44tG1V5g_Q3R1DR-nVxEZ6b1Pr6gLr6dvCGukVxEoExUImBRSrqKkH7k8mA2QiHt1YHS87DLEXg6aN743jUHIB17mk3s-Qi0pgG9g1bXhxOMTm7rwBCl1oEugWMkoNfBJNdAEAWEI"
url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token={}".format(ACCESS_TOKEN)
for i in range(1, 2):
    page = "pages/subpage/bookPage/bookPage"
    data= {
        "page": page,
        "scene": "book_id=21",
        "auto_color": True
    }
    response = requests.post(url, json=data)
    print(response.status_code)
    with open("{}.png".format(i), 'wb') as f:
        f.write(response.content)

