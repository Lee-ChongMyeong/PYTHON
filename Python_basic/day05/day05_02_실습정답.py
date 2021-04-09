#day05_실습2.py
#실습(조건: 사용자 입력하는 함수는 반드시 변수에 저장)

#1)사칙연산을 사용자입력으로 나타내어 출력(포매팅 이용)
#결과는 'x+y = ' x+y로 나타내시오.ex) 4+5.1=9.1
# 하나는 정수 입력, 하나는 실수 입력
#+,-,*,/ 4개
x, y = int(input("정수입력: ")), float(input("실수입력"))
print("{} + {:.2f} = {:.2f}".format(x,y, x+y))
print("{} - {:.2f} = {:.2f}".format(x,y, x-y))
print("{} * {:.2f} = {:.2f}".format(x,y, x*y))
print("{} / {:.2f} = {:.2f}".format(x,y, x/y))

#2)두 변수에 값을 입력받은 후 저장된 값 서로 바꾸기
#힌트: 값을 서로 바꿀 땐, 새로운 임시변수를 이용한다.
a,b = int(input("정수1입력: ")), int(input("정수2입력: "))
print("바꾸기 전: {}   {}".format(a,b))
temp = a
a = b
b = temp
print("바꾼 후: {} {}".format(a,b))




#3)수강생 과목 정보입니다.
#수강생 이름, Python,Linux,Windows,Network의 점수를 입력받고,
#합계 와 평균을 구해서 출력
#변수명과 키보드 입력함수 이용합니다.

Student = input("수강생이름: ")
Python = int(input("파이썬점수: "))
Linux = int(input("리눅스점수: "))
Window = int(input("윈도우점수: "))
Net = int(input("네트워크점수: "))

hap = sum([Python,Linux, Window, Net])
avg = hap/4

print(50 * "=")
print("수강생\tPython\tLinux\tWin\tNet\t합계\t평균")
print("""{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8.2f}
""".format(Student,Python,Linux,Window,Net, hap, avg))






