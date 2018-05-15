import requests
from bs4 import BeautifulSoup


def get_link():
    start_url = 'http://cd.ganji.com/wu/'
    web_data = requests.get(start_url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    channels = soup.select('#wrapper > div.content > div > div > dl > dt > a')
    for num in range(len(channels)):
        channel = 'http://cd.ganji.com'+channels[num].get('href')
        print(channel)


channel_zz = '''
    http://cd.ganji.com/jiaju/
    http://cd.ganji.com/rirongbaihuo/
    http://cd.ganji.com/shouji/
    http://cd.ganji.com/jiadian/
    http://cd.ganji.com/ershoubijibendiannao/
    http://cd.ganji.com/ruanjiantushu/
    http://cd.ganji.com/yingyouyunfu/
    http://cd.ganji.com/diannao/
    http://cd.ganji.com/fushixiaobaxuemao/
    http://cd.ganji.com/meironghuazhuang/
    http://cd.ganji.com/shuma/
    http://cd.ganji.com/laonianyongpin/
'''

channel_nzz = '''
    http://cd.ganji.com/bangong/
    http://cd.ganji.com/xuniwupin/
    http://cd.ganji.com/qitawupin/
    http://cd.ganji.com/ershoufree/
    http://cd.ganji.com/wupinjiaohuan/
'''
