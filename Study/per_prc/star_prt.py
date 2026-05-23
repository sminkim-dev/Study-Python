# 역 피라미드 별 찍기. 옛날 기출.

n = int(input("Row 값을 입력하시오 >> "))

for i in range(n, 0, -1):  # 5, 4, 3, 2, 1 순서로 반복
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)