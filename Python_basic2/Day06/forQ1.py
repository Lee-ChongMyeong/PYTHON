# 문제
# 1부터 1000까지의 숫자 중 n의 배수의 합을 구할 수 있도록
# for in 문을 사용해서 코드를 작성해주세요.
# n의 배수의 값은 input()을 이용해 입력받습니다.

sum = 0
add = int(input("n을 입력하세요 : "))

for number in range(0,1001, add):
    sum += number
    
print(" 총 합 : " + str(sum))

