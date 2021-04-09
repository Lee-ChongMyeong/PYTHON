# Ex04_string.py

'''
문자열
- 문자 데이터 여러개의 집합입니다
'''

print("python 문자열")
print('python 문자열')
print('''외따옴표 3개를 사용하면 
여러줄의 문자열을
한번에 출력 할 수 있습니다 ''')

'''
문자열 연산
- 숫자처럼 문자열끼리 서로 더하거나 곱하는게 가능합니다.
'''

textA = "smile"
textB = "^^"
print("textA : ", textA)
print("textB : ", textB)

stn = textA + " " + textB   # " " : 공백
print(stn)

print((textA * 4))
print()

'''
문자열은 문자들의 집합이기 떄문에 특정위치의 문자를 선택해서 사용 할 수 있습니다. 
- 각 문자 위치에서 <index(번호)>가 부여되어 있습니다
- index는 0부터 시작해서 1씩 증가합니다.
   Ex) 변수명 [index]
'''

# +       012345 6 7 8 
nation = "korea대한민국" 
# -       98765 4 3 2 1     [뒤에서 시작할떄는 -1 부터 시작]


print("nation : ", nation)
print("nation[0] :", nation[0])
print("nation[6] :", nation[6])
print("nation[-3] : ", nation[-3])
