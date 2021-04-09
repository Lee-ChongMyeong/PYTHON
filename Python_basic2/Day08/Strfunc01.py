# 문자열은 숫자 자료에 비해 복잡하므로 보다 다양한 함수, 메서드를
# 사용해 편집하거나 조작할 수 있도록 지원합니다.
# 함수 : 공용적으로 내장된 기능(. 없이 실행)
# 메서드 : 클래스에 속한 함수 (.가 왼쪽에 붙음)

s = "python programmig class"

print(len(s))

print(s.find("o"), s.rfind("o"))

s1 = "C programming"
if s1.find("java") == -1:           # find와 rfind : 찾는 문자가 없을 경우 -1을 리턴합니다.
    print("C와 관련없는 단어입니다.")
else:
    print("C와 관련된 단어입니다.")

# print(s1.index("x")) #에러 발생

print(s.count("python"))

s2 = """ 생각이란 생각할수록 생각나므로 생각하기 말아야 할 생각은 
생각하지 않으려고 하는 생각이 옳은 생각이라고 생각합니다. """

print("'생각'의 등장 횟수 : ", s2.count("생각"))

