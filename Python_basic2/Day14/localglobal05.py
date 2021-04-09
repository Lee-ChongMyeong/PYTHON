# 지역 내부와 변수가 전역변수와 같은 변수가 되도록 동기화해야 합니다.
# 이때 사용하는 키워드가 바로 global입니다.
# global 키워드를 받은 변수는 전역변수와 동기화됩니다.
# 따라서 global 키워드는 전역변수가 미리 선언되어야만 쓸 수 있습니다.

price = 1000
def sales():
    global price # 지역변수 price를 새로 만들지 말고 동기화
    price = 500 # 전역변수 price의 값이 500으로 변경

sales()
print(price)

