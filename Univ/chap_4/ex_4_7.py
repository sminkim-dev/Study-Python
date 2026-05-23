import turtle as t
t.shape("turtle")
t.speed = 10
t.pensize = 10
color_1 = input("색상 #1을 입력하십시오 > ")
color_2 = input("색상 #2을 입력하십시오 > ")
color_3 = input("색상 #3을 입력하십시오 > ")

def color_circle(color , x , y):
    r = 100
    t.up()
    t.goto(x , y)
    t.down()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

color_circle(color_1, -200 , 0)
color_circle(color_2 , 0 , 0)
color_circle(color_3 , 200 , 0)

t.done()