import random
import secrets

Attack = ["가위", "바위", "보"]
u_atk = input("가위, 바위, 보 중에 입력하세요 >> ").strip()

""" for i in range(len(u_atk)):
    if Attack[i] == u_atk:
        user_atk_num = i """
try:
    user_atk_num = Attack.index(u_atk) #list.index(찾을 값, 시작 위치, 끝 위치)

    #ai_atk_num = random.randint(0, 2)
    #ai_atk_num = random.randrange(3)
    ai_atk_num = secrets.randbelow(3) # randrange는 의사난수라서 패턴 파악 가능. 이게 더 보안상 좋음.
    print(f"AI atk : {Attack[ai_atk_num]}")
    results = (user_atk_num - ai_atk_num) % 3 #순환 만들기, 0 비김 1 이김 2 짐
    result = ["비겼습니다.", "이겼습니다.", "졌습니다."]
    print(f"{result[results]}")
except ValueError:
    print("잘못된 입력입니다. \n가위, 바위, 보 중에서만 입력하세요.")