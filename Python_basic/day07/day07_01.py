# if문 이어가기

#10 _2)
# 예제 2)

x = 15
if x > 10:
    print("10보다 크다")
if x in (10, 11, 15):
    print("x값에 15가 있다.")
if type(x) is not int:
    print("int 객체")
if x > 10 and x != 15:
    print("거짓 출력 X ")

if x > 10 or x != 15 and x > 25:        # or 앞이 참이라서 다 참으로 인식.
    print("or로 출력")

if (x > 10 or x != 15) and x > 25:        
    print("or로 출력")

if x < 10 and x == 15 or x > 25:        # 거짓
    print("?")

if x < 10 and x == 15 or x < 25:        # 참        // or이 and보다 우선될 수 있음
    print("*")
    

# 예제3)10
v = 95 

if v >= 90 and v < 100:             # 모든 프로그래밍의 숫자 범위 표현판별식
    print("{}는 90이상 100미만이다.".format(v))

if 90<= v < 100:
    print("{}는 90이상 100미만이다.".format(v))

# 예제4) 조건문으로 홀수, 짝수 판별
n = int(input("정수 입력 : "))
nmg = n % 2

if nmg == 0:
    print("입력된 값 {}는 나머지가 {}로 짝수다.".format(n,nmg))
print("첫번째 if문 끝")
if nmg == 1:
    print("입력된 값 {}는 나머지가 {}로 홀수다.".format(n,nmg))
print("두번쨰 if문 종료")


#Quiz_1)두 개의 정수값 n1, n2를 입력받고
# 두개의 값을 비교해서 크면"n1이 n2보다 크다", 작으면 "n1이 n2보다 작다"
# 같으면, "n1과 n2는 같다"를 판별하는 코딩

n1 = int(input("숫자 1 "))
n2 = int(input("숫자 2 "))

if (n1 > n2):
    print("n1이 n2보다 크다")
if (n1 < n2):
    print("n1이 n2보다 작다")
if (n1 == n2):
    print("n1와 n2는 같다.")