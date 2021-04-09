#ListFun01.py
# 리스트에서 사용하는 메서드들
# append(자료) : 배열의 마지막 인덱스 + 1 위치에 입력된 자료 전부 추가
# insert(위치, 자료) : 지정한 위치 뒤로 기존 자료 밀쳐내고 새 자료 추가
# extend(리스트) : 리스트 + 리스트 처리 ( 단 기존 리스트에 바로 적용)

nums = [1, 2, 3, 4]
nums.append(5)
print(nums)

nums.insert(2, 99)
print(nums)

print("-"*40)

list1 = [1,2,3,4,5]
list2 = [10,11]
print(list1 + list2)    # 순간적으로 더하고, 출력을 하면 롤백이 됨
print(list1, list2) 

list1.extend(list2)     # extend는 명령어를 내리는 즉시, list1이 영구적으로 변함.
print(list1)

