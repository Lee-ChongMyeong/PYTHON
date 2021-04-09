
#22_13) 디폴트 매개변수의 주의사항

## 1) def say_myself(name = "이름", age = 1, gender):
##2)def say_myself(name, age = 1, gender):

# def say_myself(name, age, gender=True): 
#     print("이름 : {}입니다.".format(name))
#     print(f"나이 : {age}")
#     if gender:
#         print("남자")
#     else:
#         print("여자")

## 1) say_myself(True)
# 중간이나 초음에 초기값을 선정시 그 이후들은 전부 다 초기값 선정을 반드시 해야한다.
## 2) say_myself("최강", 29, True)
#say_myself("최강", 29)


# 22_14) 여러 개 동시 반환은 불가능

# def say_myself(name, age, gender): 
#     print("이름 : {}입니다.".format(name))
#     print(f"나이 : {age}")
#     if gender:
#         print("남자")
#     else:
#         print("여자")

#     #return name, age, gender       # 튜플 자료형으로 자료 1개 반환
#     return name                     
#     return age                      #1) 리턴은 딱 "한 개 " 만 반환 가능!
#     return gender                   #2) 반환 후, 강제로 함수 호출 종료!

# print("반환값 : {}".format(say_myself("최강", 29, True)))

# 22_15) 조건문을 이용한 함수 내에 return 표현
# def Return_Compare(n1, n2):
#     if n1 < n2:
#         return n2
#     else:
#         return n1

# print("3과 4중에서 큰 수는 {}다".format(Return_Compare(3,4)))
# print("3과 4중에서 큰 수는 {}다".format(Return_Compare(4,3)))

# 22_16) Quiz)
# 절댓값 함수 : abs(x) 와 동일한 결과를 반환 해주는 함수 만들어 보기!


# def cp_abs(x):
#     if x <= 0:
#         return -x
#     else:
#         return x

# print("abs(x)와 동일한 기능 {}".format(cp_abs(0)))


# 22_17) Quiz) 두 개의 값을 절대값으로 비교해서 큰 값을 반환하는 함수 구현
# ex) -1 와 -2 중에서 절댓값이 큰 수는 -2다

def cp_abs(x):
    if x < 0:
        return x * (-1)
    else:
        return x 

def Return_Compare(n1, n2):
    if cp_abs(n1) < cp_abs(n2):
        return n2
    else:
        return n1

n1, n2 = int(input("정수1 : ")), int(input("정수2 : "))
print("{}와 {}중 절댓값이 큰 수는 {}다.".format(n1, n2, Return_Compare(n1,n2)))

