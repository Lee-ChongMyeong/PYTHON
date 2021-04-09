# 연습1 - idol 변수에 문자열 "방탄소년단, 여자친구, 아이오아이"가 
# 저장되어 있습니다.
# split을 이용해 각 가수이름을 추출한 뒤 "파이팅"과 함꼐
# 3줄로 출력하세요(반복문 사용)

idol = "방탄소년단,여자친구,아이오아이"
singer = idol.split(",")

for s in singer:
    print(s, "파이팅")

print("파이팅".join(singer)) # 마지막에 파이팅 안들어감