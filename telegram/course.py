import requests
import bs4

DOLLAR_RUB="https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83&aqs=chrome.0.69i59j0j69i59j69i57j0j69i61l3.309j0j7&sourceid=chrome&ie=UTF-8"

EURO_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%BA%D1%83%D1%80%D1%81&aqs=chrome.0.69i59l2j69i57j69i61j69i60j69i61j69i65l2.983j1j7&sourceid=chrome&ie=UTF-8"

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def currency_chech(currency):
    if currency=='USD':
        full_page=requests.get(DOLLAR_RUB, headers=headers)
        cur='USD'
    elif currency=='EUR':
        full_page = requests.get(EURO_RUB, headers=headers)
        cur='EUR'
    else:
        full_page = requests.get(DOLLAR_RUB, headers=headers)


    SoapObj=bs4.BeautifulSoup(full_page.content, features="html.parser")
    dig=SoapObj.findAll("span", {"class": "DFlfde SwHCTb"})
    return "Курс {} в текущий момент = {}".format(cur, dig[0].getText())




