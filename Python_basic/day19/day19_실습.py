#day19_실습.py

#1)
#클래스: Cal 생성 후, 객체 생성시 자동으로 메서드 받는 생성자 이용
#총 6개(self는 객체변수)를 메서드에 멤버변수로 사용,
#객체는 cal1과 cal2생성
#이 때, 객체로 받는 멤버변수를 제외한 나머지 멤버변수들은 합메서드와,평균메서드
#에 사용될 시, cal1, cal2의 각각 객체변수로 사용되게 만들어봅니다.

# class Cal:
#     def __init__(self, a, b, c, d, e):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.e = e

#     def sum(self):
#         #return self.a + self.b + self.c + self.d + self.e
#         self.sum = self.a + self.b + self.c + self.d + self.e
#     def avg(self):
#         # return (self.a + self.b + self.c + self.d + self.e) /5.0
#         return self.sum / 5

# #결과:
# cal1 = Cal(1,2,3,4,5)
# print(cal1.sum()) # 15
# print(cal1.avg()) # 3.0

# cal2 = Cal(6,7,8,9,10)
# print(cal2.sum()) # 40
# print(cal2.avg()) # 8.0


#2)
#위의 합,평균 메서드 클래스 중,
#객체에 의해 사용될 멤버변수들의 갯수가 정해지지 않았다고 한다면,
#어떻게 하면 사용 가능할까?

class Cal:
    def __init__(self, *args):
        self.args = args

    def sum(self):
        hap = 0
        for a in self.args:
            hap += a
        return hap

    def avg(self):
        return self.sum() / len(self.args)      # self.sum() == Cal.sum() 같은 것임


#결과:
cal1 = Cal(1,2,3,4,5)
print(cal1.sum()) # 15
print(cal1.avg()) # 3.0

cal2 = Cal(6,7,8,9,10)
print(cal2.sum()) # 40
print(cal2.avg()) # 8.0