import sys,requests,json,os
from datetime import datetime
from bs4 import BeautifulSoup
start=datetime.now()
print(start)
def scraping():
    for i in url:
        page = requests.get(i)
        soup = BeautifulSoup(page.content, 'html.parser')
        filtered = soup.find("ul", {"id": "product_list"})
        a = filtered.prettify()
        price = []
        model = []
        manufac = []
        oup = []
        for i in filtered:
            price.append(i.find("div", {"class": "sticker-price sticker-price--normal"}).get_text())
        for i in filtered:
            manufac.append(i.find("span", {"class": "manufacturer"}).get_text())
        for i in filtered:
            model.append(i.find("a", {"class": "product-name"}).get_text())
        n = len(price)
        for i in range(n):
            oup.append('Model:{0},Price:{1},Manufac:{2}'.format(model[i], price[i], manufac[2]))

        print(json.dumps(oup))
        endt = datetime.now()
        print(endt)

def pagination():
    global url
    url=["https://www.decathlon.in/15107-bikes"]
    page = requests.get("https://www.decathlon.in/15107-bikes")
    soup = BeautifulSoup(page.content, 'html.parser')
    pages=soup.find("div", {"id":"pagination_bottom"})
    for i in pages:
        ur = i.find('a')
        eee=ur.get('href')
        url.append("https://www.decathlon.in/15107-bikes"+ ur.get('href'))
    print(url)

pagination()
scraping()
