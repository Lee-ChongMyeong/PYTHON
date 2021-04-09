
# 21. 딕셔너리에서 사용하는 내장함수들

# 21_1) .get()              #1)get(x)는 x에 키를 넣을 시 value를 얻는 함수
                            #2)get(x,y)는 x에 키를 넣을 시, y는 원하는 내용 지정 가능

dic = {"a" : 1, "b" : 2, "c" : 3}
print(dic.get("a"))         # "a"키에 있는 값을 얻어서 출력(검색)
print(f"초기 : {dic}")
##print(dic['d'])           # Error
print(dic.get('d'))         # 존재하지 않는 키 검색시
                            # 얻을게 없으면, None을 출력(디폴트값)
print(dic.get('d', "키 값이 없습니다."))

# get은 값을 검색  용도로 사용해서, 키 값 없어도 에러 x 


# 21_2) .update(x)          # update(x)의 x는 딕셔너리만 올 수 있고, 
                            # 딕셔너리 요소값을 추가 및 변경하는 함수

dic = {"a" : 1, "b" : 2, "c" : 3}
print(f"{dic}")
dic.update(a = 123, d= [1.1, 2, 3.3])
print(f"{dic}")

# 21_3) .keys()와 .values()
# .keys()는 딕셔너리 안에 key 값만 따로 모아서 객체 형태로 반환
a = {"1" : 10, "2" : [10,20]}
print(a.keys())
k = a.keys()
print(k, type(k))           # dict_keys라는 사전형의 키값만 따로 모은 객체 데이터 자료

## print(k[0])              # Error : dict_keys는 인덱싱 지원 x 
                            # (인덱싱 사용 가능하게 자료형 변환 함수를 활용!)

# st_key = str(k)
lt_key = list(k)
tu_key = tuple(k)
print(lt_key, type(lt_key))
print(tu_key, type(tu_key))

# 딕셔너리의 키 값만 묶인 자료형 k를 튜플, 리스트로 변환
print(lt_key[0], tu_key[1])

# .values()는 딕셔너리 안에 values 값들만 따로 모아서 객체 형태로 반환
a = {"A" : 1, "B" : [10, 20]}
print(f"초기{a}")
print(a.values())
v = a.values()
print(list(v), type(list(v)), list(v)[0])
print()

# 21_4) .items()와 .popitem()

# .items 함수는 딕셔너리 안에 key와 value 값을 모아서 객체 형태로 반환(안에 요소는 튜플 : (키, 값))
a = {"A" : 1, "B" : 2}
i = a.items()
print(i, type(i))
print(list(i), tuple(i))

# .popitem 함수는 딕셔너리에 맨 마지막 있는 요소값을 튜플 형태 객체로 뽑은 후, 소멸
a = {"A" : 1, "B" : 2}
print(f"초기 : {a}")
kv = a.popitem()
print(kv)
print(f"소멸 : {a}")
print()

# 21_5) .pop을 이용한 내용 추출
# 문법 : {key: value}.pop(key)
a = {'A' : 90, 'B' : 80, 'C' : 70.5}
print(f"초기: {a}")
res = a.pop('B')                        # 딕셔너리pop은 키값인덱싱으로 디폴트값 생략 x 
print(res)                              # 키값 뽑을 시, value 값 반환
print(a)

# 21_6) .clear()
a = {"A" : 1}
a.clear()
print(a)

# 21_7) .fromkeys() 는 자동으로 키값들을 생성해서 반환 시켜주는 내장함수
# (단, 리스트, 문자열처럼 나열되지 x, 똑같은 걸로 자동 키값에 value 가 생성)

a = dict()
print(a.fromkeys("ABCD"))
print(a.fromkeys(['a','b','c']))        # .fromkeys(x)는 x라는 묶음형 자료 요소로 키값 변환

b = {}
print(b.fromkeys("AB", [1,2,3]))        # .fromkeys(x,y)는 y값이 value 값으로 변환

# 21_8) for 변수명 in 딕셔너리
a = {"A" : 1, "B" : 2}
print("A" in a)                         # 멤버 연산자 (대상 : key값)

ID = {"a" : 1234, "b" : "abcd"}         # 아이디 : 비밀번호

for i in ID:
    print(i)                            # 키값만 뽑힘

id1 = input("아이디 등록 : ")
pw = input("비밀번호 : ")

if id1 in ID:
    print("이미 등록된 아이디 입니다.")
else:
    print("없는 아이디입니다.")
    ID[id1] = pw

print(ID.get(input("아이디 확인"), "존재 X"))
