#day13_03.py

#17_4)문자열
# for ch in 'abcd':
#     print(ch)

# for kor in "파이썬":        #3회: 한글은 글자 하나당 횟수
#     print(kor)


#17_5)튜플 및 리스트형태의 반복문
# for i in [1, 2.27, "abc"]:
#     print(i, type(i))


# a = [(1,2), (3,4), (5,6)]   #1차 리스트 -> 2차 튜플

# for x in a:     #3개 튜플
#     print(x)

# for (x,y) in a:
#     print(x)
#     print(y)
#     print(x + y)



#17_6)Quiz_2)
# st = "Python Is Programing Language !!!"
# 문자열st 안에 공백을 제외한 문자의 개수를
# 출력하는 프로그램을 만들어주세요
st = "Python Is Programing Language !!!"

#1)for문
# cnt = 0  #공백이 아닌 문자의 갯수
# for a in st:
#     if a != ' ':
#         cnt += 1
# print("{}개".format(cnt))

#2)while문
# cnt = 0
# i = 0
# while i < len(st):
#     if st[i] != ' ':
#         cnt += 1
#     i += 1
# print("{}개".format(cnt))



#3)내장함수
sp = st.count(' ')
print("{}개".format(len(st) - sp))
