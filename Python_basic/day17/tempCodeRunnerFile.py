a = 1
def vt():
    global a    # global(광역)은 미리정의된 변수명(전역변수)를
    a += 3      # 함수 내에 지역변수로 사용되는데, 지속이용(값 소멸x)

print("전역변수 a초기값 : ", a)
vt()
print(a)