
# 26_3) 클래스 안에 메서드 정의(생성자)

class Cal:
    def __init__(self):                 # __?__ 는 Method 중에서 클래스에서만 사용 가능한 메서드(생성자)
                                        # 사용 가능한 메서드(생성자:Contructor)
        self.res = 0                    # 아까의 전역변수라고 보면됨, 초기화
        self.res2 = 1

    def add(self, n):                   # __init__ 은 객체새 생성될 때, "자동으로 호출되는 메서드"
        self.res += n
        self.res2 *= n
        return self.res, self.res2
        

c1 = Cal()
print(c1.add(3))
print(c1.add(4))

c2 = Cal()
print(c2.add(3))
print(c2.add(4))

# 생성자란? 객체가 생성될 때, 클래스의 멤버변수를 초기화하거나,
# 객체 생성과 동시에 할 작업들 기술할 때 사용

# 26_4)  자동으로 클래스 안에 삽입한 인수를 객체로 정의
class myself:
    def __init__(self, name, age):
        self.name, self.age = name, age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

m1 = myself("최강", 29)         # __init__ 자동 초기화 생성자   -> 생성할 떄, 메서드에 name, age를 미리 전달해서 자동 초기화
m2 = myself("chlrkd", 39)       # 객체 생성하자 마자 원하는 값으로 초기화

print(m1.get_name())
print(m1.get_age())

