#9 번 문제 turtle 안 씀.

height = int(input("키를 입력하시오 (단위 : cm) >> "))
weight = int(input("몸무게를 입력하시오 (단위 : kg) >> "))

def bmi_cal(heigt, weight):
    bmi = float(weight / ((height*0.01)*(height*0.01)))
    return bmi
bmi = bmi_cal(height, weight)
if bmi >= 25:
    result = "과체중입니다."
elif bmi >= 18.5 and bmi <= 24.9:
    result = "적정체중입니다."
elif bmi <= 18.4:
    result = "저체중입니다."
print(f"당신의 bmi : {bmi}")
print(result)