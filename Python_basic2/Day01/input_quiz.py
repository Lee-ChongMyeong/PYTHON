# 1. 회원의 이름과 성별 그리고 나이를 입력받으세요.
# 2. 이름 변수는 name, 성별은 gender, 나이는 age 입니다.
# 3. 입력받은 값을 통해 회원의 이름과 성별과 나이와 출생년도를 출력하세요.

name = input("이름을 입력하세요 : ")
gender = input("성별을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))

print("이름 : ", name)
print("성별 : ", gender)
print("나이 : ", age)
print("출생년도 : ", 2020 - age)

"""------------------------------------------"""

name = input("이름을 입력하세요 : ")
gender = input("성별을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))
birthYear = 20220 - age + 1

print("이름 : ", name)
print("성별 : ", gender)
print("나이 : ", age)
print("출생년도 : ", birthYear)

