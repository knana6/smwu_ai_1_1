import  turtle
turtle.shape("turtle")
turtle.pensize(5)
turtle.pencolor("blue")

while True:
    angle=int(input("거북이의회전속도"))
    distance=int(input("거북이의이동거리"))

    turtle.right(angle)
    turtle.forward(distance)
