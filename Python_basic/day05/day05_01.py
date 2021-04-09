#7_2) 변수명 활용

v = 1 # 변수 하나 정의

v1,v2,v3 = 1, '1.0', 3.14  # 변수명 여러개 선언: 변수명1, 변수명2, ... = 값1, 값2, ...

print("정수 : {}, 문자열 : {}, 실수 : {:.2f}".format(v1, v2, v3))

print("초기값 v : ", v)
v3 = v1 + v3 - 10
print("{:.2f}".format(v3))
v1 = v3 = v
print("v1 : {}, v3 : {}".format(v1, v3))

#7_3) 자료형 확인 함수 : type(x)는 x값의 자료형 어떤 객체 데이터 형식인지 출력 
a, b, c = 1, 1.1, '1'
print("a값 : {},    자료형 : {}".format(a, type(a)))        #int : Integer(정수형 객체)
print("b값 : {},    자료형 : {}".format(b, type(b)))        #float : Float(실수형 객체)
print("c값 : {},    자료형 : {}".format(c, type(c)))        #str : STring(문자열 객체)

print(type(a), type(c))                                    #디버깅 : 오류 문제점을 하나씩 분석(코드 수정) 
                                                           #중간에 print()로 출력하는 과정도 디버깅!
## print("a + c = {}".format(a + c))                          #Eroor : 정수 + 문자열

#7_4) 변수명 안에 자료형 형태 변환 함수
#변수변환

v1, v2, v3 = '1', 1, 1.1

# int(v1) : v1에 저장된 값이 정수형 변환
# float(v2) : v2에 저장된 값이 실수형 변환
# str(v3) : v3에 저장된 값이 문자열 형태 변환

print("초기값 : v1 : {}, v1 : {}, v3 : {:.1f}".format(v1, v2, v3))
print("자료형 : {}, {}, {}".format(type(v1), type(v2), type(v3)))

# v1 + v2 -> 2
v1 = int(v1)
print("변환 후 v1 : {}, 자료형 : {}".format(v1, type(v1)))
#print(v1 + v2)
v2, v3 = float(v2), str(v3)
print("{}는 {}".format(v2, type(v2)))
print("{}는 {}".format(v3, type(v3)))

#7_5) 자료형 변환 함수의 실패 예시)
s1, s2 = '1', 'a'
print("s1: {}, s2: {}".format(s1, s2))
print("s1타입 : {}, s2타입 : {}".format(type(s1), type(s2)))

print(int(s1), float(s1), sep=' , ')
print(type(int(s1)))
print("s1 자료형 : {}".format(type(s1)))        # 자료형 변환함수는 형태를 "일시적으로만" 변환
                                                # 영구적으로 유지시키려면 변환된 결과로 초기화!

print(type(str(int(s1))), type(str(float(s1)))) #str()은 문자열로 표기로만 변환시키면 되므로, 무조건 100% 됨.
                                                #? -> "?"

## print(int(s2))                               # Error : 문자열 -> 정수 변환은 ' ' 표기 떼는 것
                                                # 문자열 안이 숫자일 경우만 가능

## print(float(s2))                             # Error : 문자열 -> 실수 변환도 ' ' 표기 떼는 것

v = '1.0'
print(int(float(v)))

