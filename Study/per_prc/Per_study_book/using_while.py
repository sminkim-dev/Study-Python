limit = 10000
i = 1
sum = 0
while (True):
    sum += i
    if(sum < 10000):
        i += 1
    else:
        break
print("{}을 더할 때 {}을 넘으면 그 때의 값은 {}입니다.".format(i, limit, sum))