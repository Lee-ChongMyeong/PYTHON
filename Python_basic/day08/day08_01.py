
# 11. <제어문 : 반복문(while)>
# 반복문이란? 유사한 명령코드를 반복해서 실행하는 제어문
# while문은 if문과 유사하게 조건식을 사용
# 조건식이 거짓일 때까진 무한 반복용
# while은 종속 코드를 다 실행하면 다시 자신의 조건식으로 돌아와서 판별 
# if문과 마찬가지로 들여쓰기가 적용!

# 11_1) 기본 사용 문법
# 초기값        # a = 0 -> 반복문의 조건에 들어갈 초기값
                # 한 번 선언 후, 역할 이 끝남.

# while 조건식(값):             # 조건식 -> (True/False)로 되는 조건문
#     반복할 명령문
#     증감식          #(증감식은 필수는 x)
# while 끝난 후 명령문

# 11_2) 무한 반복 예시
# a = int(input("정수값 입력 : "))
# while a:
#     # a += 1  # a = a + 1
#     print('a = ', a)
#     a += 1
# print(a)

# 11_3) 조건식 범위 잡기
# 11_3_0 True/False
# while True:
#   print(True)         # 무한 실행

# While False:
#   Print(False)        # 쓸모 X

# 11_3_1) 1 ~ 5 까지 반복 출력

a = 1

while a <= 5:
    print(a)
    a += 1
print("현재 a:", a)


# 11_3_2) 1 ~ 5까지 반보(초기값이 다른 경우)
a = 0
while a <= 4:       # a < 5
    a += 1
    print(a)

print("현재 a:", a)


# 11_3_3) 5 ~ 0까지 반복 출력
a = 5

while a >= 0:
    
    print(a)
    a -= 1
print("현재 a:", a)

# 11_3_4) 10 ~ 0이 될 때 까지 반복(즉, 0이면 멈추기)\

i = 10

while i != 0:           # i > 0, i >= 1
    print(i, end= ' ')
    i -= 1
print("현재 a:", a)

# 11_4) 1 ~ 10 까지의 합계 구해보기(누적합계 변수명 이용)
a = 1           # 조건식에 사용될 초기값
hap = 0
while a <= 10:
    
    hap += a
    a += 1

print("1 ~ 10까지의 누적 합 : %d" %(hap))

# 11_5) 초기값이 다를 경우(11바퀴)
a = 2
hap = 1

while a <= 10:
    hap += a
    a += 1
print("1 ~ 10까지의 누적 합 : %d" %(hap))

#while문을 사용해서 별 찍기 출력
# 실행 결과
star = 1
while(star <= 5):
        print("*" * star)
        star += 1




