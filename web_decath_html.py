from lxml import html
import json
import requests
JsonList=[]
page=requests.get("https://www.decathlon.in/15107-bikes")
tree=html.fromstring(page.content)
price=tree.xpath('//div[@class="sticker-price sticker-price--normal"]/text()')
BikeModel=tree.xpath('//a[@class="product-name"]/text()')
Manufac=tree.xpath('//span[@class="manufacturer"]/text()')
n=len(price)
l=['₹']
Price = [ x.replace(y,'')  for x in price for y in l if y in x ]
for i in range(n):
 JsonList.append({"Price" : Price[i], "BikeModel" : BikeModel[i], "Manufac":Manufac[i]})
print(json.dumps(JsonList))