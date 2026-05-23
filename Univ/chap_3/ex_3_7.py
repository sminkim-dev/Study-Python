number = int(input("정수를 입력하시오 > "))
roop = bool(True)
copyNum = number
total_sum = 0
while(roop):
    if(copyNum > 0):
        sum += copyNum % 10
        copyNum //= 10
    else:
        break
print(number , "의 각 자리 수의 합은 " , int(total_sum) , "입니다.")