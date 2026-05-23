import time

total_second = int(time.time() + 3600 * 9)

total_minute = total_second // 60
total_hour = total_second // 60**2

current_second = total_second % 60
current_minute = total_minute % 60
curremt_hour = total_hour % 24

print(f"현재 시간(영국 그리니치 시각) > {curremt_hour}시 {current_minute}분 {current_second}초\n")