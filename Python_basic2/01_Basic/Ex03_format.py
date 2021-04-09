# Ex03_format.py

'''
format 메서드
- print('{}'.format(데이터))
    > 문자열 출력안의 {}(포맷필드) 위치에 데이터를 출력합니다.

'''

dataA = 100
print("data : ", dataA)
print("data : {}".format(dataA))
print()

dataB = 200
print("dataB : ", dataB)
print()

print("dataA :", dataA, "- dataB :", dataB)
print("dataA : {} dataB : {}".format(dataA, dataB))
print()

title = "python"
name = "귀도 반 로섬"
print("{} 설계자 : {}".format(title, name))

""" ------------------------------------------------------------------------- """

'''
소수점 자리 조정
- { :.소수점자리f }
    > 지정한 소수점 자리까지 출력합니다.
'''

height = 123.1234
print("높이 : {}".format(height))
print("높이 : {:.1f}".format(height))
print()


""" ------------------------------------------------------------------------- """

'''
출력 필드 폭 지정
- { :정수}
    > 해당 위치에 정수값 만큼의 공간확보를 하고 데이터를 출력합니다.

- { :기호 정수 }
    > 기호 : 숫자는 기본이 오른쪽 맞춤이고, 문자열은 기본이 왼쪽 맞춤입니다.
        < : 왼쪽 맞춤
        ^ : 가운데 맞춤
        > : 오른쪽 맞춤

'''

value = 123
print("{}".format(value)) 
print("{:5}".format(value)) 
print("{:<5}#".format(value))
print("{:>5}#".format(value)) 
print("{:^5}#".format(value)) 
print()

word = "abc"
print("{}".format(word)) 
print("{:5}".format(word)) 
print("{:<5}#".format(word))
print("{:>5}#".format(word)) 
print("{:^5}#".format(word)) 
print()


""" ------------------------------------------------------------------------- """