list_of_list = [ [1,2,3], [4,5], [6,7,8,9]]

for i in range(len(list_of_list)):
    for b in range(len(list_of_list[i])):
        print(list_of_list[i][b])

numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    # output을 보면 배열 크기와 안에 들어갈 원소 집합개수도 정해놓았기에. 아래 코드에서 인덱스 0,1,2값만 정해주면 같은 인덱스 끼리 자동으로 묶임.
    output[(number - 1) // 3].append(number) # ex) 1,2,3 -> index (0) 4,5,6 -> index(1) 7,8,9 index(3) 
print(output)