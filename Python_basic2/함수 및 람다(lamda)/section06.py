# Section 06
# 파이썬 함수식 및 람다(lamda)

# 함수 정의 방법 
# def 함수명(parameter):
# code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제 1
def hello(world):
    print("Hello", world)

hello("Python!")
hello(7777)


# 예제 2
def hello_return(world):
    val = "Hello" + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)


# 예제3(다중리턴)
# 파이썬에서는 다중 리턴이 허용된다.

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3, = func_mul(100)
print(type(val1), val2, val3)



# 예제4(데이터 타입 반환)
# 리스틑, 튜플로 반환 가능

def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 예제 5
# *args, *kwargs

def args_func(*args):
    print(args)
    print(type(args))   # 튜플로 넘어오게됨
    for t in args:
        print(t)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')


def args_func2(*args):

    for i, v in enumerate(args):        # 튜플은 인덱스가 없는데 인덱스 생성 가능
        print(i, v)

    for i, v in enumerate(range(10)):
        print(i, v)

args_func2('kim')
args_func2('kim', 'Park')
args_func2('kim', 'Park', 'Lee')    



# kwargs    (* 하나일때는 튜플, *가 두개일떄는 딕셔너리로 받음)
def kwargs_func(**kwargs):
    print(kwargs)
    for k , v in kwargs.items():
        print(k, v)

kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

# 전체 혼합
def example_mul(args1, args2, *args, **kwargs):
    print(args1, args2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)


# 중첩 함수(클로저)
# 변수의 선언을 줄일수 있고, 메모리 관리를 효율적으로 할 수 있다.




def nested_func(num):
    def func_in_func(num):
        print('>>>',num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)



# 예제 6 : 힌트(hint)

def func_mul3(x : int) -> list:         # 이함수는 리스트를 반환하게 되요
    y1 = x * 100                        # 함수의 입력값과 출력값이 무엇인지 명확하게 알 수 있음
    y2 = x * 200
    y3 = x * 300        

    return [y1, y2, y3]


print(func_mul3(5))



# 예제 7

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당

def mul_10(num : int):
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda num : num * 10

print('>>>',lambda_mul_10(10))


def func_final(x, y, func):
    print(x * y * func(10))

func_final(10,10,lambda_mul_10)


print(func_final(10, 10, lambda x : x * 1000))











