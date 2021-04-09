from selenium import webdriver
import time
from bs4 import BeautifulSoup
import codecs

f = codecs.open("d:/crawler/result.txt", encoding="utf-8", mode="w")

driver = webdriver.Chrome('D:\crawler\chromedriver.exe')

driver.get("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79")

source = driver.page_source

titlelist = []
authorlist = []
pricelist = []

s1 = BeautifulSoup(source, "html.parser")
s2 = s1.find_all("div", class_="title")
for data in s2[4:]:
    titlelist.append(data.text.strip())

s3 = s1.find_all("div", class_="author")
for data in s3:
    authorlist.append(data.text.strip().replace("\t", "").replace("\n", ""))

s4 = s1.find_all("div", class_="price")
for data in s4:
    pricelist.append(data.text.strip().replace("\t", "").replace("\n", ""))

for idx in range(len(titlelist)):
    f.write(str(idx+1)+"등 도서 정보")
    f.write(titlelist[idx])
    f.write(authorlist[idx])
    f.write(pricelist[idx])
    f.write("-"*50+"\n")




time.sleep(5)
driver.close()

