year = input("연도 입력 >> ")
result = ""
if year[-1] == '0' or year[-1] == '5':
    result += "월요일"
elif year[-1] == '1' or year[-1] == '6':
    result += "화요일"
elif year[-1] == '2' or year[-1] == '7':
    result += "수요일"
elif year[-1] == '3' or year[-1] == '8':
    result += "목요일"
elif year[-1] == '4' or year[-1] == '9':
    result += "금요일"
result += "에 접종가능합니다."
print(result)