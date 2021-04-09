# <리스트 및 튜플들의 내장함수>

#15_1)리스트 내장함수들

# 요소값 추가
#. append(x)        # 리스트 안에 x라는 요소값을 추가해서 저장

lst = [1, 2, 3]
print("초기lst : {}".format(lst))
lst.append(1)

print("1)append후 : ", lst)         # 요소값은 항상 마지막 인덱스 부분에 추가됨
lst.append('abc')

print(lst.append('b'))              # .append()는 추가만 하는 함수지 반환 대상 x 
print(lst)                          # "None" 으로 반환되서 반환값 X 

# lst.append(4, 'c')

lst = [1,2,3]
print("초기lst : {}".format(lst))
lst.extend('a')
print(lst)
lst.extend((4,5,6))
print(lst)                          # 튜플로 들어가는게 아니라 4, 5, 6 풀어서 들어감

# .insert(x,y)          # y라는 객체 데이터를 x번쨰 인덱스 위치에 추가
lst = [1,2,3]
print("초기lst : {}".format(lst))
lst.insert(1, ['a', 'b'])
print(lst)

# .pop()                #1) 기본 : .pop()는 리스트의 마지막 인덱스 위치의 요소값을 반환 후, 
                        # 삭제하는 함수
                        #2) .pop(x)는 x번쨰 인덱스 번호를 뽑은 후, 제거

# lst [1, '1', 1.1, (1,2,3)]
# print("초기lst : {}".format(lst))
# print(lst.pop())        # 마지막 인덱스의 요소값 반환후, lst 에서 제거
# print(lst)
# ch = lst.pop(1)
# print(lst)
# print(ch, type(ch))


# .remove(x)            # 리스트 안에 들어있는 요소 x 값을 제거 (반환 x)
lst = [ 1, 2, 3, 4, 1, 1, [5,1]]
print("초기 lst: {}".format(lst))
print(lst.remove(2))
print("제거 후 : ", lst)
lst.remove([5,1])
print(lst)

lst.remove(1)           # 중복값이 존재하면, 시작위치에서부터 1개만 제거
print(lst)

lst.remove(1)
print(lst)

## lst.remove(10)       # Error : 없는 요소값은 제거 불가능

#.clear()               # 리스트의 요소값 모두 제거 (빈 리스트)

lst = [1, 2, ('a', 'b', ["cde", 3, 3.14])]
print("초기lst : {}".format(lst))
lst.clear()
print(lst)

# .reverse()            # 리스트 안에 요소값들을 역순(반환x)
                        # (단, 정렬된 걸 역순이 아닌 현재 자료 상태)
lst1 = [1,2,3]
lst2 = [(1,2), "123", 1, "a", -5, 3.14]
lst1.reverse()
lst2.reverse()
print(lst1)
print(lst2)

# .sort()               # 리스트 요소값을 비교해서 정렬(오름차순)
                        # 기본값 : .sort(reverse-False)

lst1 = [1, 2, 3]
lt1_1 = [1,3,2]
lst2 = ['b', 'a', 'e']
lst1.sort()
lt1_1.sort(reverse=False)
lst2.sort()
print(lst1)
print(lt1_1)
print(lst2)


lst3 = [3.14, 1, 2, 2.0, 1, -3, -3.1]       # 숫자들은 크기순서
lst3.sort()
print(lst3)

lst4 = ['z', 'E', 'e', 'A', 'C', 'b', 'B', 'a', 'Z']
lst4.sort()
print(lst4)

lst5 = ["하양", "ㄱ", "ㅎ", "ㅜ", "탬", "ㄴ", "강이", "최강"]
lst5.sort()
print(lst5)

list6 = [1, 3.1, 2, 'a', 'B', 'c']
##list6.sort()        # Error : 요소값들의 정렬은 크기로 비교
                        # 문자열과 숫자 동시 정렬 x 

lst7 = [4, 2, 1, 3]
lst7.sort(reverse=True)
print(lst7)


# .count(x)
lst = [1, 2, 1, 1, 1, [1,2], [1,2]]
cnt1 = lst.count(1)
cnt2 = lst.count([1,2])
print("{}개".format(cnt1))
print("{}개".format(cnt2))
print("{}개".format(lst[5].count(2)))

# .index()
lst = [1, 2, 3, 1,1,1]
print("인덱스 번호 : ", lst.index(1))
print("인덱스 번호 : ", lst.index(1, 1))
##print("인덱스 번호 : ", lst.index(1, 6))        # Error : 없는 인덱스 위치


# 15_2) 튜플 내장함수(count, index)