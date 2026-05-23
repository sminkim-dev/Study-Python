input_num = int(input("정수 하나를 입력 >> "))

# % 연산자를 이용한 방법
""" 
if input_num % 2 == 0:
    print("{}은 짝수입니다.".format(input_num))
else:
    print("{}은 홀수입니다.".format(input_num)) """

# 마지막 자릿수를 이용하여 대조하여 찾는 방법

""" last_number = input_num[-1]

if last_number in "02468":
    print("짝수입니다.")
elif last_number in "13679":
    print("홀수입니다.") """

for i in range(1,input_num + 1):
    if i % 2 == 0:
        print("{} even number".format(i))
    elif i % 2 != 0:
        print("{} odd number".format(i))
print("end")