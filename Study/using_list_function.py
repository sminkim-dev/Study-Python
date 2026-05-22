import random

numbers = [103, 52, 273, 32, 77]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# reverse list
reverse_list = list(reversed(numbers))
print(reverse_list)

temp = [1,2,3,4,5]

for i in reversed(temp):
    print("첫번째 반복 {}".format(i))
print(temp)
print(temp[::-1])

example_list = ["A", "B", "C"]
for i in range(len(example_list)):
    print("{}번째 요소는 요소{}입니다.".format(i,example_list[i]))

print(example_list)
print("enumerate() : ",list(enumerate(example_list)))
for idx, value in enumerate(example_list):
    print("{}번째 인덱스 값 : {}입니다.".format(idx,value))

example_dictinary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"
}

# 딕셔너리 items()함수를 이용하여 출력
print("item() : ",example_dictinary.items())
# 반복문 + items() 함수 활용
for key, value in example_dictinary.items():
    print("dictionary[{}] = {}".format(key, value))

# 기존 특정 배수 반복문 구현
array = []
for i in range(0,20,2):
    array.append(i*i)
print(array)
# 리스트 안에 for문 작성한 코드
second_array = [i * i for i in range(0,20,2)]
print(second_array)
# 리스트 반복문 활용 예시 2가지
random_array = [random.randint(0,100) for _ in range(10)]
print(random_array)
offset = 10
dynamic_array = [i + offset for i in range(5)] # 외부 변수 반영
print(dynamic_array)

# 조건을 활용한 리스트
first_array = ["사과","자두","초콜릿","바나나","체리"]
output_array = [fruit for fruit in first_array if fruit != "초콜릿"]
print(output_array)