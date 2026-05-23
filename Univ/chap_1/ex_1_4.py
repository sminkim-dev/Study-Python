# 거북이 이동 시키는 코드. (4, 5, 6, 7번 같이 풀이하겠음.)
# 4번은 기본 이동시키는 코드
# 5번은 width() 함수를 이용해 굵기 변경
# 6번은 color() 함수를 이용해 색상 변경
# 7번은 shape() 를 이용해 모양 변경

import turtle as t # turtle 이라는 라이브러리를 t라는 짧은 이름으로 불러옴

t.shape("turtle") # 7번에 해당
#거북이 속도 설정
t.speed(3)

#그림의 길이에 맞춰 이동 길이 설정
horizontal_length = 150
vertical_length = 100

#거북이는 처음에는 오른쪽 0도를 바라보고 있음.

# 1. 첫번째 가로선 그리기
t.forward(horizontal_length)

# 2. 위로 꺾기
t.left(90)
t.forward(vertical_length)

# 3. 다시 오른쪽으로 꺾기
t.right(90)
t.forward(horizontal_length)

# 4. 아래로 꺾기
t.right(90)
t.forward(vertical_length)

# 5. 마지막 가로선 그리기
t.left(90)
t.color("red") # 6번 충족시키기
t.forward(horizontal_length)
t.width(10) # 5번 충족시키기


# 끝날 때까지 거북이 모양을 유지하면서 창을 닫지 않음.
t.done()