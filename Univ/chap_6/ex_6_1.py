result = ""
for i in range(1, 101, 1):
    if i % 2 == 0:
        result += f"{i}  "
    if i % 10 == 0:
        result += "\n"
print(result)