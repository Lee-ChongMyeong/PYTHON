# 중첩 반복문은 바깥쪽 반복문이 세로를, 안쪽 반복문이 가로를 담당합니다.
# 아래와 같은 형태의 별을 중첩 반복문을 이용해 찍어주세요.
#    *
#   ***
#  *****
# *******

for x in range(4):
    for y in range(3-x):
        print(" ", end ="")
    for z in range(2*x + 1):
        print("*", end="")
    print()

    

