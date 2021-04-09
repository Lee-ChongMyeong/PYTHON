
#27. 모듈(Module)

# 27. 모듈(Module) : 표준 라이브러리에서 미리 만들어진 함수들이 있는 "스크립트파일"을 불러와서 사용

# 먼저, 복습 차원 random() 불러오기 

# from random import random

# # 0 ~ 9 임의의 값을 5개 불러오기

# for i in range (5):
#     print(int(random()*10))

# [파이썬 기본 모듈 : 외부에서 가지고 와서 호출(외장파일)]
# C:\Program Files\Python36\Lib (실제 파이썬 설치한 경로 안에 Lib/폴더 안에 있음)

# 27_1) 모듈 임폴트(import) 
# import는 파이썬 코드를 작성해 놓은 스크립트 파일(*.py) 안에 
# 변수명, 함수, 클래스 등 정의되어 있는 것을 불러온다.


# 기본 사용되는 자동 함수(ex: len(), print(), input() 등 등)는 모듈 할 필요 x 
# 외부 모듈을 불러서 사용시 import

# 27_2) math라는 공학용 모듈 불러오기
# import math     # math 라는 모듈 호출
## print(pi)    # Error : 이렇게 호출하면, 어디 안에 만들어진 pi인지를 모름
                # math 라는 모듈 안에 있는 pi를 호출 : math.pi
# print(math.pi)      # 원주율 값 파이

# print(math.sqrt(2)) # 루트 2
# print(math.factorial(5))    # 5! = 120



# 27_3) Quiz) random(), randint(-10, 10)를 import 만 불러오기
# import random
# print(random.random())
# print(random.randint(-10, 10))



# 27_4) from [모듈이름.py] import [함수명, 변수명, 클래스명 등] : 모듈로부터 import에 호출한것만 불러옴
# from math import pi, factorial, sqrt #math 모듈로부터 import에 선언한 3개 호출
# print(pi)
# print(sqrt(4))
# print(factorial(3))
## print(math.pi)   # math 자체를 import 한게 아니라서 안됨. math 자체를 모듈 한 건 x 


# 27_5) import [모듈] as [별창] : as는 alias 로 이름이 복잡할 때, 짧게 별도로 칭해주는 기법
# import statistics               # 통계학을 지원하는 모듈
# pts = [65, 55, 74]
# print((65 + 55 + 74) / 3)
# print("평균", statistics.mean(pts)) 
# print("분산 : ", statistics.variance(pts))
# print("표준편차 : ", statistics.stdev(pts))

# import statistics as st
# pts = [65,55,74]
# print("평균", st.mean(pts)) 
# print("분산 : ", st.variance(pts))
# print("표준편차 : ", st.stdev(pts))

# 27_6) Quiz_2) math 안에 있는 factorial 함수를 f로 별칭해서 이용!
# from math import factorial as f
# print(f(5))

# 27_7) 표준 모듈 time : 시간 관련된 기능들 제공
# 대표적인 함수 : time() -> 기계의 시간 계산

# 이 함수는 1970년 01월 01일 자정시간 기준으로 현재까지 경과한 시간을 초 단위로 반환
from time import *      # *은 전체 대상(모든것)
# while True:
#     print(time())

# sleep(x) 함수 : 슬립함수는 x초 단위로 기다렸다가 실행되게 해줌
# n = 0
# while True:
#     sleep(1)
#     n += 1
#     print("n : ", n)


# 27_8) 기타 모듈들
import os                    # 운영체제와 관련된 모듈
os.system("ping 8.8.8.8")                  # 시스템에서 사용할 수 있는 명령어를 실행해주는 함수 : system("명령어")

while True:
    print("계속 하려면 아무키나 눌러주세요 ...")
    os.system("pause")        # pause는 윈도우 명령어 중 잠시 멈추게 하는 명령어