#Q1)

# dic = dict(국어 = 80, 수학 = 70, 영어 = 90)
# #print(dic)

# avg = (dic["국어"] + dic["수학"] + dic["영어"])/ len(dic)
# print("평균 : {}".format(avg))

# Q2)
# 딕셔너리 응용하기
# 원하는 사전 만들기

# 사용자에게 사전에 등록하고 싶은 단어와 뜻을 입력 받습니다.
# 그럼 그 단어와 뜻이 딕셔너리에 저장이 되어야 하며 정상적으로
# 단어를 검색을 하면 뜻이 출력이 됩니다.
# 아래와 같은 기능이 있어야 합니다.

# 1. 단어 추가
# 2. 뜻 변경
# 3. 단어 검색하면 뜻 출력
# 4. 단어 삭제
# 5. 프로그램 종료

dic = dict()

while True:
    print("1. 단어 추가")
    print("2. 뜻 변경")
    print("3. 단어 검색하면 뜻 출력")
    print("4. 단어 삭제")
    print("5. 프로그램 종료")
    print("="*25)
    choi = int(input("번호 선택: "))
    if choi == 1:
        word = input(" 추가할 단어 입력 : ")
        mean = input(" 단어의 뜻을 입력 : ")
        dic[word] = mean

    elif choi == 2:
        word = input("변경할 단어 입력 : ")
        dic[word] = input("뜻 변경 : ")

    elif choi == 3:
        word = input("검색할 단어 입력 : ")
        print(dic[word])

    elif choi == 4:
        word = input("삭제할 단어 입력 : ")
        del dic[word]
        print(dic)

    elif choi == 5:
        print("시스템을 종료합니다.")
        break