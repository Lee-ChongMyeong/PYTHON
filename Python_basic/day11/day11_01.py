#13_3 요소 값 삭제와 변경
#삭제 명령 : del

tul = (1, 3.14, 'a', "abc")

#del tu1[2]     #Error : 튜플 안의 요소값은 제거 불가능

# 변경
##tul[-2] = 'A' # Error : 튜플 안의 요소값은 변경 불가능

# print(tul)
# del tul         # tul 튜플 자체는 제거 가능
# print(tul)      # del로 제거 하면 저장된 데이터 소멸!

# lt = [1, 3.14, 'a', "abc"]
# print(lt)
# del lt[2]
# print("del lt[2]이후 :", lt)

# lt[0] = 1.14
# print("del -> lt[0]변경 : ", lt)

# del lt             # 리스트 lt 데이터 소멸!
# print(lt)

tl = (1, [3.14, "a"], 'b')
del tl[1][0]
print(tl)

# 13_4) 슬라이싱으로 요소값 삭제 및 변경

# lt = [1,2,['a','b']]
# tu = (3,4,['c','d'])

# lt[0:2] = [10,20]
# print(lt)
# del lt[1:]
# print(lt)

##tu[:2] = (30,4)
##del tu[1:]

#13_5)길이 구하는 함수 : len(x)는 x에 몇개 요소가 있는지 갯수를 반환. 묶음형 구할때 사용
a = (1,2,'a', [3,4])
b = [(1,2,3), 'a']
c = "1234"

print('a에 들어있는 요소갯수 : {}개'.format(len(a)))
print('b에 들어있는 요소갯수 : {}개'.format(len(b)))
print('c에 들어있는 요소갯수 : {}개'.format(len(c)))

#2차 자료에 묶인 갯수
print("a[3]의 요소 갯수 : {}개".format(len(a[3])))
print("b[0]의 요소 갯수 : {}개".format(len(b[0])))

