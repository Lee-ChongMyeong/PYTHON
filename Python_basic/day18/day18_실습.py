
# Q1   

#1. 구구단 중 1개만 입력해서 그 단만 출력되게 gugu를 만들어주세요.
# def gugu(dan):
#     for i in range(1,10):
#         print("{} X {} = {}".format(dan, i, dan*i))
        
# dan = int(input("단을 입력하세요 : "))

# gugu(dan)

def gugu(n):
    print("{:=^9}".format(n))
    for i in range(1,10):
        print("{} X {} = {}".format(n, i, n*i))
gugu(int(input("단 입력 : ")))

# Q2
# 2. max,min 함수의 기능을 가지고 있는 pymax,pymin 함수를 만들어주세요.

# def pymax(*args1):
#     list2 = []
#     for i in args1:
#         list2.append(i)
#         list2.sort(reverse=True)
#     return print(list2[0])

# pymax(2,4,6,8)

# def pymin(*args2):
#     list1 = []
#     for i in args2:
#         list1.append(i)
#         list1.sort()
#     return print(list1[0])

# pymin(1,3,5,7)

def pymax(*args):
    mx = args[0]
    for i in args[1:]:
        if mx < i : mx = i
    return mx 

M = pymax(-5,1,3,5,6,7,8,55)
print(M)

def pymin(*args):
    mn = args[0]
    for i in args[1:]:
        if mn > i : mn = i
    return mn
m = pymin(-5,1,3,5,6,7,8,55)

print(m)

# Q3 함수

#3. + 와 - 기능이 있는 계산기를 만들어 주세요.
# 1)덧셈, 뺄셈 함수 만들기
# 2)실행하는 main()함수 만들기
# 3)main()안에서 +,- 할 것 고르게 하기(+는 0, -는 1로 하되 나머지값으로 이용할것)
# 4)main실행시 두 개의 정수 계산 결과 출력!

# def main(num1, num2):
#     if choice =="+":
#         return num1 + num2
#     else:
#         return num1 - num2

# num1 = int(input("숫자1을 입력하세요 : "))
# num2 = int(input("숫자2을 입력하세요 : "))
# choice = input("연산을 입력하세요(+, -)")

# print(main(num1, num2))

# def add(n1, n2):
#     return n1 + n2
# def sub(n1, n2):
#     return n1 - n2

# def main():
#     n = int(input("0번('+'), 1번('-')"))
#     n1 = int(input("첫번쨰 정수 입력 : "))
#     n2 = int(input("첫번쨰 정수 입력 : "))

#     if n % 2 == 0:
#         return "{} + {} = {}".format(n1, n2, add(n1, n2))
#     else:
#         return "{} + {} = {}".format(n1, n2, sub(n1, n2))

# print(main())

# Q4 람다

# x = int(input("숫자1을 입력하세요 : "))
# y = int(input("숫자2을 입력하세요 : "))
# choi = input("연산을 입력하세요(+, -)")

# main = lambda x,y : x + y if choi == "+" else x - y 
# print(main(x,y))

n = int(input("0번('+'), 1번('-')"))
n1 = int(input("첫번쨰 정수 입력 : "))
n2 = int(input("첫번쨰 정수 입력 : "))
add = lambda n1, n2: n1 + n2
sub = lambda n1, n2: n1 - n2
main = lambda : add(n1,n2) if n % 2 == 0 else sub(n1, n2)

print(main())