import requests
import bs4
import time
import plyer


DOLLAR_RUB="https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81&aqs=chrome.0.69i59j69i57j0j69i61l3j69i65l2.4064j0j7&sourceid=chrome&ie=UTF-8"

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

last='0,0'
def checker(mode='diff'):

    global last
    full_page=requests.get(DOLLAR_RUB,headers=headers)

    soap=bs4.BeautifulSoup(full_page.content,'html.parser')
    convert=soap.findAll("span",{"class":"DFlfde SwHCTb"})
    res=convert[0].text

    if mode == 'diff':
        print((float(last.replace(',','.'))-float(res.replace(',','.'))))
        if (float(last.replace(',','.'))-float(res.replace(',','.'))<0.1):
            plyer.notification.notify(message="Курс резко вырос!\nКурс 10 минут назад: %sруб\nКурс сейчас: %sруб"%(last,res),
                                      app_icon="dollar.ico",
                                      title='КУРС РЕЗКО ИЗМЕНИЛСЯ')
        elif (float(last.replace(',','.'))-float(res.replace(',','.'))>=0.1):
            plyer.notification.notify(message="Курс резко упал!\nКурс 10 минут назад: %sруб\nКурс сейчас: %sруб"%(last,res),
                                      app_icon="dollar.ico",
                                      title='КУРС РЕЗКО ИЗМЕНИЛСЯ')
    elif mode == 'now':
        plyer.notification.notify(
            message="Текущий курс доллара: %sруб" % res,
            app_icon="dollar.ico",
            title='Уведомление о текущем курсе доллара')
    last=res
    time.sleep(600)




while True:
    for i in range(13):
        if i!=0:
            checker()
        else:
            checker('now')



