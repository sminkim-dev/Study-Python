nameList = []

while(True):
    nums = (input("입력 >> '그만' 입력시 종료"))
    if nums == "그만":
        break
    nameList.append(nums)
while(True):
    delName = (input("리스트에서 빼고 싶은 데이터 입력 >> "))
    if(delName == "stop"):
        break
    check = bool(False)
    for idx, name in enumerate(nameList):
        if(name == delName):
            nameList.remove(nameList[idx])
            check = True
    if check == False:
        print("해당 데이터 '{}'는 리스트에 존재하지 않습니다.".format(delName))
    print("현재 리스트에 남은 데이터들의 리스트를 출력합니다.")
    print(nameList)
print("종료합니다.")