import random

number = [int(x) for x in (input("Lotto 번호 입력 ex(5 8) >> ").split())]

lotto = random.sample(range(10) , 2)
print(f"당첨 번호 : {lotto}")
if number[0] in lotto and number[1] in lotto:
    print("100만원 당첨")
elif number[0] in lotto or number[1] in lotto:
    print("50만원 당첨")
else:
    print("미당첨")
