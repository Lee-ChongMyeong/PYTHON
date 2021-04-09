user = {'ck':'1234'}

print("아이디와 비밀번호를 입력하세요.")
while True:
    print("{:=^21}".format("로그인메뉴"))
    print("1. 로그인")
    print("2. 회원가입")
    print("3. 비밀번호 찾기")
    print("4. 비밀번호 수정")
    print("5. 종료")
    print("=" * 26)
    menu = int(input("메뉴를 입력해주세요: "))
    if menu == 1:
        ID = input("아이디: ")
        if ID in user:
            Password = input("비밀번호: ")
            if Password == user[ID]:
                print("로그인 성공!")
                break
            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("존재하지 않는 회원입니다.") 
    elif menu == 2:
        ID = input("회원님이 사용하실 ID를 입력해주세요 : ")
        if ID in user:
            print("이미 사용하고 있는 ID입니다. 메뉴화면에서 다시 입력해주세요!!")
        else:
            Password = input("회원님이 사용하실 패스워드를 입력해주세요 : ")
            user[ID] = Password
            print("회원님은 정상적으로 ID를 생성하셧습니다.")
    elif menu == 3:
        ID = input("회원님이 사용하신 ID를 입력해주세요 : ")
        if ID in user:
            print("회원님이 사용하신 비밀번호는 %s 입니다." % user[ID])
        else:
            print("그런 아이디는 존재하지 않습니다.")
    elif menu == 4:
        ID = input("회원님이 사용하신 ID를 입력해주세요 :")
        if ID in user:
            Password = input("회원님이 변경하실 비밀번호를 입력해주세요 :")
            user[ID] = Password
            print("회원님의 비밀번호가 정상적으로 변경되었습니다.")
        else:
            print("그런 아이디는 존재하지 않습니다.")
    elif menu == 5:
        print("로그인 메뉴를 종료합니다.")
        break   