""" num1 = int(input("정수를 입력하여주십시오 > "))
num2 = int(input("정수를 입력하여주십시오 > "))
num3 = int(input("정수를 입력하여주십시오 > ")) """

""" nums_arr = []
nums_arr.append(num1)
nums_arr.append(num2)
nums_arr.append(num3)
print("리스트 : " , nums_arr)
sum = nums_arr[0] + nums_arr[1] + nums_arr[2]
print("리스트 숫자들의 합 : " , sum) """

nums_arr = []
sum = 0
for i in range(3):
    num = int(input("정수를 입력하여주십시오 > "))
    nums_arr.append(num)
    sum += int(nums_arr[i])
print("리스트 : ", nums_arr)
print("리스트들의 합 : " , sum)