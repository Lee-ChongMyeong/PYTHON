#day09_실습.py
#1)구구단 만들기
#결과가 그림과 같이 되게 출력해주세요.

# dan = 2
# han = 1

# while dan <= 9:
#     print("===== {}단 =====".format(dan))
#     while han <= 9:
#         print("%d * %d = %d" %(dan, han, dan*han))
#         han += 1
#     han = 1    
#     dan += 1

#2)다음과 같은 별 모양을 만듭니다.(while문 하나로, 이중 while로도 표현)
# *****
# *****
# *****
# *****
# *****

# while문 하나
# i = 1
# while i <= 5:
#     print("*" * 5)
#     i += 1

# print()

# 25바퀴
# j = 1
# while j <= 25:
#     print("*", end='')
#     if j % 5 ==0:
#         print()
#     j += 1

# print()

# 이중 while
# n1 = 1
# n2 = 1
# while n1 <= 5:
#     print("*", end = '')
#     n1 += 1
#     while n2 <= 4:
#         print("*", end ='')
#         n2 += 1
#     print()
#     n2 = 1

# a = 1
# while True:
#     while a <=5:
#         print("*" * 5)
#         a += 1
#         break

#3)
# 현재 사용자가 가지고 있는 돈은 10000원 입니다.
# 사용자는 커피를 사려고 하는데 아메리카노는 3000원, 카라멜 마끼아또 는 4000원, 캔커피는 500원 입니다
# 사용자에게 어떤것을 마실지 입력을 받아서 구매를 하고 만약 잔액이 부족하다면,
# "잔액 부족"이라는 문구가 나오도록 만들어주세요
# -조건
# -사용자가 입력을 할 때 번호 혹은 커피의 이름으로 입력을 해도 정상적으로 작동 할 수 있도록 합니다 
# -커피를 산 후 다시 커피를 살 수 있는 항목이 자동으로 나와야 합니다
# -사용자가 프로그램을 종료 할 수 있어야 합니다
# money = 10000 # 사용자의 금액
# ice_ame = 3000 # 아이스아메리카노 금액
# caramel = 4000 # 카라멜 마끼아또 금액
# can = 500 # 캔커피 금액
# ame = "아이스 아메리카노"
# cara = "카라멜 마끼아또"
# can_coff = "캔커피"

money = 10000 # 사용자의 금액
ice_ame = 3000 # 아이스아메리카노 금액
caramel = 4000 # 카라멜 마끼아또 금액
can = 500 # 캔커피 금액
ame = "아이스 아메리카노"
cara = "카라멜 마끼아또"
can_coff = "캔커피"


while True:
    print("=" * 25)

    print("1. 아이스 아메리카노")
    print("2. 카라멜 마끼아또")
    print("3. 캔커피")
    print("4. 현재잔액")
    print("5. 커피판매기 종료.")

    choi = input("번호나 커피이름으로 입력하세요 : ")
    if choi == "1" or choi == "아이스 아메리카노":
        if money - ice_ame < 0:
            print("=" * 25)
            print("잔액부족. 잔액 : %d 원" %money)
            continue
        else:
            money -= ice_ame
            print("=" * 25)
            print("아이스 아메리카노 구매완료! 잔액 : %d 원" %money)
            continue
    elif choi =="2" or choi == "카라멜 마끼아또":
        if money - caramel < 0:
            print("=" * 25)
            print("잔액부족. 잔액 : %d 원" %money)
            continue
        else:
            money -= caramel
            print("=" * 25)
            print("카라멜 마끼아또 구매완료! 잔액 : %d 원" %money)
            continue
    elif choi == "3" or choi == "캔커피":
        if money - can < 0:
            print("=" * 25)
            print("잔액부족. 잔액 : %d 원" %money)
            continue
        else:
            money -= can
            print("=" * 25)
            print("캔커피 구매완료! 잔액 : %d 원" %money)
            continue
    elif choi == "4":
        print("=" * 25)
        print("현재잔액 : %d 원" %money)
        continue
    elif choi == "5":
        print("=" * 25)
        print("종료되었습니다")
        break
    break