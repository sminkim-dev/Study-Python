data = {"principal" : 1000 , "year" : 1}

def update():
    data["principal"] *= 1.07
    print(f"{data['year']}년 후 {data['principal']}가 되었습니다.")
    data["year"] += 1
while(True):
    if  data["principal"] > 2000:
        data["year"] -= 1
        break
    else:
        update()
print(f"{data['year']}년이 걸렸습니다.")