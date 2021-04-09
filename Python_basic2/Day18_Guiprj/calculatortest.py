from tkinter import*

root =Tk()

root.configure(width="400", height="400")

################### 함수 배치 부분 ######################
def plu():
    num1 = int(E1.get())
    num2 = int(E2.get())
    result1 = num1 + num2
    print(result1)
    Lb1=Label(root, text=str(result1))
    Lb1.place(x=10, y=130, width=100, height=30)

def min():
    num1 = int(E1.get())
    num2 = int(E2.get())
    result2 = num1 - num2
    print(result2)
    Lb1=Label(root, text=str(result2))
    Lb1.place(x=10, y=130, width=100, height=30)

def mul():
    num1 = int(E1.get())
    num2 = int(E2.get())
    result3 = num1 * num2
    print(result3)
    Lb1=Label(root, text=str(result3))
    Lb1.place(x=10, y=130, width=100, height=30)

def div():
    num1 = int(E1.get())
    num2 = int(E2.get())
    result4 = num1 / num2
    print(result4)
    Lb1=Label(root, text=str(result4))
    Lb1.place(x=10, y=130, width=100, height=30)

def dem():
    num1 = int(E1.get())
    num2 = int(E2.get())
    result5 = num1 % num2
    print(result5)
    Lb1=Label(root, text=str(result5))
    Lb1.place(x=10, y=130, width=100, height=30)

################### 창 부품 배치 부분 ####################
Button(root, text="+", command=plu).place(x=150, y=30, width=30, height=30)
Button(root, text="-", command=min).place(x=150, y=80, width=30, height=30)
Button(root, text="*", command=mul).place(x=200, y=30, width=30, height=30)
Button(root, text="/", command=div).place(x=200, y=80, width=30, height=30)
Button(root, text="%", command=dem).place(x=250, y=30, width=30, height=30)

E1 = Entry(root)
E1.place(x=10, y=30, width=100, height=30)

E2 = Entry(root)
E2.place(x=10, y=80, width=100, height=30)



root.mainloop()

