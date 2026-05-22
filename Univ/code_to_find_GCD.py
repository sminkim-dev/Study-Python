# 숫자 2개를 입력받고, 두 수의 공약수를 구하기
def common_divisor(num1,num2):
    limit = min(num1,num2)
    for i in range(limit,0,-1):
        if num1 % i == 0 and num2 % i == 0:
            return i

while(True):
    line = [int(x) for x in input(">>> ").split()]
    if line[1] == 0 or line[0] == 0:
        print("program exit")
        break
    print("common divisor : ",common_divisor(line[0],line[1]))
