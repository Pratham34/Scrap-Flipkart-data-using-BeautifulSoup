import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div",class_="_4rR01T")
    # print(names)
    for i in names:
        name = i.text
        Product_name.append(name)

    # print(Product_name)    
    # print(len(Product_name))

    prices = box.find_all("div",class_="_30jeq3 _1_WHN1")

    for i in prices:
        price = i.text
        Prices.append(price)
    # print(Prices)    

    desc = box.find_all("ul",class_="_1xgFaf")
    for i in desc :
        des = i.text
        Description.append(des)
    # print(Description)     

    reviews = box.find_all("div",class_="_3LWZlK")
    for i in reviews :
        review = i.text
        Reviews.append(review)

for i in range(len(Reviews),240):
    Reviews.append("None")        

    # print(Reviews)    
# print(len(Reviews))    
# print(len(Description))
# print(len(Prices))
# print(len(Product_name))

df = pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
print(df)

df.to_csv("flipkart_mobiles_under_5000.csv")
















    # print(soup)
    # while True:

    # next page
    # np = soup.find("a",class_="_1LKTO3").get("href")
    # print(np)
    # cnp = "https://www.flipkart.com" + np
    # print(cnp)

    # url = cnp
    # r = request.get(url)
    # soup = BeautifulSoup(r.text,"lxml")




