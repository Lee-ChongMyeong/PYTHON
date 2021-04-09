# day12_실습2.py

#1)정수값들을 입력받은 후, 리스트에 저장합니다.(갯수는 5개)
#이 때, 정수값들이 정렬된 후, 역순으로 저장해서 출력합니다.
# intlist = list()  #[]
# print(intlist)
# a = 1
# while a <= 5:
#     n = int(input("정수 입력: "))
#     intlist.append(n)
#     a += 1
# intlist.sort(reverse=True)
# print(intlist)


#2)# 변수 안에 문자열을 슬라이싱 혹은 인덱싱 하여 리스트에 저장시키는 문제
# 인덱스 번호를 입력 받아서
# 슬라이싱으로 몇번째부터 몇번째 까지 뽑아서 리스트에 저장
# 인덱싱으로 몇번째 뽑아서 리스트에 저장
# 리스트로 추가된 거 출력
# 초기화 설정
#1.슬라이싱으로 결과		-> 몇 번째부터 ~ 몇 번째 위치까지
#2.인덱싱			-> 몇 번째?
#3.리스트 출력		-> 확인용
#4.초기화
#5.종료

word = "hello my name is chlrkd"
wordlist = []  

while True:
    print("========")
    print("1.슬라이싱")
    print("2.인덱싱")
    print("3.리스트 출력")
    print("4.초기화")
    print("5.종료")
    print("========")
    choi = input("번호 선택: ")
    if choi.isdecimal():
        choi = int(choi)
        if choi == 1:
            n1 = int(input("몇 번 째 글자부터? "))
            n2 = int(input("몇 번 째 글자까지? "))
            wordlist.append(word[n1 - 1: n2])
        elif choi == 2:
            n = int(input("몇 번 째 글자를 뽑겠습니까?"))
            wordlist.append(word[n - 1])
        elif choi == 3:
            print(wordlist)
        elif choi == 4:
            wordlist.clear()
        elif choi == 5:
            break
        else:
            print("없는 번호")
    else:
        print("잘못 입력했습니다. 다시 해주세요.")
