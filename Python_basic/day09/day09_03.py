# 12_4)continue문
# 반복문 안에 continue문을 사용시 아래 명령문을 실행하지 않고,
# 강제로 반복문 맨 처음으로 이동하는 분기문

# 1 ~ N 까지의 수 중에서 짝수값만 출력하는 프로그램
# N는 정수값 직접 입력

# N = int(input("정수 입력 : "))
# n = 0
# while n < N:
#     n += 1
#     if n % 2 == 1:
#         continue
#     print("짝수 :", n, end=' ')

# if문 단독으론 break, continue 불가능(반복문안에서 적용)
# if True:
#     break
#     continue

# 12_5)예시 코드(콜라판매기가 있고, 콜라는 총 10개 있다.)
# 단, 리필 할 땐, 콜라 갯수는 좋지 않으며, 판매기 종료 버튼 만들것

cola = 10   # 콜라의 초기갯수
while True:
    print("1번 : 콜라 클릭")
    print("2번 : 콜라 리필")
    print("3번 : 판매기 종료")
    print("="*20)
    choi = int(input("원하는 버튼 입력 : "))

    if choi == 1:
        if cola == 0:
            print("품절")
            continue
        print("콜라가 나왔습니다.")
        cola -= 1
        print("현재 콜라는 {}병 남았습니다.".format(cola))

    elif choi == 2:
        print("콜라가 리필되었습니다.")
        print("콜라는 {}병 그대로 남아있습니다.".format(cola))
    
    elif choi == 3:
        print("판매기 전원 off")
        break
