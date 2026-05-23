number = int(input("정수 입력 >> "))

result = "2와 3으로 나누어짐" if number % 2 == 0 and number % 3 == 0 else "2와 3으로 안 나누어짐"
print(result)