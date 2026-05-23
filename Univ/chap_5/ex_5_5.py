import random
#global check
check = 0
while(True):
    num1 = random.randint(1 , 100)
    num2 = random.randint(1 , 100)
    sub_result = num1 - num2
    problem = f"{num1} - {num2} = "
    value = int(input(f"{problem}"))
    if value == sub_result:
        print("정답입니다.\n")
        continue
    else:
        check += 1
        print(check ,"틀렸습니다.\n")
        if check == 3:
            print("프로그램을 종료합니다.")
            break