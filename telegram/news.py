import requests
import bs4

YANDEX_URL='https://yandex.ru/'

def news_check():
    YANDEX_RESPONSE=requests.get(YANDEX_URL)

    BsObj=bs4.BeautifulSoup(YANDEX_RESPONSE.content, features='html.parser')

    news1=BsObj.select('.news__item-content ')
    news2=BsObj.findAll('a')

    text_list=[]
    for i in news1:
        text_list.append(i.getText())

    href_list=[]
    for i in news2:
        if 'news/story' in i['href']:
            href_list.append(i['href'])

    return  text_list[0:5],href_list[0:5],text_list[6:10],href_list[6:10]
