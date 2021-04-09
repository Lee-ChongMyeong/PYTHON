# 22_8) 매개변수명 (리스트)

# def hap(a):
#     i = 0
#     for x in a:
#         i += x
#     return i

# res = hap([1,2,3,4,5,6])
# print(f"합:{res}")
# print(sum([1,2,3,4,5,6]))

# print(max(1, 2, 3))

# 22_9) 예제7) 인수값이 몇개인지 알 수 x
# def sum_many(*args):            # 가변인수
#     # print(*args)       : 디버깅(가변인수로 묶인거라 자료 형태가 정해져 있진 x )
#                                 # 가짜 매개변수라고 보면 됨.
#     ## print(type(*args))       # TypeError
#     print(args, type(args))     # 튜플형으로 활용

#     hap = 0
#     for a in args:
#         hap += a
#     return hap

# res = sum_many(1,2,3,4,5)
# print("합 : ", res)

# 인수값이 몇 개든 (자료형 등 ) 상관 x , *args처럼 매개변수명 앞에 *을 붙이면,
# 함수 호출 시 인수값들 전부 모아서 "튜플형태"로 만들어줍니다.
# args는 arguments(인수값)로 명칭을 "가변인수"라 합니다.
# 가변인수는 *매개변수명으로 표현 하면 다 가변인수로 적용!
# ex) *args대신, *ck

# 22_10) 예제8) 인수값을 문자열과 가변인수로 구성
def sum_mul(choi, *args):
    if choi == "합":
        res = 0
        for i in args: res += i

    elif choi == "곱":
        res = 1
        for i in args: res *= i

    else:
        res = "잘못 선택"

    return res

res1 = sum_mul("합", 1,2,3)
print(res1)

res11 = sum_mul("합", 1, 1.1, 2, 2.14)
print(res11)

res22 = sum_mul("곱", 1,2,3,4,5)
print(res22)

res3 = sum_mul("1", 1,2,3,4,5,6)
print(res3)


# 22_11) 가변인수(주의사항)

# def sum_mul(*args, choi):
#     if choi == "합":
#         res = 0
#         for i in args: res += i

#     elif choi == "곱":
#         res = 1
#         for i in args: res *= i

#     else:
#         res = "잘못 선택"

#     return res

# print(sum_mul(1,2,3, "합"))


# 가변 인수는 모든 인수를 다 받기 때문에 항상 마지막에 표현 해야한다!


# 22_12) keyword 파라미터   **kwargs
# **kwargs : 딕셔너리 인수값들만 받는 매개 변수 (변수명(키) = '값' 으로 묶인 인수값)

def dic_kwargs(**kwargs):
    # print(kwargs)
    lt = [ ]
    for i in kwargs: 
        lt.append(i)
    return lt
    # return [i for i in kwargs]

k_res = dic_kwargs(a=1, b=2, c=3.14)
print(k_res)

print(list(dict(a=1, b=2, c=3.14).keys()))



