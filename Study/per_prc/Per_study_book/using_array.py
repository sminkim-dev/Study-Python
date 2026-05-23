# 배열 이용

print("리스트 이용")
people = int(input("인원 수를 입력 >> "))
nameList = []
scoreList = []
for i in range(people):
    name = input("이름 : ")
    score = int(input("점수 : "))
    nameList.append(name)
    scoreList.append(score)
find_name = input("찾으시는 이름을 입력하십시오 >> ")
found = bool(False)
for ixd , name in enumerate(nameList):
    if(find_name == name):
        print("이름 : {} 성적 : {} \n".format(nameList[ixd], scoreList[ixd]))
        found = True
if(found == False):
    print("찾으시는 이름이 존재하지 않습니다.")