import urllib.request
import random
import re


def my_spider():
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]

    # url = "https://maoyan.com/board"
    url = "https://xueqiu.com/snowman/S/SH600316/detail#/ZYCWZB"

    randdom_header = random.choice(my_headers)

    req = urllib.request.Request(url)

    req.add_header("User-Agent", randdom_header)
    req.add_header("GET", url)

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)

    rec = re.compile(r'http.*?//(.*?)/.*')
    dbfile = rec.findall(url)
    print(dbfile)
    with open('../db/' + dbfile[0], mode='w', encoding='utf-8') as f:
        f.write(html)

