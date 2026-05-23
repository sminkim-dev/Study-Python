import turtle as t
# 7번 문제 포함. side 변수 기본 100 인 값을 변경 -> 200

t.shape("turtle")
t.speed = 3
t.pensize = 8

#side = 100
side = 200
for i in range(3):
    t.left(120)
    t.forward(side)
t.done()