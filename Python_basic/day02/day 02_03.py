# day02_03.py

# 4. <숫자형(함수 및 연산자)>

#4_1) 크기 비교 함수
print(max(3.1, 7, -1, 4))  # 7 최댓값
print(min(3, 7, -1.1, 4))  # -1 최솟값

#4_2) 연산 함수 및 연산자 (sum([]), pow(), divmod(), round(), abs())

#4_2_1) sum([x, y, ...]) 는 [x, y, ...] 안의 모든 값들을 더해서 합계 구하는 함수

print(sum([1, 2, 3, 4, 5]))

#4_2_2) pow(x,y)는 x^y의 결과
print(pow(5,2))

# x ** y : 거듭제곱 연산자
print(5 ** 2)

#4_2_3) divmod(x,y)는 x를 y로 나눠서 결과를 (몫, 나머지)
print(divmod(10,3)) #(3, 1)
print(divmod(10,5)) #(5, 0)
# x // y 는 몫만 반환, x % y는 나머지를 반환
print(10 //3, 10 % 3); print(10 // 2, 10 % 2)

#4_2_4) round(x.y, z)는 소수 x.y를 소숫자리 z까지 나타내기 (반올림)
print(round(11.52, 1))
print(round(11.56, 1))
print(round(11.12 + 1.123, 4))

#4_2_5) abs(x)는 정수x를 절댓값 반환
print(abs(5)); print(abs(-5))

##print(abs(-1, -2))    #Error : 인수는 ' 한 개 ' 만
print(abs(-1), abs(-2))


