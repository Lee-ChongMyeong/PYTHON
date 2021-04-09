# 가변인자 리스트는 파라미터(인수, 매개변수, 입력값) 왼쪽에 *을
# 붙여서 선언하며 이 경우 들어오는 자료를 모두 튜플로 묶어서
# * 인수명에 전달합니다.

# def student1(name1):
#     print("출석인원 : %s" % name1)
# def student2(name1, name2):
#     print("출석인원 : %s, %s" % (name1, name2)) 

# student1("김영수")
# student2("김영수", "이영수")

def add_num(*nums):
    sum = 0
    print(type(nums))
    for num in nums:
        sum += num
    return sum
    
result1 = add_num(3,5,7,9)
result2 = add_num()
result3 = add_num(100, 200, 300, 400, 500, 600, 700, 800)
print(result1, result2, result3)


