import time

start_time = time.time()
input("30초 인 것 같으면 누르십시오.")
end_time = time.time()

result = end_time - start_time
gap = result - 30
print(f"{result:.2f}초 지났습니다.")
if gap == 0:
    print("30초에 딱 맞췄습니다.")
elif gap > 0:
    print(f"{abs(gap):.2f}초 늦었습니다.")
else:
    print(f"{abs(gap):.2f}초 빨랐습니다.")