# 알라딘 베스트페이지에 접근해서
# 전체 소스코드를 획득한 다음
# 거기서 "li" 태그 자료만 정제해서
# 갯수가 몇 개인지 확인해보세요

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import codecs

f = codecs.open("d:/crawler/result2.txt", encoding="utf-8", mode="w")

driver = webdriver.Chrome('D:\crawler\chromedriver.exe')

driver.get("https://www.aladin.co.kr/home/welcome.aspx")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

source = driver.page_source

s1 = BeautifulSoup(source, "html.parser")
s2 = s1.find_all("div", class_="ss_book_box")   # 1등 책부터 50등 책까지, s2 자체는 리스트임

# for item in s2:
#     for li in item.find_all("li"):              # 얘 자체가 list 가 되어 버림
#         print(li.text)
#     print("-" * 50)                

# count = 0
# for item in s2:
#     li = item.find_all("li")
#     print(len(li))
#     count += 1
#     if len(li) < 8:
#         print(str(count)+"위")
#         print(li[0].text)
#         print(li[1].text)
#         print(li[2].text)
#     else:
#         print(str(count)+"위")
#         print(li[1].text)
#         print(li[2].text)
#         print(li[3].text)
#     print("-" *50)

count = 0
for item in s2:
    li = item.find_all("li")
    print(len(li))
    count += 1
    f.write(str(count)+"위 도서\n")
    if len(li) < 8:
        f.write(li[0].text)
        f.write(li[1].text)
        f.write(li[2].text)
        f.write("-"*50+"\n")
    else:
        f.write(li[1].text)
        f.write(li[2].text)
        f.write(li[3].text)
        f.write("-"*50+"\n")
    print("-" *50)


print(len(s2))



time.sleep(3)
driver.close()