import turtle as t

t.speed = 10
t.pensize = 5

def car_body(color, x, y):
    t.up() # 이동할 때는 선을 안 그리게 펜을 듭니다.
    t.goto(x, y) # 지정된 위치로 이동
    t.down() # 그리기 시작할 때 펜을 내립니다.

    # ⭐ 색 채우기 핵심: fill하기 전에 색을 미리 정합니다.
    t.color(color) 
    
    # ⭐ 색 채우기 시작
    t.begin_fill() 

    # ⭐ 직사각형 그리기 (가로 200, 세로 80)
    for i in range(2):
        t.forward(200) # 가로 길게
        t.left(90)
        t.forward(80) # 세로 짧게
        t.left(90)

    # ⭐ 색 채우기 끝 (여기에 color를 넣지 않습니다!)
    t.end_fill() 

def car_wheel(color, x , y):
    r = 20
    t.up()
    t.goto(x , y)
    t.down()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
def car_top(color , x , y):
    t.up()
    t.goto(x , y)
    t.down()
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()
# 검은색 자동차 몸체 그리기 (위치: -100, -40 으로 조정) 길이 200 높이 80
car_body("black", -100, -40)
car_wheel("blue" , -50, -50)
car_wheel("blue", 50, - 50)
car_top("green" , -50 , 40)

t.done()