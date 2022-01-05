#  解析html内容，过滤内容
# 市净率的计算方法是：市净率=（P/BV）即：每股市价(P)/每股净资产(Book Value)
import re


class filter_hexun_summary:
    def __init__(self, spider_file):
        self.spider_file = spider_file

    def run(self):
        with open('../db/' + self.spider_file, mode='r', encoding='utf-8') as f:
            s = f.read()
            s = s.replace('\"', '\'')

        num1 = s.find('所属地区')
        num2 = s.find('ICB行业市值排名')
        s1 = s[num1:num2+100]
        print(s1)
        # res = re.findall(r"(.*?)</td>.*?target='_blank'>(.*?)</a>.*?class='tb2_new'>(.*?)</td>.*?'tb2_new'>(.*?)</td>.*?class='tb1_new'>(.*?)</td><td.*?</td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb1_new'>(.*?)</td>.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb1_new'>(.*?)</td>.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td rowspan='2' class='tb5_new'>(.*?)<br.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb4_new'>(.*?)</td><td class='tb4_new'>(.*?)</td>.*?class='tb7_new'>(.*?)</td>.*?target='_blank'>(.*?)</a>.*?class='tb5_new'>(.*?)</td>.*?target='_blank''>(.*?)</a>.*", s1, re.S)
        res = re.findall(r"(.*?)</td>.*?target='_blank'>(.*?)</a>.*?class='tb2_new'>(.*?)</td>.*?'tb2_new'>(.*?)</td>.*?</div></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb1_new'>(.*?)</td>.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb1_new'>(.*?)</td>.*?target='_blank'>(.*?)</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td rowspan='2' class='tb5_new'>(.*?)<br.*?target='_blank'>(.*?)\s*?</a></td><td class='tb2_new'>(.*?)</td><td class='tb2_new'>(.*?)</td></tr><tr><td class='tb4_new'>(.*?)</td><td class='tb4_new'>(.*?)</td>.*?class='tb7_new'>(.*?)</td>.*?target='_blank'>(.*?)</a>.*?class='tb5_new'>(.*?)</td>.*?target='_blank'>(.*?)</a>.*", s1, re.S)
        res_tuple = res[0][1::2]
        return res_tuple



