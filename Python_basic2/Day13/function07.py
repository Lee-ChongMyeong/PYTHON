# return 문은 단독으로도 사용할 수 있습니다.
# return 문 뒤에 아무것도 작성하지 않은 경우는 값을 전달하는 기능
# 은 없이 그냥 함수를 강제 종료시키는 기능만 수행합니다.
# 즉, 함수 내부에서 break문과 같은 용도로 사용할 수 있습니다.

def say_nickname(nick):
    if nick == "바보":
        print("별명을 다시 입력하세요 .")
        return
    print("나의 별명은 %s입니다." % nick)
nickname = input("별명 : ")
say_nickname(nickname)

