#day08_실습.py
#11_7)Quiz_1)1 ~ 10까지 숫자 중 짝수가 나오게 출력하는 코딩
#( while문 + if문, while문만으로 표현)

#1) while + if문
# a = 1
# while a <= 10:
#     if a % 2 == 0:
#         print(a, end=' ')
#     a += 1

#2)while문만
# i = 0
# while i < 10:
#     i += 2
#     print(i, end=' ')

# i = 1
# while i <= 5:
#     print(i * 2, end=' ')
#     i += 1


#11_8)Quiz_2)1 ~ 100까지 숫자 중 7의 배수의 합과 갯수를 출력하는 코딩
# n = 1   #초기값
# hap = 0  #누적합계
# cnt = 0  #누적갯수

# while n <= 100:
#     if n % 7 == 0:
#         hap += n        #hap = hap + n
#         cnt += 1
#     n += 1
# print("7의 배수 합:{},  갯수:{}개".format(hap, cnt))



#11_9)Quiz_3)# 1 ~ 30 까지의 값을 출력 할 때, 다음과 같은 형식으로 출력
#1    2    3    4    5
#6    7    8    9    10
#11   12   13   14   15
#16   17   18   19   20
#21   22   23   24   25
#26   27   28   29   30

# a = 1
# while a < 31:
#     print(a, end='\t')
#     if a % 5 == 0:
#         print()
#     a += 1


#11_10)Quiz_4)
#할아버지의 연세는 68살이다.
#할아버지는 손자의 나이보다 5배에 3살이 더 많다.
#손자의 나이는 얼마인가? 
# son = 1
# while 5 * son + 3 != 68:
#     son += 1
# print("{}살".format(son))



#11_11)Quiz_5)1부터 10까지의 숫자들을 한 개씩 누적한 값들 중 홀수만을 출력
#출력결과 =>       1, 3, 15, 21, 45, 55

a = 1
hap = 0
while a <= 10:
    hap += a
    if hap % 2 == 1:
        if hap == 55:
            print(hap)
        else:
            print(hap, end=', ')
    a += 1
# print("\b\b ")

