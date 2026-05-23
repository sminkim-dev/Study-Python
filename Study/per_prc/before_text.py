numbers = [273 , 103, 5, 32, 65, 9, 72, 800, 99]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print("{} 은 짝수이고 {}자릿수입니다.".format(numbers[i], len(str(numbers[i]))))
    else:
        print("{} 은 홀수이고 {}자릿수입니다.".format(numbers[i], len(str(numbers[i]))))
