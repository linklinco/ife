import json
import requests
from bs4 import BeautifulSoup
import html2text as ht
def get_html(i,url,name):
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
    save_html_to_md(i,html,name)
def save_html_to_md(i,html,file_name):
    text_maker = ht.HTML2Text()
    soup = BeautifulSoup(html,"lxml")
    res = soup.find_all(class_ = 'md-content-wrap')
    text = text_maker.handle(str(res[0]))
    with open('No.'+str(i)+file_name +'.md','w',encoding = 'utf8') as f:
        f.write(text)
if __name__ == "__main__":
    with open("data.json",'r',encoding='utf8') as f:
        data = json.load(f)
    j = 1
    for i in data:
        get_html(j,i['url'],i['title'])
        j += 1
