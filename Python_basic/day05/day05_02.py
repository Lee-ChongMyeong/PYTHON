# 8. 키보드 입력 함수 : input("입력할 메세지 : ")는 키보드로 입력받는 함수

# 8_1) input() 사용
# 문법
# 변수명 = input("내용")

# a = input("입력 : ")

# print("a : ", a)
#input()을 사용하면 터미널 창의 커서에다가 원하는 값을 키보드 입력 후, 엔터하면 변수명에 저장



# 8_2) 문자열과 정수, 실수값을 입력받고, 출력?
# s = input("문자열 : ")
# n, f = input("정수 : "), input("실수 : ")
# print("s타입 : {}, n타입 : {}, f타입 : {}".format(type(s), type(n), type(f)))
# print("s : {}, n : {}". format(s, n, f))

# 입력 받은 값은 "항상" 기본값 문자열(str) : input()

s = input("문자열 : ")
n, f = int(input("정수 : ")), float(input("실수 : "))
print("s타입 : {}, n타입 : {}, f타입 : {}".format(type(s), type(n), type(f)))
print("s : {}, n : {}". format(s, n, f))
