import random

def ran():
    num = random.randint(1,9)
    return num

n1 = ran()
n2 = ran()    
result = n1 * n2
while(True):
    problem = f"{n1} X {n2} = "
    in_value = int(input(f"{problem}"))
    if result == in_value:
        break
print("맞았습니다.")