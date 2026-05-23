# 1번 스크립트 모드로 출력 (스킵)
# 2번 print 출력 결과 스킵

# 3번 원주율 3.14로 원 면적 구하기
radius = float(input("반지름 입력 >> "))
Pi = 3.14

result = pow(radius,2) * Pi
#result = radius**2 * Pi
print(f"해당 반지름의 면적은 {result}입니다.")