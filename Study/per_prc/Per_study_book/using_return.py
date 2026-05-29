def return_test():
    return
value = return_test()
print(value)


ranges = [(0,50),(0,1000),(50,100),(500,1000)]
def cal(start_num, end_num):
    output = 0
    for i in range(start_num, end_num + 1):
        output += i
    return output

for start_ , end_ in ranges:
    label = f"{start_} to {end_}"
    result = cal(start_,end_)
    binary_nums = "{:b}".format(result)
    hex_nums = "{:x}".format(result)
    print(f"{label:<15} : {result:>10,} : {binary_nums:<25} : {hex_nums:>10}")