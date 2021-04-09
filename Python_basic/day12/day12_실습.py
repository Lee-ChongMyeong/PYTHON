# 이 주민번호를 "-" 기준으로 나눈 후, 생년월일만 뽑은 후, 새로운 변수명에 저장
# 이 때, "1"은 총 몇개인지, 갯수를 구합니다.

pid = "930211-1233219"

# a = pid.split("-")
# print(a[0].count('1'))


a = pid.split("-")[0]
print(a.count('1'))



# stralng 의결과 : "Python Is Important Programing"로 나오게 한다.
strlang = "python:is:important:programing"


print(strlang.title().replace(":", ' ' ).title())
