#  解析html内容，过滤内容
import re

with open('../db/93223591074bb591677374dae559f42f', mode='r', encoding='utf-8') as f:
    s = f.read()
    s = s.replace('\"', '\'')

num1 = s.find('所属地区')
num2 = s.find('ICB行业市值排名')
s1 = s[num1:num2+100]
print(s1)
# res = re.findall(r"(.*?)</td>.*?target='_blank'>(.*?)</a>.*?class='tb2_new'>(.*?)</td>.*?'tb2_new'>(.*?)</td>.*?class='tb1_new'>(.*?)</td><td.*?</td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb1_new'>(.*?)</td>.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb1_new'>(.*?)</td>.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td rowspan='2' class='tb5_new'>(.*?)<br.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb4_new'>(.*?)</td><td class='tb4_new'>(.*?)</td>.*?class='tb7_new'>(.*?)</td>.*?target='_blank'>(.*?)</a>.*?class='tb5_new'>(.*?)</td>.*?target='_blank''>(.*?)</a>.*", s1, re.S)
res = re.findall(r"(.*?)</td>.*?target='_blank'>(.*?)</a>.*?class='tb2_new'>(.*?)</td>.*?'tb2_new'>(.*?)</td>.*?class='tb1_new'>(.*?)</td><td.*?</td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb1_new'>(.*?)</td>.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb1_new'>(.*?)</td>.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td rowspan='2' class='tb5_new'>(.*?)<br.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb4_new'>(.*?)</td><td class='tb4_new'>(.*?)</td>.*?class='tb7_new'>(.*?)</td>.*?target='_blank'>(.*?)</a>.*?class='tb5_new'>(.*?)</td>.*?target='_blank'>(.*?)</a>.*", s1, re.S)
print(res)
print()
for i in res:
    for j in i:
        print(j.strip())


# 正则表达式：
#序号： <i .*?>([\d]+)</i>
#电影名称： <p.*?(title=".+?")
#主演： <p class="star">(.*?)</p>
#上映时间： <p class="releasetime">(.* ?)</p>
#汇总：  r'<dd.*?<i .*?>([\d]+)</i>.*?<p.*?(title=".+?").*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.* ?)</p>.*?</dd>'

