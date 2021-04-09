# 12. 제어문(분기문)

# 12_1) break문
# break문은 반복문에서 사용 가능하며,
# 강제적으로 반복문을 빠져나가 프로그램을 중단
# a = 1
# while a:
#     print("a값 : ", a, end= ' ')
#     a += 1
#     break
#     print()
#     print("a += 1:", a)

# 12_2) 이중 while 에서 break
# break는 자신을 종속하고 있는 반복문만 탈출
# 즉, 반복문 전체를 빠져나가는 건 아니다.
# a = 1
# b = 1
# while a == 1:
#     print("a는 %d다." %(a))
#     while b == 1:
#         print("b는 {}다.".format(b))
#         break

# 분기문은 반복문 하나에 하나씩만 적용



# 12_3)예시 (?단 입력시 구구단에서 해당 배수단만 출력(단 0을 입력하면 종료))



while True:
    num = int(input("단을 입력하세요"))
    if num == 0:
        print("구구단 프로그램을 종료합니다.")
        break
    elif 2 <= gugu <= 9:
        n = 1
        while n <= 9:
            print("%d X %d = %d" %(num, n, num * n))
            n += 1
    else:
        print("2단 ~9단 사이값으로 다시 입려갷주세요.")

