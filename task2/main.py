import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

def draw_koch_snowflake(order, size):
    window = turtle.Screen()
    window.bgcolor("blue")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.color("white")
    snowflake_turtle.width(3)
    snowflake_turtle.speed(4)

    snowflake_turtle.penup()
    snowflake_turtle.goto(-size / 2, 200)
    snowflake_turtle.pendown()

    for i in range(3):
        koch_snowflake(snowflake_turtle, order, size)
        snowflake_turtle.right(120)

    window.mainloop()

def main():
    level = input ('Enter number of vertices ')
    try:
        num_level = int(level)
        draw_koch_snowflake(num_level, 400)
    except:
        print ("Incorrect number of vertices")

if __name__ == "__main__":
    main()
