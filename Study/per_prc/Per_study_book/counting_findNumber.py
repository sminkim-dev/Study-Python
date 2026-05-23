import random
numbers = []
for i in range(15):
    numbers.append(random.randint(0,9))
counter = {}
print("생성된 숫자들 " , numbers)
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(f"실행 결과 : {dict(sorted(counter.items()))}")