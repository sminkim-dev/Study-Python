amountOfFuelRefueled = float(input("주유한 연료의 양(단위 : 리터) : "))
mileage = float(input("주행한 거리 (km) : "))
fuelEfficiency = mileage / amountOfFuelRefueled
print("자동차의 연비는 " , fuelEfficiency , "km / 리터 입니다.")