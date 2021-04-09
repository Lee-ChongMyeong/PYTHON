# 지역변수
# 지역변수는 함수 내부에 선언된 변수입니다.
# 지역변수는 함수가 호출되면 스택영역에 같이 할당되며
# 함수 실행문을 모두 실행하면 지역과 함께 같이 소멸되어 재 호출이  
# 불가능해집니다.

def introduce():
    word = "하이!" # 지역변수 word
    print(word)
introduce()
print(word)