from selenium import webdriver
import time


# 네이버로 이동한 다음 검색창에 "교보문고"를 입력하고
# 검색버튼을 누르게 해 주세요. 이동한 페이지에서 결과창에 나오는
# 교보문고 버튼을 클릭해서 페이지에 접근하게 만들어주세요.

driver = webdriver.Chrome('D:\crawler\chromedriver.exe')
time.sleep(3)
driver.get("https://www.naver.com")
search  = driver.find_element_by_xpath('//*[@id="query"]')
search.send_keys('교보문구')        #search.send_keys('교보문구\n')     -> enter 키 기능  
driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="header"]/div[3]/ul[2]/li[1]/a').click()


