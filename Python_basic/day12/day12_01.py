# 문자열 내장함수 계속

# 14_3) 위치를 요소값으로 인덱스번호 반환(.index())
# a = "Python to python"
# print("인덱스 : ", a.index('p'))
# print("인덱스 : ", a.index('o'))
# print("인덱스 : ", a.index('o', 5))     #.find와 동일
##  print(a.index('1'))                 # Error : 없는 요소값을 index하면 에러!

#14_4) 문자열 안에 삽입해서 반환(.join())
a = ''
print("초기값 : {}, 타입 : {}".format(a, type(a)))
print("join1: ", a.join("1234"))        # a변수명에 "1234" 글자를 삽입
print(a)

b = ','
print("b에 초기값 : ", b)
print("join2:", b.join("1234"))         # b변수명에 "1234"를 "," 를 기준으로 하나씩 삽입.
print(a, b)

a = a.join("abcd")
b = b.join("abcd")
print(a, b, sep=" <-> ")

#14_5) 소문자 -> 대문자(.upper()), 대문자 -> 소문자(.lower())
a = "hello"
print(a.upper())

b = "HELLO"
print(b.lower())

#14_6) 대, 소문자를 유용하게 바꾸는 추가 내장함수들
#.capitalize함수는 용도가 문자열의 첫글자만 대문자로 변환해서 반환
a = "hello. PyThon"
print(a.capitalize())


# .title 함수는 알파벳을 제외한 문자열을 나눠서 각각
# 첫 글자만 대문자로 바꾸는 용도로 변환해서 반환
a = "helloo pyTHon"
print(a.title())

# 14_7) 문자열 바꾸기(.replace(바꾸고 싶은 문자열, 새롭게 바꿀 문자열)) -> 반환
a = "hEllo hEllo hello"
print(a.replace("hE", "He"))
print(a.replace("hE", "He", 1))       # 3번쨰 인수 : 몇 개만 바꿀지 갯수

# 14_8).isdecial()함수는 입력한 문자열이 정수형으로 변환이 가능한지 판별(True, False)
a = "123"
a1 = "abc"
print(a.isdecimal())    
print(a1.isdecimal())

# 14_9) 문자열 나누기(분할) -> .splice()
# " ~ " .split("나눌 기준 값")
# split은 문자열 안에 있는 값을 기준으로 나누기 때문에 "문자열만" 분할 가능하며,
# 분할 할시, 반환을 오로지 "리스트"로만 반환한다. (저장은 별개)

sl1 = "Life Is Too Short"
print("1)split:", sl1.split())  # 디폴트값 (스페이스바, 엔터, 탭 등)을 기준으로 리스트 안에 분할
print(sl1)                      # 저장할 땐, 리스트로 저장할 변수명 필요!

print("2)split:", sl1.split('  '))  # split 은 리스트로 반환, 정확하게 두칸 공백으로만 분할

sl2 = "Life", "Is", "Too", "Short"
print(sl2[0].split('i'))            # 기준값으로 할 경우 값은 소멸

sl3 = "a:b:c"
lt_sl3 = sl3.split(":")
print(lt_sl3, type(lt_sl3))
