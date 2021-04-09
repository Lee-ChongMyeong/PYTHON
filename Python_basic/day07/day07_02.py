#10_3) 조건문(if ~ else문)

# 문법
# if 조건식:              # 조건식이 "참이면",
#     수행문1             # 수행문 1,2 를 실행 후, if문 종료
#     수행문2           
# else:                   # 위의 조건식이 "거짓일 때", 발동
#     수행문3              # 수행문3을 실행 후, IF문 종료
# if else문 끝난 후 수행

# 예제01)
money = 5000
card = False

if card or money >= 4000:
    print("택시")
else:
    print("걷기")
print("if~else 종료 후, 프린트")

# 예제02)
x = 15
if x > 15:
    print("x가 15보다 크다")

else:           #단순 if문? if x <= 15
    print("x는 15보다 작거나 같으므로 거짓")

#Quiz_2)짝수와 홀수 구별

n = int(input("정수 입력 : "))
nmg = n % 2

if nmg == 0:
    print("입력된 값 {}는 나머지가 {}로 짝수다.".format(n,nmg))
else:
    print("입력된 값 {}는 나머지가 {}로 홀수다.".format(n,nmg))
