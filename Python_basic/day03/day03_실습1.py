
#Quiz_1) 다음과 같은 결과가 나오게 이스케이프 적용
print('"C:\\Program Files\\Python36\\"')
print('"D:\\1 week python\\test\\"')
#print("\"C:\\Program Files\\Python36\\\"")
#print('"D:\\1 week python\\test\\"')

#Quiz_2) 다음과 같은 결과가 나오게 출력 코딩
#단, 이스케이프, print내장함수((sep, end는 적어도 한 번은 적용!!))
print("\t\t#### 회비\\정보 ####")

print("="*50)

print("이름\t\t", end="")
print("나이\t", end="")
print("전화번호\t", end="")
print("회비")

print("="*50)
print("홍길동\t\t", end="")
print("15\t", end="")
print("010","1234","5678\t", end="", sep="-")
print("\\20,000")

print("임꺽정\t\t", end="")
print("20\t", end="")
print("010","2345","6789\t", end="", sep="-")
print("\\30,000")

print("김철수\t\t", end="")
print("28\t", end="")
print("010","3456","7890\t", end="", sep="-")
print("\\50,000")

print("="*50)
print("총합계\t\t\t\t\t", end="")
print("\\100,000")

# print('\t\t#### 회비\\정보 ####')
# print("=================================================")
# print("이름\t\t나이\t전화번호\t회비")
# print("=" * 50)
# print("홍길동\t\t15\t010-1234-5678\t\\20,000")
# print("임꺽정\t\t20\t010","2345","6789\t\\30,000", sep='-')
# print("김철수\t\t", 28, '\t',end='', sep='')
# print("010","3456","7890\t\\50,000", sep='-')
# print("=" * 50)
# print("총합계\t\t\t\t\t\\100","000",sep=',')