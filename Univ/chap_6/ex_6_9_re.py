import itertools
import string

target = input("입력 >> ")
alphabet = string.ascii_lowercase
digit = string.digits

chars = [alphabet , alphabet , alphabet , digit , digit]
all_combination = itertools.product(*chars)

for combo in all_combination:
    guess = "".join(combo)
    print(guess)
    if guess == target: break

print(f"패스워드 => {guess}")