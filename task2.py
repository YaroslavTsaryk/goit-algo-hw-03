import sys
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()


    for angle in [-120, -120, 0]:
        koch_curve(t, order, size)
        t.left(angle)
    
    window.mainloop()


def main(argv, argc):
    i=""
    while not i.isdigit():
        i= input("Number of iterations (int): ")
    # Виклик функції    
    draw_koch_curve(int(i))


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))