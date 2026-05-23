result = ""
for num in range(1, 101):
    result += str(num)
    if num % 3 == 0:
        result += " 짝"
    result += "\n"
print(result)