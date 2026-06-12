class Silver:
    def __init__(self, name , rate):
        self.name = name
        self.rate = rate
        self.point = 0
    def setMoney(self, money):
        self.point += (money)*(self.rate/100)
    def totalPoint(self):
        return self.point
    def toString(self):
        #return "{}의 포인트 적립률 : {:.1f}".format(self.name, self.totalPoint())
        return f"{self.name}의 포인터 적립률 : {self.totalPoint():.1f}"
class Gold(Silver):
    def __init__(self, name, rate):
        super().__init__(name, rate)

def cal(s, g):
    if s == 0:
        return 0
    return ((g - s) / s) * 100
print("Silver and Gold membership diffrent Accumulation rate")
print("Silver = 3% , Gold = 5%")
print("3time accumulate some money")
s = Silver("Silver", 3)
g = Gold("Gold", 5)
for i in range(3):
    s.setMoney(int(input("Silver input : ")))
for i in range(3):
    g.setMoney(int(input("Gold input : ")))
print(s.toString())
print(g.toString())
print(f"Gold Membership Silver Membership 보다 {cal(s.totalPoint(), g.totalPoint()):.1f}")
#print("Gold membership이 Silver membership 보다 {:.1f}% 정도 더 적립률이 높다.".format(cal(s.totalPoint(), g.totalPoint())))
