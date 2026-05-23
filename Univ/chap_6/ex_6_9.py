import string

# 1. 대상 패스워드 설정 (사용자 입력)
target = input("패스워드를 입력하시오: ")

# 알파벳 소문자(a-z)와 숫자(0-9) 리스트 준비
alphabet = string.ascii_lowercase  # 'abcdef...xyz'
digits = "0123456789"

found = False

# 2. 5중 반복문으로 모든 조합 생성 (알파벳 3개 + 숫자 2개)
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in digits:
                for e in digits:
                    # 현재 시도할 조합 생성
                    guess = a + b + c + d + e
                    print(guess) # 현재 시도 중인 패스워드 출력
                    
                    # 3. 정답 확인
                    if guess == target:
                        print(f"\n패스워드 발견: {guess}")
                        found = True
                        break
                if found: break
            if found: break
        if found: break
    if found: break