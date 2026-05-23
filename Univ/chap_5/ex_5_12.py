import random

at_list = ["가위", "바위", "보"]
Attack = input("가위, 바위, 보 중 하나 입력 > ")

# 1. 입력값 검증: 리스트에 없는 걸 입력하면 바로 종료
if Attack not in at_list:
    print("잘못된 입력입니다. 다시 실행하세요.")
else:
    # 2. 인덱스 찾기 (for문 대신 .index()를 쓰면 한 줄로 끝납니다!)
    at_trans_num = at_list.index(Attack)

    # 3. 컴퓨터 공격 (0~2 사이의 정수 하나)
    r_Attack = random.randint(0, 2)
    print(f"컴퓨터: {at_list[r_Attack]}")

    # 4. 결과 판정
    if at_trans_num == r_Attack:
        result = "비겼습니다."
    elif (at_trans_num == 0 and r_Attack == 2) or \
         (at_trans_num == 1 and r_Attack == 0) or \
         (at_trans_num == 2 and r_Attack == 1):
        result = "이겼습니다!"
    else:
        result = "졌습니다..."
        
    print(result)