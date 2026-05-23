import turtle as t

t.shape = 20

x1 = int(input("x1 > "))
y1 = int(input("y1 > "))
x2 = int(input("x2 > "))
y2 = int(input("y2 > "))

distanceBetweenPoint = float(abs(((x1 - x2)**2 + (y1 - y2)**2)**0.5))

def draw(x1 , y1, x2 , y2):
    t.up()
    t.goto(x1 , y1)
    t.down()
    t.goto(x2 , y2)
    t.write(("점의 길이 : ", distanceBetweenPoint))
draw(x1, y1, x2 , y2)

t.done()