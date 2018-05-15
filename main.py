import time
from multiprocessing import Pool
from extract_url import channel_zz
from page_parsing import get_detail_link1, get_page_detail_zz, url_list


def get_all_detail_link(url):
    time.sleep(1)
    for i in range(1, 100):
        get_detail_link1(url, i)


def get_all_page_detail():
    links = url_list.find()
    li = list(links)
    num = url_list.count()
    urls = []
    for i in range(num):
       urls.append(li[i]['link'])
    for j in range(len(urls)):
        get_page_detail_zz(urls[j])


if __name__ == '__main__':
    pool = Pool()
    start = time.time()
    # pool.map(get_all_detail_link, channel_zz.split())
    pool.apply_async(get_all_page_detail)
    pool.close()
    pool.join()
    print('all subprocess done')
    end = time.time()
    print('总共耗时:', end-start)


