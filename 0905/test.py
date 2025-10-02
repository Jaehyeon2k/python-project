import turtle

t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("lightblue")  # 背景颜色

t.color("white")

t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(0, 80)  
t.pendown()

t.begin_fill()
t.circle(35)     
t.end_fill()

def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)   # 眼睛大小
    t.end_fill()

draw_eye(-15, 120)   # 左眼
draw_eye(15, 120)

t.pensize(3)
t.color("brown")

# 左手
t.penup()
t.goto(-40, 75)  # 身体左侧
t.pendown()
t.setheading(160) # 左上方向
t.forward(80)

# 右手
t.penup()
t.goto(40, 75)   # 身体右侧
t.pendown()
t.setheading(20)  # 右上方向
t.forward(80)

turtle.forward(20)
t.goto(-7.5 , 100)

turtle.done()