# 로또 번호 추첨 프로그램을 만들어주세요.
# 단 gui 형태로 만들어주셔야 합니다.

# "추첨"이라고 써진 버튼을 클릭했을 때
# 번호 6개를 출력하게 만들어주세요

# "초기화"라고 써진 버튼을 눌렀을 떄는 출력된 로또번호가
# 삭제되도록 만들어주세요

# 추첨을 연달아 누르면 누를때마다 다시 번호를 추첨합니다.

# "제작자"라고 써진 버튼을 누르면 본인의 이름 나오게

import random
from tkinter import *

root = Tk()

root.configure(width="70m", height="100m")

################### 함수 배치 부분 ######################
def click():
    global Lb1
    getnumber = []
    while (len(getnumber)) != 6:
        number = random.randint(1,45)
        if number not in getnumber:
            getnumber.append(number)
    getnumber.sort()
    Lb1 = Label(root, text=getnumber)
    Lb1.place(x=50, y=110, width=150, height=60)


def reset():
    global Lb1
    Lb1.destroy()
    Lb1 = Label(root, text="")
    Lb1.place(x=50, y=110, width=150, height=60)

def dev():
    Lb2 = Label(root, text="제작자 : 이총명")
    Lb2.place(x=50, y=250, width=150, height=60)


################### 창 부품 배치 부분 ####################
Button(root, text="추첨", command=click).place(x = 10, y = 60, width=110, height=30)
Button(root, text="초기화", command=reset).place(x=130, y= 60, width=110, height=30)
Button(root, text="제작자", command=dev).place(x=80, y= 200, width=100, height=30)

Lb1 = Label(root)       # global 처리 때문에 만들어 놓은 것임

root.mainloop()