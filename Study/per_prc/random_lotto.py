import random

while(True):
    try:
        #입력 받기
        user_input = input("복권 두 자리 수를 입력하시오. 0~9, ex : 7 8 >> ").split()
        
        #길이 확인
        if len(user_input) != 2:
            print("반드시 2개의 숫자만 입력해야합니다.")
            continue
        n1, n2 = map(int, user_input)

        #예외 처리 (범위 체크)
        if not 0 <= n1 <= 9 and 0 <= n2 <= 9:
            print("숫자는 0~9만 입력가능합니다.")
            continue
        #랜덤 수 외 입력값 중복 처리
        if n1 == n2:
            print("서로 다른 숫자를 입력해야 합니다.")
            continue
        #위 조건문을 전부 통과하면 break로 아래 메인으로 내려감. 아닐 경우 except으로 던져짐.
        break
    except ValueError:
        print("Error : 숫자만 입력가능합니다. 다시 시도하세요.")

lotto = random.sample(range(10),2)
print(f"당첨 번호는 : {lotto}")

user_nums = [n1,n2]
match_count = 0

for num in user_nums:
    if num in lotto:
        match_count += 1

if match_count == 2:
    print("당첨 금액은 100만원입니다.")
elif match_count == 1:
    print("당첨 금액은 50만원입니다.")
else:
    print("당첨되지 않았습니다.")