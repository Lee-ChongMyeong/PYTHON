# return 구문의 용도는 사실 두 가지 입니다.
# 1. return 값을 호출한 위치에 가져다 둔다.
# 2. return 문 실행시 즉시 함수를 종료한다.
# 이 두가지는 동시에 진행되는 로직입니다.
# 따라서 문장에 2개 이상의 return 문을 작성하면 첫번쨰 리턴문까지만
# 함수가 실행되고 바로 종료됩니다.

def sum_and_sub(n1, n2):
    return n1 + n2
    return n1 + n2
result = sum_and_sub(7,2)
print(result)