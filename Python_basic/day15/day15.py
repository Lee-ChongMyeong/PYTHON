#day15_01.py

# 딕셔너리 계속

# 20_2) dict(변수명 = '값')함수로 딕셔너리 변환(사전형 변환 함수)
# a = 5
# dc = dict(a = 1, b = [10, 20])
# print(dc)
# print(a)
## print(b)     #Error : dict()는 변수명 -> 키값 변환(변수명 생성X)

# 20_3) 딕셔너리 값 추가
# 사용 형식
# 딕셔너리변수명[추가하고 싶은 key] = 추가하고 싶은 value

# a = {"이름" : "최강"}
# print(f"초기값 a : {a} ")
# print(a["이름"])
# a["나이"] = 29
# print("사전값 추가 : ", a)

# 20_4) 딕셔너리 값 삭제
# 사용 형식
# del 딕셔너리 변수명 [키값]
# dic = {'a' : 10, 'b' : {'A' : 100}}
# print(f"초기 : {dic}")
# del dic['b']
# print(dic)
# del dic['b']['A']
# print(dic)
#del dic         # 딕셔너리 객 체 소멸
#print(dic)

# 20_5) 딕셔너리의 값 변경
# 딕셔너리는 중복된 키 값 추가 X
# 사용하면 기존에 있떤 키 안에 value 값만 변경 

# 사용 형식
# 딕셔너리변수명 [ 존재하는 key ] = 변경할 value

a = {"이름 " : "최강", "나이" : 29}
print(f"초기 : {a}")

a["이름 "] = "Choi Gang"
print(f"변화 : {a}")
