import turtle as t

radius = 50
t.shape("turtle")
t.speed = 3

def draw_ring(x , y):
    t.up()
    t.goto(x , y)
    t.down()
    t.circle(radius)

draw_ring(0 , 0)
radius += 20
draw_ring(100 , 0)
radius += 20
draw_ring(200 , 0)

t.done()