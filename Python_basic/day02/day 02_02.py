# 3. <숫자형(진법)>
# 3_1 2진법(Binary), 8진법(Octor), 10진법(Decimal), 16진법(Hexa_Decimal)

print(0b100)
print(0o100)
print(100)
print(0x100)

#진법 표현식을 출력시 결과 : 10진수로 변환

#3_2) 진법 변환함수
# 진법 변환 함수들의 결과 형태는 문자열로 반환!
print(bin(100))
print(oct(100))
print(hex(100))


#3_3) 진법 연산
print(hex(342 + 577))
print(0x5c + 0o26)  

# 에러
## print(hex(bin(100))) #Error : 문자열로 변환된골론 진법 변환 함수 적용 X
## print(hex('ob1000000'))
##print(oct(hex(100) + bin(10)))
print(hex(100) + bin(10))   #'0x64' + '0b1010' -> 문자열 + 문자열은 문자열이 하나로 합쳐짐







