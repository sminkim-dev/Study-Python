import datetime

now = datetime.datetime.now()

# 기본 시간 전체 출력
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

# 현재 시간 불러와 오전/오후 구분 후 출력
""" trans_hour = now.hour - 12
if(now.hour > 12):
    print("오후 {}시 {}분입니다.".format(trans_hour,now.minute))
elif(now.hour < 12):
    print("오전 {}시 {}분입니다.".format(trans_hour,now.minute)) """

# 현재 월(month)을 불러와 조건문으로 현재 월 기준 어떤 계졀인지 출력
month = now.month
if 3 <= month and month <= 5:
    print("{}월은 봄입니다.".format(month))
elif 6 <= month <= 8:
    print("{}월은 여름입니다.")
elif 9 <= month <= 11:
    print("{}월은 가을입니다.")
elif month == 12 or 1 <= month and month <= 2:
    print("{}월은 겨울입니다.".format(month))

