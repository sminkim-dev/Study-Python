import time

counter = 0
def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1

    # cal fibonacci
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
target_num = int(input("target number >> "))
start_time = time.time()
fibonacci(target_num)
end_time = time.time()
execution_time = end_time - start_time

print("----------")
print("fibonacci({}) 계산에 활용된 덧셈 횟수는 {}번이고 소요시간은 {:.4f}초입니다.".format(target_num,counter,execution_time))