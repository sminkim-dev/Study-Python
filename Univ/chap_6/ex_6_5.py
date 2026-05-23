import random
data = {"count" : 1 , "corrct" : 0}

def ran():
    num = random.randint(1,9)
    return num
print("---------------random 구구단 프로그램 ---------------")
while(True):
    if data["count"] == 4:
        break
    r_num1 = ran()
    r_num2 = ran()
    result = r_num1 * r_num2
    problem = f"{r_num1} X {r_num2} = "
    in_value = int(input(f"{problem}"))
    if in_value == result:
        print("정답입니다.")
        data["corrct"] += 1
    else:
        print(f"{data['count']}번 틀렸습니다. {data['corrct']}번 맞췄습니다.")
        data["count"] += 1
print("프로그램 종료합니다.")
print("------------------------------------------------------")
