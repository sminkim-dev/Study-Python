import turtle as t

t.speed = 3
t.pensize = 8

radius = 100
def draw_rings(color , x , y):
    t.pencolor(color)
    t.up()
    t.goto(x , y)
    t.down()
    t.circle(radius)
# line row 1
draw_rings("black" , 0 , 0)
draw_rings("blue", 220 , 0)
draw_rings("green", -220 , 0)
#line row 2
draw_rings("purple" , 110 , - 100)
draw_rings("red", -110 , -100)
t.done()