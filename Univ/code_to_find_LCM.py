# 두 수를 입력받고 최소 공배수(least common multiple)를 구하는 프로그램
def cal_LCM(num1,num2):
    # 우선 GCD 을 구해야 함. 이유 a x b = GCD x LCM 이기 떄문임
    limit = min(num1,num2)
    for i in range(limit,0,-1):
        if num1 % i == 0 and num2 % i == 0:
            value_GCD = i
            break
    value_lcm = (num1 * num2) // i
    return value_lcm

while(True):
    # List Comprehension (리스트 컴프리헨션)
    # 문자열 line을 split()으로 나눠서 x 라는 변수에 담고 해당 변수는 int(x)를 통해 문자열에서 정수로 변환되서 리스트에 저장되는 방식
    line = [int(x) for x in input(">>> ").split()]
    if line[0] == 0 or line[1] == 0:
        print("program exit")
        break
    print("least common multiple : ",cal_LCM(line[0],line[1]))