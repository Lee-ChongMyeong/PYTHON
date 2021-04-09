#day11_실습1.py


#Quiz_1) 다음과 같은 자료형 요소값들이 있습니다.
a = [1,2, ['a','b',['Life','Live']]]
b = (3,4, ('c','d',('Hello','Hi')))      

#1) 인덱스로 b자료형 안에 4와 'c'와 'Hi' 추출

print(b[1])
print(b[2][0])
print(b[2][2][1])

#2) 인덱스로 a자료형 안에 1,'a','Life'를 10, 'A', 'LIFE'로 변경
a[0] = 10
a[2][0] = 'A'
a[2][2][0] = 'LIFE'
print(a)


#3) 슬라이싱으로 a자료형에 있는 값 'b','LIFE','Live'를 출력

print(a[2][1])
print(a[2][2][0])
print(a[2][2][1])

#Quiz_2)day07의 수강생 과목 실습.py의 5번 문제 수정(수강생 과목 )

#수강생 과목 정보입니다.
#수강생 이름, Python,Linux,Windows,Network의 값을 입력받고,
#입력 받은 값들을 리스트로 저장.
#List_St에 각 점수들만 뽑을 때, while문 이용 후, 합계와 평균값을 구한 후, 다음 조건에 만족하게 코딩
#마무리는 삭제해서 없어진 것 확인!

#80.00점 이상은 합격
#70.00점 ~ 79.xx점이면 미달
#70.00점 미만은 불합격


# List_St = []

# Student = input("수강생이름: ")
# Python = int(input("파이썬점수: "))
# Linux = int(input("리눅스점수: "))
# Window = int(input("윈도우점수: "))
# Net = int(input("네트워크점수: "))

# #List_St = list = [Student, Python, Linux, Window, Net]

# List_St.append(Student)
# List_St.append(Python)
# List_St.append(Linux)
# List_St.append(Window)
# List_St.append(Net)

# i = 1
# hap = 0
# while(i < len(List_St)):
#     hap += List_St[i]
#     i += 1
# avg = hap/ (len(List_St) - 1)

# if 0 <= avg <= 100:
#     if avg >= 80:
#         total = "합격"
#     elif avg >= 70 and hap < 80:
#         total = "미달"
#     else:
#         total = "불합격"
# else:
#     print("다시 입력해주세요")


# print("*"*50)
# print("수강생 : {}".format(List_St[0]))
# print("Python 점수 : {}".format(List_St[1]))
# print("리눅스 점수 : {}".format(List_St[2]))
# print("윈도우 점수 : {}".format(List_St[3]))
# print("네트워크 점수 : {}".format(List_St[4]))
# print("총 점수 : {}".format(hap))
# print("*"*50)
# print("%.2f : %s" %(avg, total))


#Quiz_3)
#김밥천국에서 라면,김밥,떡볶이 3가지를 팔고 있습니다
# 가격은 라면:4,000,김밥:1,500,떡볶이:3,000 입니다
# 음식에 가격을 사용자가 입력한 가격으로 바꿀 수 있으며 메뉴의 이름도
# 변경이 가능한 프로그램을 만들어주세요
#조건
#반드시 리스트를 사용합니다
#프로그램은 다음과 같은 기능을 가지고 있어야 합니다
#1.메뉴 확인
#2.가격 확인
#3.가격 변경
#4.메뉴 변경
#5.프로그램 종료

price = [4000, 1500, 3000]
menu = ["라면", "김밥", "떡볶이"]


while True:
    print("*" * 50)
    print("1. 메뉴 확인")
    print("2. 가격 확인")
    print("3. 가격 변경")
    print("4. 메뉴 변경")
    print("5. 프로그램 종료")
    print("*" * 50)
    choi = int(input("숫자를 입력 하세요 : "))
    print("*" * 50)

    if choi == 1:
        print(menu)

    elif choi == 2:
        print(price)

    elif choi == 3:
        # print("현재 가격 → 1) 라면 : {}, 2) 김밥 : {}, 3) 떡볶이 : {} 4)뒤로가기".format(price[0], price[1], price[2]))
        # cmenu = int(input("변경하실 메뉴를 선택하세요 : "))
        
        # if cmenu == 1:
        #     cmenu2 = int(input("변경하실 가격을 입력하세요 : "))
        #     price[0] = cmenu2
            
        #     continue

        # elif cmenu == 2:
        #     cmenu2 = int(input("변경하실 가격을 입력하세요 : "))
        #     print(cmenu2)
        #     continue

        # elif cmenu == 3:    
        #     cmenu2 = int(input("변경하실 가격을 입력하세요 : "))
        #     print(cmenu2)
        #     continue
        # elif choi == 4:
        #     print("뒤로 가기")
        #     continue
        # else:
        #     print("다시 입력하세요!")
        #     break
        # break1

        print(price)
        n1 = int(input("몇 번 째 가격을 변경?:"))
        if 1 <= n1 <= len(price):
            n2 = int(input("가격은 얼마?:"))
            price[n1 - 1] = n2
            continue
        print("잘못 선택, 처음부터 다시해주세요!")

    elif choi == 4:
        # print("현재 메뉴 → 1) {}, 2) {}, 3) {}".format(menu[0], menu[1], menu[2]))
        # cprice = int(input("변경하실 메뉴를 선택하세요"))
        # continue
        print(menu)
        m1 = int(input("몇 번쨰 메뉴의 이름 변경 ? :"))
        m2 = int(input("바꿀메뉴 이름 입력?:"))
        menu[m1 - 1 ] = m2

    elif choi == 5:
        print("프로그램이 종료되었습니다.")
        break