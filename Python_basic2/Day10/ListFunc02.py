# del(리스트(인덱스번호]) : 해당 리스트의 해당 인덱스번호 삭제
# 리스트 [:] = [] 해당 범위 자료 삭제, 슬라이싱 지정 가능

score = [88, 95, 70, 100, 99, 80, 78, 50, 50, 50,]

score.remove(100)
print(score)
del(score[2])
print(score)
score[1:4] = []
print(score)

# 리스트 내부 전체 요소 삭제하기
list1 = [1, 3, 5, 7, 9]
list1.clear()
print(list1)

list2 = [2, 4, 6, 8, 10]
list2[:] = []
print(list2)

