
# day19_03.py

# 26.클래스와 객체 활용
# 26_1) 덧셈 계산기

# class Cal:
#     def setdata(self, first, second):
#         self.first = first              # self.first 는 객체를 생성 후, 사용되는 멤버변수로
#         self.second = second            # "객체에 생성되는 객체만의 변수"를 객체변수

#     def add(self):
#         res = self.first + self.second
#         return res
    
# a = Cal()
# a.setdata(3,4)
# print(a.add())

# b = Cal()
# b.setdata(3, 7)
# print(b.add())


# 26_2) 객체변수와 메서드 정의를 이용한 클래스 활용

class FourCal:
    def setdata(self, a, b):
        self.a, self.b = a, b
    
    def add(self, a, b):
       return self.a + self.b

    def sub(self, a, b):
        return a - b

    def mul(self, a):
        return a * self.b

    def div(self):
        return self.a / self.b
    
c1 = FourCal()
c1.setdata(12,4)

print(c1.add(0, 0))     # 16        c1.a + c1.b 라는 객체변수 더한 결과값이 반환
                        # 0,0 은 의미 없음. 아무수나 들어가도 됨.

print(c1.sub(5,3))      # 2         클래스 안에 sub메서드에 전달된 5 - 3 반환
print(c1.mul(2))        # 8         
print(c1.div())         # 3.0





     
