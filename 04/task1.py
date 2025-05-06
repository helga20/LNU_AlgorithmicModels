import turtle

def example_1():
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(1)
    t.forward(100)
    t.right(90)
    t.forward(100)
    turtle.done()

def example_2():
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(1)
    for _ in range(4):
        t.forward(100)
        t.right(90)
    turtle.done()

def example_3():
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(1)
    t.circle(50)
    turtle.done()

def example_4():
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(1)
    for _ in range(3):
        t.forward(100)
        t.left(120)
    turtle.done()

if __name__ == "__main__":
    # example_1()  # Прямокутний маршрут
    # example_2()  # Малювання квадрата
    # example_3()  # Малювання кола
    example_4()  # Малювання трикутника
    pass