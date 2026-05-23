data = {"sum" : 0}
in_arr = []
while(True):
    num = int(input("정수를 입력하시오 >> "))
    if num == 0:
        break
    else:
        in_arr.append(num)
        data["sum"] += num
print(f"입력된 정수들은 : {in_arr}입니다.")
print(f"정수들의 합은 {data['sum']}입니다.")