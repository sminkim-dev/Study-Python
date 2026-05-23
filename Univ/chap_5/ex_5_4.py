score = int(input("성적 입력 >> "))
result = ""
if(score >= 90):
    result += "A"
elif(score >= 80 and 90 > score):
    result += "B"
elif(score >= 70 and 80 > score):
    result += "C"
else:
    result += "F"
result += "학점 입니다."
print(result)