#day06_02.py

# 10. <제어문(조건문 : if문)>

# 10_1) 조건문(단순 if문)
# 문법                          #들여쓰기(기본 4칸 스페이스바 및 tab키)
# if 조건식:                    #조건식 => 비교/논리/멤버/식별 등
#                               #True/False 인지 판별
                                #:은 아직 끝나지 않았다라는 의미로, 파이썬에선 들여쓰기를 사용하겠다.
                                #조건식이 "참이면", 수행문1, 2를 실행 후 if문 종료
                                #조건식이 "거짓이면", 수행문 1, 2는 실행 X, if문 종료
#    수행문1                    
#    수행문2
# 수행문3                       # if문 종료 되면, 수행문3 실행.

# 들여쓰기
# 파이썬에서 공백 및 tab은 들여쓰기라는 문법이 적용됩니다.
# 명령문 안에 명령문과 바깥 명령문을 구분하기 위한 기능


# 예시
if "배고픔":
    print("밥먹자")

if '':
    print("거짓X")

if " ":
    print("공백도 한칸(참)")

if 0:
    print("숫자는 0만 아니면 다 참(출략X)")

    