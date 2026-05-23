interestRate = int(input("이자율 단위 : %) : "))
principal = int(input("원금 (단위 : 만원) : "))
period = int(input("거치 기간 (단위 : 년) : "))

def cal(interestRate , principal , period):
    principal = principal*10**4
    increase = 0
    for i in range(period):
        principal = (principal * 1.05)

    print(period , "년 후의 원리금은 " , round(principal) , " 원입니다.\n")
cal(interestRate , principal , period)