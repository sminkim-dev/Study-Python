nums_array = []
for_times = int(input("몇 개의 정수를 입력하시겠습니까?"))
for i in range(for_times):
    nums_array.append(int(input("정수를 입력 >> ")))
for nums in nums_array:
    if nums % 2 == 0:
        print(nums , "짝수입니다.")
    else:
        print(nums , "홀수입니다.")
        