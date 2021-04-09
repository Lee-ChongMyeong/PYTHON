
# datatypestr02

# 문자열을 출력할 떄 줄을 개행해서 출력하고 싶다면 \n 탈출문자를 활용한다.
# 이 문자는 커서가 이 지점에 닿으면 enter키를 눌러서
# 커서를 다음줄로 내려달라는 요청이다.

s1 = "first\nsecond"
print(s1)

s2 = "first\n\nsecond"
print(s2)

s3 = "first\\nsecond"
print(s3)