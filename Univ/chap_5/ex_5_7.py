num1 = int(input("첫번째 숫자 >> "))
num2 = int(input("두번째 숫자 >> "))
num3 = int(input("세번째 숫자 >> "))

num_arr = [num1, num2, num3]
flist = num_arr[:]
alist = num_arr[:]
u_list = []
d_list = []
for a in range(len(flist)):
    max = -float('inf')
    for i in flist:
        if max < i:
            max = i
    d_list.append(max)
    flist.remove(max)
for a in range(len(alist)):
    min = float('inf')
    for b in alist:
        if b < min:
            min = b
    u_list.append(min)
    alist.remove(min)
print(f"List : {num_arr} , 오름차순 : {u_list} , 내림차순 : {d_list}\n")
print(f"Max : {d_list[0]}, Min : {u_list[0]}")