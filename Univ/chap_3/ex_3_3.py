# 1명이 하루에 2명씩 감염 가능.
infectionIndex = int(input("감염 지수 : "))
day = int(input("일수 : "))

def cal(infectionIndex , day):
    value = pow(infectionIndex,day)
    return value
print(day , "일 후에 예상 감염자는 " , cal(infectionIndex,day) , "명 입니다.")