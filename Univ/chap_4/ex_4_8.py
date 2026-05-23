import turtle as t

point_arr = [int(x) for x in input("앞에서 부터 x1 , y1 , x2 , y2 , x3 , y3 순으로 입력하시오 >> ").split()]
#string = input("앞에서 부터 x1 , y1 , x2 , y2 , x3 , y3 순으로 입력하시오 >> ").split()
""" for i  in range(6):
    point_arr.append(int(string[i])) """

def draw(Points):
    t. speed(20)
    t.pensize(10)

    t.up()
    t.goto(Points[0] , Points[1])
    t.down()
    
    for i in range(2, len(Points) , 2):
        t.goto(Points[i] , Points[i + 1])

#draw(point_arr[0] , point_arr[1] , point_arr[2], point_arr[3], point_arr[4], point_arr[5])
draw(point_arr)
t.done()