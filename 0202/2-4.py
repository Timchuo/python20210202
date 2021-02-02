import turtle
polygon = turtle.Turtle()
t2 = turtle.Turtle()
num_sides = int(input('要畫幾邊形(3-10)?'))
side_leng = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_leng)
    t2.forward(side_leng)
    t2.left(angle)
    polygon.right(angle)
turtle.done()
    
    