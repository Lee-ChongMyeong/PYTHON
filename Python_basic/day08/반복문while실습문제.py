#day08_실습1.py
#11_7)Quiz_1)1 ~ 10까지 숫자 중 짝수가 나오게 출력하는 코딩( while문 + if문, while문만으로 표현)

#1) while + if 문
num = 1
while (num <= 10):
    num += 1
    if num % 2 ==0:
        print(num, end = ' ')
print()

#2) while 문
# i = 0
# while i < 20:
#   i += 2
#   print(i, end=' ' )      

#11_8)Quiz_2)1 ~ 100까지 숫자 중 7의 배수의 합과 갯수를 출력하는 코딩
num1 = 1    # 초기값
sum1 = 0    # 누적합계
cnt = 0     # 누적갯수
while num1 <= 100:
    
    if num1 % 7 ==0:
        sum1 += num1
        cnt += 1
    num1 += 1
print("7의 배수 합:{}, 갯수:{}개".format(sum1, cnt))

#11_9)Quiz_3)# 1 ~ 30 까지의 값을 출력 할 때, 다음과 같은 형식으로 출력
#1    2    3    4    5
#6    7    8    9    10
#11   12   13   14   15
#16   17   18   19   20
#21   22   23   24   25
#26   27   28   29   30

num2 = 0
while num2 <= 29:
    num2 += 1
    print(num2, end='\t')
    if num2 % 5 == 0:
        print()

#11_10)Quiz_4)
#할아버지의 연세는 68살이다.
#할아버지는 손자의 나이보다 5배에 3살이 더 많다.
#손자의 나이는 얼마인가?

son = 1
while 5 * son + 3 != 68:
    son += 1
print("손자나이 : {}살".format(son))

#11_11)Quiz_5)1부터 10까지의 숫자들을 한 개씩 누적한 값들 중 홀수만을 출력
#출력결과 =>       1, 3, 15, 21, 45, 55

num5 = 1
sum2 = 0 

while num5 <= 10:
    
    sum2 += num5
    if sum2 % 2 == 1:
        print(sum2, end= ', ')
    num5 += 1
print("\b\b ")