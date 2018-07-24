import requests
from bs4 import BeautifulSoup
import json


class product_names:
    def __init__(self, products):
        final_scrape = []
        self.name= [product.find("a", {"class": "product-name"}).get_text() for product in products]
        self.price=[product.find("div", {"class": "sticker-price sticker-price--normal"}).text.replace('₹','') for product in products]
        length=len(self.name)
        for i in range(length):
            final_scrape.append({"Name": self.name[i], "Price": self.price[i]})
        print (json.dumps(final_scrape))
    def scrape(url):

        #url=["https://www.decathlon.in/15098-jogging-shoes"]
        reqq = requests.get(url)
        soup = BeautifulSoup(reqq.content, 'html.parser')
        box_product = soup.find_all("ul", {"id": "product_list"})
        name = [ product_names(product) for product in box_product ]


def pagination():
    reqq=requests.get("https://www.decathlon.in/15098-jogging-shoes")
    soup=BeautifulSoup(reqq.content,'html.parser')
    pages = soup.find("ul", {"class": "pagination"})
    url.append('https://www.decathlon.in' + (pages.find('a').get('href')))
    return ([product_names.scrape(link) for link in url])
url=["https://www.decathlon.in/15098-jogging-shoes"]
pagination()
