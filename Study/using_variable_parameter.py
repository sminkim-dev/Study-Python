# example variable parameter
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "hello","enjoy", "Python programming")

# 기본 매개변수는 가변 매개변수 앞에 쓰면 X
# 가변 매개변수 뒤에 기본 매개변수를 쓸 경우에는 키워드 매개변수를 활용함. 아래 함수 호출문부분에서 n = 3에 해당함
def print_n_times(*values, n = 2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("hi","name", "programming", n = 4)

def test(a, b = 10, c = 100):
    print(a + b + c)
# 기본 형태 basic form 
test(10,20,30)
# 키워드 매개변수로 모든 매개변수를 지정한 형태 A form where all parameters are specified using keyword parameters.
test(a = 10, b = 100, c= 200)
# 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태 A form where all parameters are haphazardly specified using keyword parameters.
test(c= 10, a = 100, b = 200)
# 키워드 매개변수로 일부 매개변수만 지정한 형태 A form where only some parameters are specified using keyword parameters
test(10, c = 200)
