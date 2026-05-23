def manual_big_add(num1_str, num2_str):
    # 1. 각 숫자를 뒤집어서 리스트로 만듦 (일의 자리부터 인덱스 0에 오도록)
    # 예: "123" -> [3, 2, 1]
    list1 = [int(d) for d in reversed(num1_str)]
    list2 = [int(d) for d in reversed(num2_str)]
    
    result = []
    carry = 0  # 받아올림 변수
    
    # 두 리스트 중 더 긴 것의 길이를 구함
    max_len = max(len(list1), len(list2))
    
    # 2. 낮은 자릿수부터 하나씩 더하기 시작
    for i in range(max_len):
        # 해당 자릿수에 숫자가 없으면 0으로 취급
        d1 = list1[i] if i < len(list1) else 0
        d2 = list2[i] if i < len(list2) else 0
        
        # 합계 = 첫 번째 숫자 + 두 번째 숫자 + 이전 자릿수에서 올라온 값
        total = d1 + d2 + carry
        
        # 현재 자릿수에 남을 값 (10으로 나눈 나머지)
        result.append(total % 10)
        
        # 다음 자릿수로 보낼 받아올림 값 (10으로 나눈 몫)
        carry = total // 10
        
    # 3. 모든 계산이 끝났는데 마지막 받아올림이 남아있다면 추가
    if carry:
        result.append(carry)
        
    # 4. 리스트를 다시 뒤집어서 문자열로 합침
    return "".join(map(str, reversed(result)))

# --- 테스트 실행 ---
n1 = "99999999999999999999" # 아주 큰 수
n2 = "1"
print(f"결과: {manual_big_add(n1, n2)}")