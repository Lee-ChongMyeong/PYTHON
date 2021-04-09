

# 24. lamda라는 기능으로 함수 정의를 간편하게 사용 객체 데이터
# (함수정의 def 와 동일한 기능)

# 문법
# 변수명 = lamda 매개변수명1, 매개변수명2, ... : 리턴될 값
#값 안에다가 결과 기능 변수명에 초기화
# 함수의 결과값이 간단하게 나올 때 주로 이용....

# 24_1 def 형식
# a, b = 1,2
# def add(x,y):
#     return x + y
# print(add(a,b))     # 3 
# print(add)          # <function add at 0x00000155784960D0> 메모리 주소값(16진수)
# print(type(add))    # function : 함수

# 24_2) lambda 형식

# a, b= 1, 5
# add = lambda x,y : x + y
# print(add, type(add))
# print(add(a,b))


# 24_3) lambda를 이용한 이중 함수 객체 정의 1)
# a, b= 3, 4
# add = lambda x, y : x + y
# mul = lambda x, y : x * y

# print(add(a,b))
# print(mul(a,b))

# 24_4) lambda를 이용한 이중 함수 객체 정의 2)
# a, b = 3, 4 
# lam_list = [lambda x,y : x+y, lambda x,y : x*y]
# print(lam_list, type(lam_list))                     # 람다는 객체 데이터로 저장됨.
# print(lam_list[0](a,b))                             # 7
# print(lam_list[1](a,b))                             # 12

# 24_5) lambda에 조건문 활용(단, if ~else만 가능)

# elif 사용 불가능.

# a = int(input("정수입력 : "))
# ## odd = lambda a: "짝수" if a % 2 == 0             # 단순 if문으로는 안됨
# ## print(f"{a}는 {odd}"")

# odd = lambda a: "짝수" if a % 2 == 0 else "홀수"
# print(f"{a}는 {odd(a)}")


# 24_6) lambda에 리스트 내포를 이용해서 for 문 구현
f = lambda *args: [x * 3 for x in args]
print(f(1,2,3))




