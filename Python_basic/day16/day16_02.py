# 22_6) 예제5) 되돌려주는 반환값이 없는 경우(return 문 x )
# def add_sam(a,b):
#     print("{},{}의 합 : {}다".format(a,b, a+b))

# print("먼저, 호출부터 한다.")
# add_sam(3,4)
# print("호출이 끝난 후, 다음 명령 수행")

# print(add_sam(3,4))             # add_sam(3,4)로 함수 호출 되고, print 기능만 한 후, 
#                                 # 호출이 끝남으로 반환값이 없기 때문에 "None" 으로반환

# 22_7) 예제6) return 문이 있을 경우
def sub_sam(a,b):
    res = a - b
    print("{}, {}의 차는 {}다".format(a, b, res))
    return res

n = sub_sam(3,4)
print("반환값 : ", n)

## print(res)   Error           # Error : res 와 매개변수는 sub_sam 함수에서만 존재하는 변수명
## print(a, b)  Error           # 매개변수와 함수 내에서 만들어진 변수명들은 
                                # 그 함수 내에서만 존재하기 떄문에, 외부로 가면 : 자동 소멸"

print(sub_sam(10, 20))          

