# 반지름 100인 오륜기 그리기 코드 구현
import turtle as t

radius = 100
t.shape("turtle")
t.speed(3)
t.pensize(8)

# 원을 그리는 함수 정의 (색상과 좌표를 받음)
def draw_ring(color, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.pencolor(color)
    t.circle(radius)

# 1. 윗줄 (파랑, 검정, 빨강)
# x좌표 간격을 220 정도로 잡으면 적당히 겹칩니다.
draw_ring("blue", -220, 0)
draw_ring("black", 0, 0)
draw_ring("red", 220, 0)

# 2. 아랫줄 (노랑, 초록)
# 윗줄 사이사이에 배치하기 위해 x좌표를 중간값으로 설정하고 y를 내립니다.
draw_ring("yellow", -110, -100)
draw_ring("green", 110, -100)

t.hideturtle()  # 그림 완성 후 거북이 숨기기
t.done()