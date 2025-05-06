import turtle

# Функція для малювання сонця
def draw_sun(radius):
    # Малюємо коло
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(radius)  
    turtle.end_fill()

    # Малюємо сонячні промені
    for _ in range(12):  
        turtle.penup()
        turtle.goto(0, 0)  
        turtle.forward(radius)  
        turtle.pendown()
        turtle.forward(50)  
        turtle.penup()
        turtle.backward(radius + 50)  
        turtle.left(30)  

def main():
    turtle.speed(5) 

    turtle.penup()
    turtle.goto(0, -100)  
    turtle.pendown()
    draw_sun(100)  

    turtle.done()

main()
