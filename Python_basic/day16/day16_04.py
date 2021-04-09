# Quiz)

# 길이를 반환하는 함수 : len(x) 와 동일한 기능 구현해보기!

lt = ["a", "b", "c", 4]
tu = (1,2,3, "d", "e")
dic = {"a" : 1, "b" : 2}
st = "python"

print(len(lt), len(tu), len(dic), len(st), sep= ", ")

def copy_len(x):
    strlen = 0
    for i in x:
        strlen += 1
    return strlen

print(copy_len(lt), copy_len(tu), copy_len(dic), copy_len(st), sep=', ')

# 22_12) 매개변수에 초기값을 미리 지정(디폴트 매개변수)
def say_myself(name = "이름", age = 1, gender =True):
    print("이름 : {}입니다.".format(name))
    print(f"나이 : {age}")
    if gender:
        print("남자")
    else:
        print("여자")

say_myself("최강", 29, "남자")
say_myself("chlrkd", 29)
say_myself()

