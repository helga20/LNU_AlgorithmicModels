import turtle

def draw_filled_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_smiley():
    turtle.speed(5)
    
    # Голова
    draw_filled_circle(0, 0, 100, "yellow")
    
    # Очі
    draw_filled_circle(-40, 40, 15, "black")
    draw_filled_circle(40, 40, 15, "black")
    
    # Усмішка
    turtle.penup()
    turtle.goto(-40, -30)
    turtle.pendown()
    turtle.color("black")
    turtle.setheading(-60)
    turtle.circle(40, 120)
    
    turtle.hideturtle()
    turtle.done()

draw_smiley()
