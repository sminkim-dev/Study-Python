# 10진수와 2진수의 변환
print("{:b}".format(10))
binary_num = int("1010",2)
print(binary_num)

# 10진수와 8진수의 변환
eight_num = "{:o}".format(10)
print(eight_num)
print(int("12",8))

# 10진수와 16진수 변환
print("{:x}".format(10))
print(int("10", 16))

# count()함수 예시
print("안녕안녕하세요".count("안"))

# 리스트 내포를 사용해본 코드
output = [1,5,7,9,12,22,66,77,88,95]
# convert binary numbers
sum = 0
for i in output:
    print("{} : {:b}".format(i, i))
    sum += i
print("합계 : {}".format(sum))