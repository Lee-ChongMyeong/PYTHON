#day06_01.py

# 9. <자료형 연산자 종류>

# 9_1) 산술 연산자(+, -, *, %, //, ** 등)

# 9_2) 대입 연산자 ( = ), 복합대입연산자(+=, -=, *=, /=, %= 등)

a, b = 1,2
print("초기값a : ", a)

a %= b      # a = a + b     #자기가신 = 자기자신 - 연산자 - 다른값(누적)
print(a)    



# 9_3) 관계연산자

# 9_3_1) 크기 비교 연산자 (<. >, <=, >=)

x, y = 3,5

print(x > y, x < y, x >= y, x <= y, sep=", ")

## print('b' >= 'a')  #Error : 크기 비교는 반드시, 숫자들끼리만 비교 가능
# print(5 >= 4.99)


# 9_3_2) 비교연산자 (==, != )
# == 같을 때 True, != 같지 않을 떄 True
# 같냐, 같지 않냐의 비교라 어떤 자료들이든 비교 다 가능!

print(3 == 5)
print(3 != 5)
print(5 == 'a')
print("a" == "a")
print("b" != "B")

# 9_4) 논리 연산자 (and, or, not)
print( 3 < 5 and "a" != "b")    # T and T : T
print( 3 > 5 and "a" != "b")    # F and T : F
print( 3 < 5 and "a" == "b")    # T and F : F
print( 3 > 5 and "a" == "b")    # F and F : F
# and는 논리곱(그리고) : 둘 중 적어도 하나가 False면, 모두 False, 둘 다 True 일 때만 True

print( 3 < 5 or "a" != "b")    # T or T : T
print( 3 > 5 or "a" != "b")    # F or T : T
print( 3 < 5 or "a" == "b")    # T or F : T
print( 3 > 5 or "a" == "b")    # F or F : F
# or는 논리합(또는) : 둘 중 적어도 하나가 True면, 모두 True, 둘 다 False 일 때만 False


print(not True)
print(not False)
print(not (5 > 3))      # not는 논리 부정 ( T -> F, F -> T)

# 9_5) 멤버 연산자(멤버는 항상 여러개 묶는 자료형들이 들어와야함!)

x = 1
print( x in (1,2,3))            # T ( , ,) : 묶음형(튜플자료형())
print( x not in [2,3,4])        # F [ , , ] : 묶음형(리스트 자료형)
print('1' in "1234")            # T 문자열도 묶음형

# in은 멤버 안에 있으면, True / 없으면 False
# not in 은 멤버 안에 없으면, True / 있으면 False

# 9_6) 식별 연산자(자료형 객체 타입이 같은지 다른지 위주로 사용)
x = 1
print(x is x)           # 의미 x / 값하고 값 비교할때는 == 씀.
print(x is int(x))      # 의미 x 
print(type(x) is int)
print(x is int)         # 의미 x 
print(int)
print(type(x) is not float)
print(int is str)       # is 는 이런것 비교하는게 중요한것임

# 식별 : is 는 객체 자료가 같으면, True / is not은 객체 자료가 다르면 True


# 9_7) 연산자 우선 순위
# 1순위) 묶는 것들 -> (, ), [, ], {, }
# 2순위) 인덱스(단항연산자)
# 3순위) 산술 -> 관계, 멤버, 식별, 논리

print( 7 > 18)
print( 6 % 3 > 2)
print(5 + 5 != 2 * 5)
print(1 == '1')
print(10 // 3 == 10 % 3)
print(15 % 4 in (0, 1, 2))
print(3 < 5 and 1 + 2)
print(True == 1)

# 9_8) 부울형 : True, False만을 가진 값

# bool(x)함수는 x가 참, 거짓인지 판별
t, f = True, False  # True가 정수 : 1, False가 정수 : 0

print("t : {}, f : {}, 자료형 : {}".format(t, f, type(t)))      # 크기 : 1Byte(1, 0)

a, b, c, d = 0.001, "", 1, " " 
print(bool(a), bool(b), bool(c), bool(d), sep = ", ")
print(bool(-3.14), bool([1,2]))

# 숫자는 0을 제외한 모든 값들은 전부 참! (0이라는 값만 거짓)
# 문자열은 ""로 아예 값이 없으면 거짓, 나머진 모두 참(값만 존재하면)




