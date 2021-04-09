# 연습
# 1. 인수형태를 정수형태로 시작값(start), 끝값(end)을 전달받아
#    반복문으로 start부터 end까지의 누적 총합을 구하는 함수를
#    정의하세요.
# 2. 함수이름은 calc_rangesum로 정의하세요.
# ex) calc_rangesum(3,7) ==> 3부터 7까지의 누적합을 구해와햐 함.


def cal_rangesum(start, end):
    sum = 0
    for num in range (start, end + 1):
         sum += num
    
    return sum

result = cal_rangesum(3, 7)
print("4부터 6까지의 누적합계 : ", result)

result = cal_rangesum(6, 9)
print("6부터 9까지의 누적 합계 : ", result)
