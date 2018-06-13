import requests
import json
from bs4 import BeautifulSoup
reqq=requests.get("https://www.decathlon.in/15107-bikes")
soup=BeautifulSoup(reqq.content,'html.parser')
products=soup.find('ul', {'id': 'product_list'})
JsonList=[]
price=[]
BikeModel=[]
Manufac=[]
#getting price details
for j in products:
 oneby=j.find('div', {'class' : "box-product"})
 price.append(oneby.find('div', {'class':'sticker-price sticker-price--normal'}).get_text())
for i in products: #Getting Bike Model
 BikeModel.append(i.find('div', {'class':'box-product__footer'}).get_text())
for n in products: #Getting Bike Brand
 Manufac.append(n.find('span',{'class': 'manufacturer'}).get_text())
n=len(price)
#Printing Price and Brand together
#for i in range(n):
# print ('\n price:{0}, 	 BikeModel:{1},	 	Manufac:{2}'.format(price[i],BikeModel[i],Manufac[i]))
#dictio=dict(zip(price,BikeModel))
#print(dictio)
#Removing Rs. Symbol from Price to save as json format
l=['₹']
Price = [ x.replace(y,'')  for x in price for y in l if y in x ]
for i in range(n):
 JsonList.append({"Price" : Price[i], "BikeModel" : BikeModel[i], "Manufac":Manufac[i]})
print(json.dumps(JsonList))	
