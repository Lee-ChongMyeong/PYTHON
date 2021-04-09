#10_4) 조건문(다중 if문 : if ~elif~  else문)

# 문법
# if 조건식1:           # 조건식1이 "참"이면,
#     수행문1           # 수행문 1,2를 실행
#     수행문2
# elif 조건식2:         # 조건식1이 "거짓"이고, 조건식2가 "참"일 때,
#     수행문3           # 수행문3이 실행 후, if 문 종료
# elif 조건식3:         # 조건식1과 2 "거짓"이고, 조건식3이 "참" 일 때,
#     수행문4           # 수행문4이 실행 후     
# else:                 # 위의 조건식들이 다 "거짓"이어야 
#     수행문5           # 수행문 5을 실행 후, if문 종료
# if문 종료후 명령문        


# 예제
a = "Life is too short, you need Health!"
if 'Wife' not in a:
    print('Wife')
elif 'Health' in a and 'you' not in a:
    print("Health!")
elif 'shirt' in a:
    print("shirt")
elif 'need' in a:
    print('need')
else:
    print("None")

