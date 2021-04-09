
#별찍기.py

#별모양찍기
#print("*")

#1)         #2)         #3)         #4)         #5)
# *****       *           *****       *****           *
# *****       **          ****         ****          **
# *****       ***         ***           ***         ***
# *****       ****        **             **        ****
# *****       *****       *               *       *****

#1_1)별 5개씩 5번 찍기
# for i in range(5):
# print("*" * 5)

#1_2)
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()

#2)
# for i in range(1,6):
#     print("*" * i)

#2_2)
# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

#2_3)
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*",end="")
#         j += 1
#     print()
#     i += 1


#3)
# for i in range(5,0,-1):
#     print(i *"*")

#3_2)
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
#3_3)
# i = 5
# while True:
#     print("*" * i)
#     i -= 1
#     if i == 1:
#         break


#4)
# for i in range(5,0,-1):
#     print("{:>5}".format("*" * i))

#4_2)
# for i in range(5,0,-1):
#     for sp in range(5-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end='')
#     print()

#5)while +for
# i = 1
# while i <= 5:
#     for a in range(5-i):
#         print(" ",end="")
#     for b in range(i):
#         print("*",end="")
#     print()
#     i += 1

#3_2_6_1:
for i in range(5):
    for j in range(4-i):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    for l in range(i):
        print('*', end='')
    for m in range(5-i):
        print(' ', end='')
    print()
print()
#3_2_6_2:
for i in range(5):
    for j in range(4-i):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    for l in range(4-i):
        print(' ', end='')
    print()
print()

#3_2_7:
for i in range(5):
    for j in range(i):
        print(' ', end='')
    for k in range(9-2*i):
        print('*', end='')
    for l in range(i):
        print(' ', end='')
    print()
print()
#별 문제 :
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    for k in range(8-2*i):  #(4-i)*2도 가능
        print(' ', end='')
    for l in range(i+1):
        print('*', end='')
    print()
