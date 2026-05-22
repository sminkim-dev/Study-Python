def f(x):
    return 2*x + 1
def g(x):
    return x**2 + 2*x + 1

print(f(10))
print(g(10))

# 가변 매개변수를 이용하여 전달된 값을 모두 곱한 값을 반환하는 코드 작성
def mul(*values):
    value = 1
    for i in values:
        value *= i
    return value
print(mul(5,7,9,10))

# available factorial method
def fac(number):
    result = 1
    for i in range(1,number + 1):
        result *= i
    return result
number = 5
print(f"The factorial value of the value {number} is {fac(number)}")

# Code that outputs all factorials up to the integer
target_num = int(input("input interger >> "))
for index in range(target_num):
    first_str = f"{index + 1}!"
    result = fac(index + 1)
    print(f"{first_str:<3} : {result}")