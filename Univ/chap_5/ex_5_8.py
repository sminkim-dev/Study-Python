puppy_age = int(input("강아지의 나이 입력 >> "))
# 처음 2년동안은 사람의 10년, 이후 강아지의 1년은 사람의 4년에 해당함.
def pupIntoHuAge(age):
    trasAge = 0
    for i in range(1, age + 1):
        if i > 2:
            trasAge += 4
        elif 1 <= i and i <= 2:
            trasAge += 10
    print(f"강아지의 나이를 사람 나이로 환산하면 {trasAge}살입니다.")
pupIntoHuAge(puppy_age)