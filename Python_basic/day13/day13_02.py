#day13_02.py

#17. 제어문(반복문: for문)

#문법
# for 임의의변수명 in 갯수를가진자료형:           #임의의변수명은 아무이름
#     반복할 수행문

# 갯수를가진자료형(갯수를 가진 것들: 문자열, 튜플, 리스트, 딕셔너리, range() 등)
# while과 다르게 in이란 멤버연산자로 사용해서 갯수를 가진 만큼 횟수로 반복

#사용도: 갯수를 가진 자료형의 0번째인덱스로 자동 시작해서 마지막 인덱스까지 돌고,
#임의의변수명에 자동 인덱싱 하면서 반복

#17_1)range(x) :  0 ~  x 미만의 범위(x는 인덱스번호)
# print(range(5), type(range(5)))
# for a in range(5):      # 0 ~ 4 : 5회 반복
#     print('반복 출력')

# for a in range(10):
#     print("{}번째 반복".format(a))

# a = range(3)
# print(a[3])

#17_2)range(x,y) : x번째부터 ~ y미만의 범위
# for a in range(1, 11):
#     print("%d번" %(a))

#17_3)range(x,y,z) : x번째부터 ~ y미만 범위 중 z만큼 증감
# for a in range(1,11, 2):
#     print(a)


#Quiz_1) 10부터 차례대로 출력해서 1까지 감소해서 출력(range)
# for a in range(10, 0, -1):
#     print(a)






