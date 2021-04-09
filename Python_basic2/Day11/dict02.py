# 사전 데이터 관리
# 사전 자료형은 변경 가능한 자료형입니다. 따라서 실행중에 삽입, 삭제
# 수정등의 편집을 자유롭게 할 수 있습니다.
# 사전에 데이터를 수정하거나 편집할때는
# 사전[key] = value 문법을 사용합니다.
# 추가한 key가 기존에 존재하는 key라면 value 값을 교체해주고
# 그렇지 않다면 key:value 쌍이 사전에 추가됩니다.

dic = {"boy":"소년", "student":"학생", "book":"책"}
dic["book"] = "서적"
print(dic)

dic["girl"] = "소녀"
print(dic)

# 삭제는 del 명령어를 이용해 할 수 있습니다.
# del 명령어를 사용하는 경우 key값을 이용해 key:value를 삭제합니다.
del dic["boy"]
print(dic)

# 딕셔너리 자료형의 key만 따로, 혹은 value만 따로 모아서 받고 싶은
# 경우는 keys(), values()를 사용해 얻어올 수 있습니다.
# 이 경우 key값이나, value 값으로만 구성된 유사리스트(list와는 다른)로
# 결과값이 출력되며, items()는 (key, value) 형태로 묶은
# 튜플 집합을 출력합니다.
# 위의 메서드를 이용해 출력된 자료는 반복문을 이용해 사용할 수 있으나,
# 리스트가 아니기 때문에 편집이 불가능합니다.
print("-" * 40)
print(dic.keys())
print(dic.values())
print(dic.items())  # 튜플 형태로 묶여짐.
print(dic)

# key 값만 모아서 출력 가능
keylist = dic.keys()
for k in keylist:
    print(k)
