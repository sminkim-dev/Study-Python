max_value = -float('inf')
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i

    result = i * j
    if(max_value < result):
        max_value = result
        a = i
        b = j
print("최대가 되는 경우 : {} * {} = {}".format(a,b,a*b))