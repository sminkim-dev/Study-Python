dictionary = {"name" : "7D 건조 망고",
              "type" : "당절임",
              "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
              "origin" : "필리핀"}

for k, v in dictionary.items(): # items()은 리스트나 배열의 enumertate와 기능이 동일. 값이랑 인덱스를 둘 다 가져오고 싶을 때 사용
    if isinstance(v, list): #if isinstance 자료형을 확인하는 검문소 역할 > list가 맞으면 true 아니면 false 반환
        print(f"{k} : ")
        for item in v:
            print(f"- {item}")
    else:
        print(f"{k} : {v}")

    