import datetime

now = datetime.datetime.now()

#print
attiributes = ["year", "month", "day", "hour", "minute", "second"]
units = ["년", "월", "일", "시", "분", "초"]

for i in range(len(attiributes)):
    value = getattr(now, attiributes[i])
    print(f"{value}{units[i]}", end=" ")

if now.hour < 12:
    print("\n현재 시각은 {}시로 오전입니다!".format(now.hour))
if now.hour >= 12:
    print("\n현재 시각은 {}시로 오후입니다!".format(now.hour))
