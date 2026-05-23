import turtle as t

color = ["red" , "yellow" , "blue" , "black"]
point = [0 , 0 , 10, -20 , 30 , 40 , 50 , -60]
__ck__ = 0
def draw(color , point):
    t.speed(0)
    t.pensize(5)

    t.fillcolor(color[0])
    t.goto(point[0] , point[1])
    t.stamp()

    for i in range(2 , len(point) , 2):
        c_idk = (i // 2) % len(color) 
        t.fillcolor(color[c_idk])
        t.goto(point[i] , point[i + 1])
        t.stamp()

draw(color, point)
t.done()