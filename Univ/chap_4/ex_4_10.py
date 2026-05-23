import random

r_num = [0,1,2,3,4,5,6,7,8,9]
r_alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
choice_num = random.choice(r_num)
choice_alp1 = random.choice(r_alp)
choice_alp2 = random.choice(r_alp)

securityPassword = f"{choice_num}{choice_alp1}{choice_alp2}"
print(f"생성된 패스워드 : {securityPassword}")