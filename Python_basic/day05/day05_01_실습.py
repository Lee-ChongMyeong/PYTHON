# day05_실습.py
# 다음의 변수에 저장되어 있는 값을 활용하여 동일한 결과가 나오게 해주세요
# 자료형 변환 함수 이용
x,y,z = '100', 10.5, 20

#1) 110.5
#2) 10020
#3) 10.520.0
#4) 110.520

print(int(x) + y)

print(x + str(z))
print(int(x)**2 + z)
print(pow(int(x),2)+z)

print(str(y)+str(float(z)))
#print("{}{}".format(y,float(z))

print(str(int(x)+y)+str(z))
print("{}{}".format(int(x) + y,z))