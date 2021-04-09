#day07_실습.py

#실습문제:

#1)정수 값 한 개 입력 받고 입력 받은 값이 7의 배수 인지를
#구분하는 코드를 작성합니다.

num1 = int(input("정수 입력 : "))

if num1 % 7 == 0:
    print("7 의 배수 입니다.")
else:
    print("7의 배수가 아닙니다.")

#2)2개의 정수 값을 입력 받아 빼기 계산을 할 때,
#항상 양의 정수(0)가 나올 수 있도록 합니다.


num2 = int(input("정수 입력 1 : "))
num3 = int(input("정수 입력 2 : "))

if num2 >= num3:
    print(num2 - num3)
elif num2 < num3:
    print(num3 - num2) 

#3)다음 코드를 만들어 줍니다.
#-학점 입력하게 코드 작성(변수: score, score는 정수)
#-90이상 100이하면 '학점은 A'
#-80이상 90미만이면 '학점은 B'
#-70이상 80미만이면 '학점은 C'
#-60이상 70미만이면 '학점은 D'
#-'F'
#단, 학점은 0.00 ~ 100.00 범위

score = int(input("학점 입력 : "))

# if score >= 90 and score <= 100:
#     print("학점은 A")
# elif score >=80 and score < 90:
#     print("학점은 B")
# elif score >=70 and score < 80:
#     print("학점은 C")
# elif score >= 60 and score < 70:
#     print("학점은 D")
# elif 0 <= score < 60:
#     print("학점은 F")
# else:
#     print("점수는 0 ~ 100 사이 입력 ")

if 0 <= score <= 100:
    if 90 <= score:
        print("'A'")
    elif 80 <= score:
        print("'B'")
    elif 70 <= score:
        print("'C'")
    elif 60 <= score:
        print("'D'")
    else:
        print("'F'")
else:
    print("점수는 0 ~ 100 사이 입력")



#4)3과 5의 배수를 구분하는 조건문을 코딩
#3과 5의 배수(공배수)면 '{}는 3과 5의 배수다'를 출력
#3의 배수면 '{}는 3의 배수다'를 출력
#5의 배수면 '{}는 5의 배수다'를 출력
#3의 배수도 5의 배수도 아닌 값이면 '{}는 3의 배수도 5의 배수도 아니다'를 출력

number = int(input("정수 입력 : "))

if number % 3 ==0 and number % 5 == 0:
    print("{}는 3과 5의 배수다".format(number))
elif number % 3 ==0:
    print("{}는 3의 배수다.".format(number))
elif number % 5 == 0:
    print("{}는 5의 배수다.".format(number))
else:
    print("{}는 3의 배수도 5의 배수도 아니다.".format(number))

#5)day05_실습2.py의 3번 문제 수정(수강생 과목 )

#수강생 과목 정보입니다.
#수강생 이름, Python,Linux,Windows,Network의 값을 입력받고,
#각 점수들만 뽑아서, 평균값을 구하고, 다음 조건에 만족하게 코딩

#80.00점 이상은 합격
#70.00점 ~ 79.xx점이면 미달
#70.00점 미만은 불합격


Student = input("수강생이름: ")
Python = int(input("파이썬점수: "))
Linux = int(input("리눅스점수: "))
Window = int(input("윈도우점수: "))
Net = int(input("네트워크점수: "))

hap = sum([Python,Linux, Window, Net])
avg = hap/4.0

if avg >= 80:
    total = "합격"
elif avg >= 70 and hap < 80:
    total = "미달"
else:
    total = "불합격"



print("*"*50)
print("수강생 : {}".format(Student))
print("Python 점수 : {}".format(Python))
print("리눅스 점수 : {}".format(Linux))
print("윈도우 점수 : {}".format(Window))
print("네트워크 점수 : {}".format(Net))
print("*"*50)
print("%.2f : %s" %(avg, total))


#결과
# ============================================================
# 수강생의 평균점수는 얼마나 되는지 테스트해봅니다.
# 정보 입력 준비를 해주세요.
# ============================================================
# 수강생 : 최강
# Python점수 : 89
# 리눅스점수 : 88
# 윈도우점수 : 97
# 네트워크점수 : 77
# ============================================================
# 87.75: 합격
# ============================================================

#위에서 이름과 정수는 입력받기
