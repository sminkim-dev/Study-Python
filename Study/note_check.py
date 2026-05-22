# 알고리즘 이해 노트
memo = {}
min_n = 2
max_n = 10
total_n = 100

def problems(remain,min_n):
    key = (remain,min_n)
    if key in memo:
        return memo[key]
    
    if remain == 0:
        return 1

    count = 0
    start = min_n
    end = min(max_n,remain)

    for i in range(start,end+1):
        count += problems(remain - i , i)
    return count
print("전체 사람 수 : {}명을 {} ~ {}명씩 앉히는 패턴의 수 : {}".format(total_n,min_n,max_n,problems(total_n,min_n)))