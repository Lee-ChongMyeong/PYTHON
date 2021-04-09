#Ex03-Quiz_format.py

'''
이름, 나이, 키를 변수에 저장해서 출력하는 코드를 작성하세요
- 키는 소수점 첫쨰자리까지만 출력됩니다.
'''

name = "이총명"
age = 23
height = 179.3245

print("이름 : ", name)
print("나아 : ", age)
print("키   :  {:.1f}cm".format(height))
print()

'''
오늘 날짜의 년월일만 변수에 저장해서 출력하세요
'''

year = 2020
month = 12
day = 16

print(year,"년", month,"월", day,"일")
print("{} 년 {} 월 {} 일".format(year,month,day))
print()

'''
아래의 제품이름과 가격을 각각 변수에 저장해서 출력하는 코드를 작성하세요

--- 제품 목록 ---
bluetooth 5.0    8000
ssd 512G         120000
'''

pro1 = "bluetooth 5.0"
pro2 = "ssd 512G"
price1 = 8000
price2 = 120000

print("---- 제품목록 ----")
print("{:20}{:10}원".format(pro1, price1))
print("{:20}{:10}원".format(pro2, price2))





