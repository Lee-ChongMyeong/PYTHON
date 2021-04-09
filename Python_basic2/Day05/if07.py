# elif문은 if문과 else문 사이에 작성할 수 있으며
# 차순위로 비교할 조건식을 작성할 수 있습니다.
# 만약 여러 조건식이 한 번에 성립한다면 위쪽에 있는 조건식이
# 더 높은 우선 순위를 가집니다.

age = int(input("나이를 입력하세요 : "))
if age >=20:
    print("성인입니다.")
elif age >= 17:
    print("고등학생입니다.")
elif age >= 14:
    print("중학생입니다.")
elif age >= 8:
    print("초등학생입니다.")
else:
    print("미취학 아동입니다.")