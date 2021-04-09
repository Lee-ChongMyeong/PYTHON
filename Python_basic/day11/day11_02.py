#14. <문자열 관련 내장함수들>

# 14_0)"".format()



# 14_1) 문자 갯수 세서 반환(.count())
a = "Python to python"
#print("갯수 : ", a.count('p') )

#"~".count("요소값")은 요소값의 갯수가 몇 개인지 반환
# .이 연결 연산자(안으로)
# print("없는 것 : ", a.count('1')) #없는 요소는 0개로 반환



# 14_2) 위치를 요소값으로 활용해서 인덱스번호로 반환(검색) : .find(), .rfind()
a = "Python to python"
print("'p'", a.find('p'))
print("'o'", a.find('o'))       # "~" 중 시작 위치에서부터 맨 처음에 찾은 것

print("'p(1)'       'o(2)': ", a.find('o', 5), a.find('o', 9))

#.find('?', 시작인덱스번호, 끝인덱스번호)를 하면 시작은 인덱스위치부터 범위 안에서 검색!
print(a.find('1'))      # -1은 못찾을 경우 반환

# .rfind 함수는 find 함수와 기능은 동일하지만,
# 차이점은 인덱스 번호 시작위치가 오른쪽 -> 왼쪽(역순)

print(a.rfind('o'))