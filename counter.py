import time
from page_parsing import url_list, page_detail


while True:
    c1 = url_list.count()
    c2 = page_detail.count()
    c = {'url': c1, 'detail': c2}
    time.sleep(5)
    print(c)
