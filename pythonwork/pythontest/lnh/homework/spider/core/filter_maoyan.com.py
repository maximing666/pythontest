#  解析html内容，过滤内容
import re

with open('db/maoyan', mode='r', encoding='utf-8') as f:
    s = f.read()
res = re.findall(r'<dd.*?<i .*?>(.+?)</i>.*?<p.*?title="(.+?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?</dd>', s, re.S)
# print(res)
# print()
for i in res:
    for j in i:
        print(j.strip())


# 正则表达式：
#序号： <i .*?>([\d]+)</i>
#电影名称： <p.*?(title=".+?")
#主演： <p class="star">(.*?)</p>
#上映时间： <p class="releasetime">(.* ?)</p>
#汇总：  r'<dd.*?<i .*?>([\d]+)</i>.*?<p.*?(title=".+?").*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.* ?)</p>.*?</dd>'

