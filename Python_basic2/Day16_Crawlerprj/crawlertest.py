from selenium import webdriver
import time

driver = webdriver.Chrome('D:\crawler\chromedriver.exe')

driver.get("https://www.naver.com")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="account"]/a/i').click()      # 괄호안에 ' ' 쓰기 

userid = driver.find_element_by_xpath('//*[@id="id"]')
userid.send_keys('dlchdaud1004')

userpw = driver.find_element_by_xpath('//*[@id="pw"]')
userpw.send_keys('cleverlee1512')

driver.find_element_by_xpath('//*[@id="log.login"]').click()

time.sleep(5)

driver.close()


