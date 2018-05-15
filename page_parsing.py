import requests
from bs4 import BeautifulSoup
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
page_detail = ganji['page_detail']


def get_detail_link1(channel, page):
    time.sleep(1)
    web = channel + 'o' + str(page) + '/'
    web_data = requests.get(web)
    soup = BeautifulSoup(web_data.text, 'lxml')
    txt = soup.find_all(text="下一页")
    if txt:
        links = soup.select('a[href*="detail"]')  # css*= 获取href属性含有detail的tag（只有转转平台的商品链接有detail)
        link = links[::2]  # 取奇数序号的值，因为相邻图片和标题的链接一样
        for num in range(len(link)):
            url_list.insert_one({'link': link[num].get('href').split('?')[0]})
    else:
        pass


def get_page_detail_zz(channel):
    time.sleep(1)
    web_data = requests.get(channel)
    soup = BeautifulSoup(web_data.text, 'lxml')
    title = soup.select('div.box_left_top > h1')
    price = soup.select('div.price_li > span > i')
    area = soup.select('div.palce_li > span > i')
    page_detail.insert_one({'title': title[0].text, 'price': price[0].text, 'area': area[0].text})











