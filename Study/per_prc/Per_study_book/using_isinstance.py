character = {
    "name":"기사",
    "level" : 12,
    "items":{
        "sword" : "불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기", "세게 베기", "아주 세게 베기"]
}

print("출력 연습")
for key in character:
    v = character[key]
    if isinstance(v,list):
        for item in v:
            print(f"{key} : {item}")
    elif isinstance(v, dict):
        for k2 , v2 in v.items():
            print(f"{k2} : {v2}")
    elif isinstance(v, str):
            print(f"{v} : {v}")