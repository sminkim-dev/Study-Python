# 숫자 n을 입력 받아서 3-6-9게임의 박수 순열(sequence)를 출력하라
def sequence(n):
    count = 0
    for i in range(1,n+1):
        s = str(i)
        if (('3' in s) or ('6' in s) or ('9' in s)):
            clap = s.count('3') + s.count('6') + s.count('9')
            print("짝" * clap, end=" ")
        else:
            print("{} ".format(i),end="")

num = int(input(">>> "))
sequence(num)
        