def num_sum(x , y):
    sum = x + y
    return sum
def show(sum, result_value):
    ans = "정답입니다." if result_value == sum else "틀렸습니다."
    print(ans)
x = int(input("첫번째 정수 입력 >> "))
y = int(input("두번째 정수 입력 >> "))
problem = f"정수 {x} + {y} 의 합은? "
sum = num_sum(x,y)
result_value = int(input(f"정수 {x} + {y} 의 합은? "))
show(sum, result_value)