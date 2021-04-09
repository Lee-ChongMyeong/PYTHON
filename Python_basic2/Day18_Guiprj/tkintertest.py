# gui 프로그래밍을 위한 tkinter 임포트
from tkinter import * 

# 창 만들고 유지하기
root = Tk()

# 창 크기 설정
root.configure(width="75m", height="100m")

################### 함수 배치 부분 ######################
# 문제 1.
# test라는 이름의 함수를 만들어주세요
# 이 함수는 실행시 콘솔창에
# "Hello Python" 이라는 문장을 출력합니다.
# 함수를 만들고 "테스트 버튼" 버튼에 연결해서 클릭할 때 마다
# 콘솔창에 "Hello Python" 이 출력되게 해보세요.

def test():
    print("Hello Python")

def test2():
    value = E1.get()
    print(value)

def exchange():
    value = int(E2.get())
    result = value / 38.61
    print("원화" + str(value) + "원 : " + str(result) + "NTD")

def onselect(evt):
    w = evt.widget
    index = w.curselection()
    value = w.get(index)
    print(index, value)

################### 창 부품 배치 부분 ####################
Button(root, text="테스트버튼", command=test).place(
    x=10, y=10, width=100, height=30
)

Button(root, text="Entry테스트", command=test2).place(
    x=150, y=10, width=100, height=30
)

Button(root, text="환율", command=exchange).place(
    x=10, y=50, width=100, height=30
)

E1 = Entry(root)    # 문자열로 받아짐
E1.place(x=10, y=130, width=100, height=30)

E2 = Entry(root)
E2.place(x=10, y=180, width=100, height=30)

L1 = Listbox(root)
L1.place(x=130, y=130, width=100, height=150)
L1.insert(0, "피자")
L1.insert(1, "치킨")
L1.insert(1, "햄버거")

Lb1 = Label(root, text="메뉴판")
Lb1.place(x=130, y=110, width=100, height=20)

Sb1 = Spinbox(root, from_=1, to=5)
Sb1.place(x=10, y= 230, width=100, height=30)

option1=["파이썬", "자바", "C++"]        # 옵션에 넣을 것들
variable = StringVar(root)
variable.set(option1[0])    # 메뉴창에 초기에 설정된 값은 "1"
op1=OptionMenu(root, variable, *option1)
op1.place(x=10, y=260, width=100, height=35)


# Listbox의 이벤트 세팅
L1.bind('<<ListboxSelect>>', onselect)


# gui 프로그래밍의 마지막 지점에 항상 작성되어 있어야 한다.
root.mainloop()