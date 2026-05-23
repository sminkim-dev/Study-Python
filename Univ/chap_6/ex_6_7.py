import random

def ran():
    num = random.randint(1,6)
    return num

for nums in range(1,4):
    print(f"첫번째 주사위는 : {ran()} , 두번째 주사위는 : {ran()}")