
# 26_5) 육면체 부피를 구하는 클래스 생성(초기값 및 가로, 세로, 높이 원하는대로 부피 구하기)

class Vol:
    def __init__(self, 가로, 세로, 높이):
        self.가로, self.세로, self.높이 = 가로, 세로, 높이  # 3개 자동 초기화

    def set_가로(self,가로):
        self.가로 = 가로
    def set_세로(self, 세로):
        self.세로 = 세로
    def set_높이(self, 높이):
        self.높이 = 높이

    def get_vol(self):
        return self.가로 * self.세로 * self.높이

    def __str__(self):              # __str__ 생성자는 객체 생성 후, 객체 자체를 출력시,
                                    # 문자열로 자동 반환되는 생성자
        return "가로:{}, 세로:{}, 높이:{}".format(self.가로,self.세로,self.높이)

v1 = Vol(100,100,100)       # 초기값 넣음
print("부피 : {:,}m^3".format(v1.get_vol()))

v1.set_가로(200)
print("가로 바꾼 부피 : {:,}m^3".format(v1.get_vol()))

print(v1)

