# 범위를 지정한 다음 빈 리스트를 대입하거나 ([]) del 자료 명령어를 
# 이용하면 리스트 내부 요소를 삭제할 수도 있습니다.

nums = [0, 1, 2, 3, 4, 5 ,6 ,7, 8, 9]
print(nums)
nums[2:5] = []
print(nums)
del nums[4]
print(nums)


# 리스트에도 문자열처럼 +, *를 사용할 수 있습니다.
# +는 양쪽 리스트 연결, *는 반복해서 출력입니다.
list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
listadd = list1 + list2
print(listadd)
listmul = list2 * 4
print(listmul)