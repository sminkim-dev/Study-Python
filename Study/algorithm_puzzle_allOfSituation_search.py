# 앉힐 수 있는 최소 사람 수 : 2
# 앉힐 수 있는 최대 사람 수 : 10
# 전체 사람의 수 : 100

# 설정값
memo = {}
min_n = 2
max_n = 10
total_n = 100
# 재귀 함수 부분 (남은 사람 수, 최소 앉을 수 있는 사람 수)
def problems(remain_people, min_sitting):
    # 1. 메모이제이션 확인
    key = (remain_people, min_sitting)
    if key in memo:
        return memo[key]
    
    # 2. 종료 조건 (Base Case)
    if remain_people == 0:
        return 1  # 정확히 0명이 남으면 하나의 완성된 패턴으로 인정
    
    count = 0
    
    # 3. 재귀 호출 (Recursive Step)
    # 현재 테이블에 앉힐 수 있는 범위: 
    # (이전 테이블 인원수 이상) ~ (설정된 최대 인원수 및 남은 인원수 중 작은 값)
    start = min_sitting
    end = min(max_n, remain_people)
    
    for i in range(start, end + 1):
        count += problems(remain_people - i, i)
        
    # 결과 저장 및 반환
    memo[key] = count
    return count

# 결과 출력
result = problems(total_n, min_n)
print(f"전체 사람 수 {total_n}명을 {min_n}~{max_n}명씩 앉히는 패턴의 수: {result}")