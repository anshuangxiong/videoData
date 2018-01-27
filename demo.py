# coding=utf-8

import urllib.request as req
from bs4 import BeautifulSoup
import cx_Oracle
from selenium import webdriver
from lxml import etree

#driver = webdriver.Firefox()  #调用chrome浏览器

#driver.get('http://www.tudou.com/sec/%E9%9F%B3%E4%B9%90?spm=a2h28.8313475.nav.dn_sec3')

#print(driver.title)

# 执行js得到整个dom
#html = driver.execute_script('''
    #alert('123')

#''')
#doc = etree.HTML(html)
#print(doc)
# 用xslt从dom中提取需要的字段

db = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/orcl')
# print(db)


headers = {# 'Accept': 'application/json, text/javascript, */*; q=0.01',
           # 'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Cache-Control': 'max-age=0',
           'Host': 'www.tudou.com',
           'Cookie': 'HasLoaded=true; cna=/pqOEgmV73ICAcpxTsA9G6JC; _zpdtk=b5bb91787cae14516baf5668659efd19845e2f79; __ysuid=1510452478660Ci5; isg=AsnJJalo9z0a1ItIlmXigrka2PWVvrzCDNQNYGs-XbDusunEsmbNGLfsgCD_',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
           'Connection': 'keep-alive',
           'X-CSRF-TOKEN': 'b5bb91787cae14516baf5668659efd19845e2f79',
           'Referer': 'http://www.tudou.com/sec/%E9%9F%B3%E4%B9%90?spm=a2h28.8313475.nav.dn_sec3',
           # 'X-Requested-With': 'XMLHttpRequest'
           }

for t in range(1, 10):
    request = req.Request(url="http://www.tudou.com/sec/%E9%9F%B3%E4%B9%90?spm=a2h28.8313475.nav.dn_sec3")
    response = req.urlopen(request)
    # print(response.read())
    print("********************************")
    soup = BeautifulSoup(response, 'html.parser')
    # print(soup.prettify())
    v_pack = soup.find_all(name='div', attrs={'class': 'v-pack'})
    i = 0
    for tag in v_pack:
        i = i + 1
        v_thumb = tag.find_all(name='div', attrs={'class': 'v-thumb'})
        v_meta = tag.find_all(name='div', attrs={'class': 'v-meta'})
        image = v_thumb[0].img
        a = v_meta[0].a
        # print(i)
        # print(image['src'])
        # print(image['src'].index('?'))
        # print(image['src'][0:image['src'].index('?')])
        # print(image['alt'])
        # print(a['href'])
        # print(a['href'][0:a['href'].index('?')])
        names = image['alt']
        url = image['src'][0:image['src'].index('?')]
        href = a['href'][0:a['href'].index('?')]
        types = "音乐"
        cr = db.cursor()
        sql = "INSERT INTO video_data(NAME,TYPE,VIDEO_URL,IMG_URL) VALUES ('" + names + "', '" + types + "', '" + url + "', '" + href + "')"
        cr.execute(sql)
        cr.close()
        db.commit()




