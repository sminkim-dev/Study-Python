import time
import sys
sys.set_int_max_str_digits(100000)
# 효율성 개선 전
""" def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# want layer index value write value of integer
target_layer = int(input("target_layer >> "))
for i in range(target_layer):
    print(f"fibonacci({i + 1}) : ", fibonacci(i + 1)) """
# 효율성 개선
def fibonacci_loop(n):
    start_time = time.perf_counter()
    a, b = 1, 1 # 교재 기준 시작
    for _ in range(n - 1):
        a, b = b, a + b
    end_time = time.perf_counter()
    fin_time = end_time - start_time
    print("소요 시간 : {:.4f}".format(fin_time))
    return a

target = 100
print(f"fibonacci({target}) 결과 계산 완료")
print(fibonacci_loop(target))