text = [int(x) for x in input("정수 입력 >> ").split()]
F_list = text[:]
S_list = text[:]
up_arr = []
down_arr = []

def Up():
    for i in range(len(F_list)):
        max_value = -float('inf')
        for a in F_list:
            if a > max_value:
                max_value = a
        up_arr.append(max_value)
        F_list.remove(max_value)
def Down():
    for i in range(len(S_list)):
        min_value = float('inf')
        for b in S_list:
            if b < min_value:
                min_value = b
        down_arr.append(min_value)
        S_list.remove(min_value)
Up()
Down()
print("Max Value : " , up_arr[0])
print("Up-arr-setting : " , up_arr)
print("Min Value : " , down_arr[0])
print("Down-arr-setting : " , down_arr)