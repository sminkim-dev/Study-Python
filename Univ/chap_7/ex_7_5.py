data = {"factorial" : 1}
fac = int(input("정수 입력 >> "))

def factorial(fac):
    for i in range (1, fac + 1):
        data["factorial"] *= i
    return
factorial(fac)
print(f"{fac}! 은 {data['factorial']}입니다.")
