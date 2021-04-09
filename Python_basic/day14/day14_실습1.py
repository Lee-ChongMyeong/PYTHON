#day14_실습1.py

#17_12)Quiz_1)
#5개의 점수를 입력받아서 리스트 변수명 저장합니다.
#리스트 요소값들 중에서 큰 값(M), 작은 값(m)을 찾아서 출력!
#단, max(),min()함수는 사용 하지 말 것

# score = []
# for a in range(5): 
#     score.append(int(input("점수값 입력:")))
# print(score)

# score.sort()
# print(score[0], score[4],sep=', ')

# M = m = score[0]
# for a in score:
#     if a > M : M = a
#     if a < m : m = a
# print("최대:", M)
# print("최소:", m)

# print(min(score))
# print(max(score))



#17_13)Quiz_2)
#난수(1,100)중 임의값 하나 생성 되면, 그 값이 어떤 숫자인지 맞추는 게임입니다.
# 사용자가 입력한 숫자가 난수보다 큰 지 작은 지를 알려주고,
#10번 기회로 추측해서 난수값을 맞추게 조건 잡아봅니다.
from random import randint
rand = randint(1,100)
for a in range(10000):
    ans = input("번호 입력 (q to exit): ")
    if ans.lower() == 'q':
        print("게임종료")
        break
    if ans.isdecimal():
        n = int(ans)
        if rand == n:
            print("{}: 정답 찾았습니다.".format(n))
            break
        elif rand > n: 
            print("입력값보다 높습니다.")
        elif rand < n: 
            print("입력값보다 낮습니다.")
        print("남은 기회는 {}회 남았습니다.".format(9 - a))
    else:
        print("잘못입력해서 기회가 1개 날랐습니다.")
        print("남은 기회는 {}회 남았습니다.".format(9 - a))
    if a == 9:
        print("기회가 끝났습니다.")
        break