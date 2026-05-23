weight = int(input("물체의 무게를 입력하시오 (단위 : kg) > "))
speed = int(input("물체의 속도를 입력하시오 (단위 : m/s) > "))

cal_energy = 0.5 * weight * speed**2
print(f"물체는 {cal_energy:.2f}줄의 에너지를 가지고 있다.\n")