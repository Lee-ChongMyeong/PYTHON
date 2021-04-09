# 50개의 "-" 를 출력하되 매 5번째에는 "+"가 출력되도록
# for in 문을 작성해주세요.

for x in range(1,51):
    if x % 5 :
        print("-", end="")
    else:
        print("+", end="") 

print()

# 50개의 "-"를 출력하되 5, 15, 25, 35, 45 번쨰마다 "+"가
# 출력되도록 for in 문을 작성해주세요.

# for x in range(1,51):
#     if (x+5) % 10:
#         print("-", end="")
#     else:
#         print("+", end="")

for x in range(1,51):
    if x % 10 == 5:
        print("+", end="")
    else:
        print("-", end="")

print()




