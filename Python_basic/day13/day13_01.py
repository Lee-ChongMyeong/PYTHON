#day13_01.py

# 16. <랜덤함수>
#랜덤함수: random()는 random.py라는 외부 파일에서 불러와서 안에 정의된 함수를 이용
#(모듈: 무언가를 불러와서 사용)

#16_1)랜덤함수 모듈화
# from random import random  # random.py(스크립트)로부터(from) random 함수(import)를 가지고 와서 불러옴.

# print(random())             # 0.0XXX 초과 ~ 1.0 미만 값
# print(random() * 10)        # 0.0XXX 초과 ~ 10.0 미만 값
# print(int(random() * 10))   # 0 ~ 9 (정수범위)

#16_2)Quiz
# 1 ~ 10 까지의 임의의 값을 생성
# print(int(random() * 10)  + 1)
# 1 ~ 100 까지의 임의의 값을 생성
# print(int(random() * 100)  + 1)
# 100 ~ 999까지의 임의의 값을 생성
# print(int(random() * 900) + 100)


#16_3)randint(x,y)는 x이상 ~ y이하 정수값 랜덤 호출
# from random import randint
# print(randint(5,10))        #5이상 10이하 값 중 임의 값
# print(randint(-1000,1000))


#16_4)randrange(x,y,z)는 x이상 ~ y미만 중 z씩 증감 범위 랜덤
# from random import randrange
# print(randrange(5,10,2))       #5부터 2씩 증가 된 값부터 ~ 10미만 까지의 임의 값


#16_5)ASCII코드(키보드에 있는 값을 컴퓨터가 알아듣게 번역되는 코드(2^7: 0 ~ 127인 128개))
#chr(정수)는 아스키코드로 정수 -> 문자로 반환하는 함수
# print(chr(65), chr(97), sep=', ')
#ord('문자')는 아스키코드로 문자 -> 정수로 반환
# print(ord('A'), ord('a'), sep=', ')













