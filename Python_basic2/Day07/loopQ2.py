# 구구단 전체 출력 
# for dan in range(2, 10):
#     print(dan, "단")
#     for hang in range(1,10):
#         print(dan, "*", hang, "=", dan*hang)
# 아래 코드를 while문을 사용한 중첩 코드로 변경해주세요.
# 힌트 -> while문 하나당 변수 하나를 써야 합니다.

#dan = 1
#hang = 0
#
#while dan < 9:
#    dan += 1
#    print(dan, "단")
#    
#    while hang < 9 :
#        hang += 1
#        print(dan, "*", hang, "=", dan * hang)
        
dan = 2
while dan < 10:
    hang = 1        # hang변수는 도입부에 쓰면 안됨. 중요 !!! 
    print(dan, "단입니다.")
    while hang < 10:
        print(dan, " * ", hang, "=", dan*hang)
        hang += 1
    dan += 1