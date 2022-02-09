import turtle
import turtle as t

t.setup(800, 600)
t.speed(0.5)

# Left Hand
t.penup()
t.goto(177, 112)
t.pencolor("lightgray")
t.pensize(3)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.setheading(80)
t.circle(-45, 200)
t.circle(-300, 23)
t.end_fill()

# Left Hand - inner
t.penup()
t.goto(182, 95)
t.pencolor("black")
t.pensize(1)
t.fillcolor("black")
t.begin_fill()
t.setheading(95)
t.pendown()
t.circle(-37, 160)
t.circle(-20, 50)
t.circle(-200, 30)
t.end_fill()

# outline
# head - top
t.penup()
t.goto(-73, 230)
t.pencolor("lightgrey")
t.pensize(3)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.setheading(20)
t.circle(-250, 35)

# left ear
t.setheading(50)
t.circle(-42, 180)

# left side
t.setheading(-50)
t.circle(-190, 30)
t.circle(-320, 45)

# left leg
t.circle(120, 30)
t.circle(200, 12)
t.circle(-18, 85)
t.circle(-180, 23)
t.circle(-20, 110)
t.circle(15, 115)
t.circle(100, 12)

# right leg
t.circle(15, 120)
t.circle(-15, 110)
t.circle(-150, 30)
t.circle(-15, 70)
t.circle(-150, 10)
t.circle(200, 35)
t.circle(-150, 20)

# right hand
t.setheading(-120)
t.circle(50, 30)
t.circle(-35, 200)
t.circle(-300, 23)

# right side
t.setheading(86)
t.circle(-300, 26)

# right ear
t.setheading(122)
t.circle(-53, 160)
t.end_fill()

# right ear internal
t.penup()
t.goto(-130, 180)
t.pencolor("black")
t.pensize(1)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.setheading(120)
t.circle(-28, 160)
t.setheading(210)
t.circle(150, 20)
t.end_fill()

# left ear internal
t.penup()
t.goto(90, 230)
t.setheading(40)
t.begin_fill()
t.pendown()
t.circle(-30, 170)
t.setheading(125)
t.circle(150, 23)
t.end_fill()

# left hand - internal
# t.penup()
# t.goto(-180, -55)
# t.fillcolor("black")
# t.setheading(40)
# t.begin_fill()
# t.pendown()
# t.circle(-30, 170)
# t.setheading(125)
# t.circle(150, 23)
# t.end_fill()

# right hand - internal
t.penup()
t.goto(-180, -55)
t.fillcolor("black")
t.begin_fill()
t.setheading(-120)
t.setheading(-120)
t.pendown()
t.circle(50, 30)
t.circle(-27, 200)
t.circle(-300, 20)
t.setheading(-90)
t.circle(300, 14)
t.end_fill()

# left leg - internal
t.penup()
t.goto(108, -168)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.setheading(-115)
t.circle(110, 15)
t.circle(200, 10)
t.circle(-18, 80)
t.circle(-180, 13)
t.circle(-20, 90)
t.circle(15, 60)
t.setheading(42)
t.circle(-200, 29)
t.end_fill()

# right leg - internal
t.penup()
t.goto(-38, -210)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.setheading(-155)
t.circle(15, 100)
t.circle(-10, 110)
t.circle(-100, 30)
t.circle(-15, 65)
t.circle(-100, 10)
t.circle(200, 15)
t.setheading(-14)
t.circle(-200, 27)
t.end_fill()

# right eye - 眼圈
t.penup()
t.goto(-64, 120)
t.begin_fill()
t.pendown()
t.setheading(40)
t.circle(-35, 152)
t.circle(-100, 50)
t.circle(-35, 130)
t.circle(-100, 50)
t.end_fill()

# 右眼珠
t.penup()
t.goto(-47, 55)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.setheading(0)
t.circle(25, 360)
t.end_fill()
t.penup()
t.goto(-45, 62)
t.pencolor("darkslategray")
t.fillcolor("darkslategray")
t.begin_fill()
t.pendown()
t.setheading(0)
t.circle(19, 360)
# t.circle(19, 360)
t.end_fill()
t.penup()
t.goto(-45, 68)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.setheading(0)
t.circle(10, 360)
t.end_fill()
t.penup()
t.goto(-47, 86)
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.setheading(0)
t.circle(5, 360)
# t.circle(5, 360)
t.end_fill()

# left eye - 眼圈
t.penup()
t.goto(51, 82)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.setheading(120)
t.circle(-32, 152)
t.circle(-100, 55)
t.circle(-25, 120)
t.circle(-120, 45)
t.end_fill()

# 眼珠
t.penup()
t.goto(79, 60)
t.goto(79, 60)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.setheading(0)
t.circle(24, 360)
t.end_fill()
t.penup()
t.goto(79, 64)
t.pencolor("darkslategray")
t.fillcolor("darkslategray")
t.begin_fill()
t.pendown()
t.setheading(0)
t.circle(19, 360)
t.end_fill()
t.penup()
t.goto(79, 70)
# t.goto(79, 70)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.setheading(0)
t.circle(10, 360)
t.end_fill()
t.penup()
t.goto(79, 88)
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.setheading(0)
t.circle(5, 360)
t.end_fill()

# nose
t.penup()
t.goto(37, 80)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.circle(-8, 130)
t.circle(-22, 130)
t.end_fill()

# mouse
t.penup()
t.goto(-15, 48)
t.setheading(-36)
t.begin_fill()
t.pendown()
t.circle(60, 70)
t.setheading(-132)
t.circle(-45, 100)
t.end_fill()

# rainbow
t.penup()
t.goto(-135, 120)
t.pensize(5)
t.pencolor("cyan")
t.pendown()
t.setheading(60)
t.circle(-165, 150)
t.circle(-130, 78)
t.circle(-250, 30)
t.circle(-138, 105)
t.penup()
t.goto(-131, 116)
t.pencolor("slateblue")
t.pendown()
t.setheading(60)
t.circle(-160, 144)
t.circle(-120, 78)
t.circle(-242, 30)
t.circle(-135, 105)
t.penup()
t.goto(-127, 112)
t.pencolor("orangered")
t.pendown()
t.setheading(60)
t.circle(-155, 136)
t.circle(-116, 86)
t.circle(-220, 30)
t.circle(-134, 103)
t.penup()
t.goto(-123, 108)
t.pencolor("gold")
t.pendown()
t.setheading(60)
t.circle(-150, 136)
t.circle(-104, 86)
t.circle(-220, 30)
t.circle(-126, 102)
t.penup()
t.goto(-120, 104)
t.pencolor("greenyellow")
t.pendown()
t.setheading(60)
t.circle(-145, 136)
t.circle(-90, 83)
t.circle(-220, 30)
t.circle(-120, 100)
t.penup()

# heart shape
t.penup()
t.goto(220, 115)
t.pencolor("brown")
t.pensize(1)
t.fillcolor("brown")
t.begin_fill()
t.pendown()
t.setheading(36)
t.circle(-8, 180)
t.circle(-60, 24)
t.setheading(110)
t.circle(-60, 24)
t.circle(-8, 180)
t.end_fill()


# five rings
def draw_ring(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.circle(6)


draw_ring(-5, -170, "blue")
draw_ring(10, -170, "black")
draw_ring(25, -170, "brown")
draw_ring(2, -175, "lightgoldenrod")
draw_ring(16, -175, "green")
t.penup()
t.pencolor("black")
t.goto(-16, -160)
t.write("BEIJING 2022", font=('Arial', 10, 'bold italic'))
t.hideturtle()
t.done()
