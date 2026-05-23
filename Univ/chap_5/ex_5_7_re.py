nums = [int(x) for x in input("정수 입력 >> ").split()]

u_list = sorted(nums)
d_list = u_list[::-1]

print(f"Input Array List : {nums}")
print(f"Up List : {u_list} , Down List : {d_list}")
print(f"Max : {d_list[0]} , Min : {u_list[0]}")