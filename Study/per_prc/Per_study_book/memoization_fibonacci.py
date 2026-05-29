import time
import sys
# import sys를 하는 이유 : python 자체에서 코드 안전성을 위해서 제한을 걸어놓기 때문, 재귀 깊이 제한은 1000, 문자열은 print문은 보통 4300자까지만 허용
# 때문에 sys로 python에서 걸어놓은 limit의 제한을 푸는 것, 단 하드웨어의 성능이 따라준다면 해당 방식을 해도되지만, 권장은 아님.
# 왜냐, 가능하면 for 반복문을 이용하면, 길이가 1000이든 100000이든 가능하기 때문.
sys.set_int_max_str_digits(100000)
sys.setrecursionlimit(10000)
dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        # 바로 아래 에러 걸림, 
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

target = 20
start_time = time.time()
print("fibonacci({}) : {}".format(target,fibonacci(target)))
end_time = time.time()
execution_time = end_time - start_time
print(dictionary)
print("걸린 시간은 {:.4f}초입니다.".format(execution_time))