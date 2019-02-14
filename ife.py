# coding = utf8
import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

def save_to_json(data,file_name):
    res  = json.dumps(data,ensure_ascii = False)
    with open(file_name,'w+',encoding='utf8') as f:
        f.write(res)
url = "http://ife.baidu.com/college/detail/id/5"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "DNT": "1",
    'If-Modified-Since': 'Mon, 26 Feb 2018 16:20:21 GMT',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

}
r = requests.get(url, headers=headers,timeout = 10)
r.encoding = "utf-8"
html = r.text
soup = BeautifulSoup(html,"lxml")
res = soup.find_all(class_ = 'cal-list-title')
info = []
for i in range(0,len(res)):
    j = {}
    asd = str(res[i])
    j['url'] = "http://ife.baidu.com"+asd[33:53]
    j['title'] = asd[71:-4]
    info.append(j)
save_to_json(info,'data.json')