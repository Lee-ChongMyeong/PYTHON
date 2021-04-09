# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수


# 선언 
# class 클래스명:
#     함수
#     함수
#     함수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 각각의 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용



# 예제 1

class UserInfo:     # 클래스는 첫글자가 대문자로 원칙
                    # 클래스 선언간 단어와 단어가 연결될 경우, 대문자로 시작
    # 클래스는 속성, 메소드로 구성

    def __init__(self, name):
        self.name = name
#        print("초기화 : ", name)

    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)



# 예제 2
# self 의 이해

class SelfTest: 
    def function1():                # 클래스 메서드
        print("function1 called!")  # self 가 없음
                                    

    def function2(self):            # 인스턴스 메서드
        print(id(self))
        print("fucntion2 called!")

self_test = SelfTest()
## self_test.function1()
SelfTest.function1()
self_test.function2()

# 증명
print(id(self_test))
SelfTest.function2(self_test)


# 예제3
# 클래스 변수, 인스턴스 변수(self 가 들어가야됨)

class WareHouse:
    # 클래스 변수

    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)       # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)          # 자기 네임스페이스에 없으면 클래스 네임스페이스에 가서 변수를 찾고
                                # 거기에도 없으면 에러가 발생




