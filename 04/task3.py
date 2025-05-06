import turtle

# Функція для малювання спіралі з прямих ліній
def draw_line_spiral(steps, length):
    for i in range(steps):
        turtle.forward(length)  
        turtle.left(30)  
        length += 5  

# Функція для малювання правильного багатокутника
def draw_polygon(sides, side_length):
    angle = 360 / sides  
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.left(angle)  

def main():
    turtle.speed(0)  

    # Малюємо спіраль
    turtle.penup()
    turtle.goto(-200, 0)  
    turtle.pendown()
    draw_line_spiral(36, 10)  

    
    turtle.penup()
    turtle.goto(200, 0) 
    turtle.pendown()
    draw_polygon(12, 50)  

    turtle.done()

main()
