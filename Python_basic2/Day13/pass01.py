# pass구문
# pass 구문은 아무것도 하지 말라는 명령어입니다.
# 보통 def나 if, for 등처럼 : 을 사용하는 문법은
# 아래쪽에 반드시 실행문을 작성해야 하는 경우가 있는데
# 이 때 실행문 부분을 비워두고 싶을 때 사용할 수 있는것이
# 바로 pass입니다.

print("안녕하세요 여러분 ~~")
pass
print("오늘 날씨가 흐리네요.")

# 함수를 이름만 만들어놓고 실행문을 배치하지 않으면 에러가 남

# def abc(): error

def abc():
    pass

score = 90
if score >= 50:
    pass
else:
    pass

