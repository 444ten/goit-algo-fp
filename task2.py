import turtle
import math

def draw_pythagoras_tree(t, branch_len, level):
    if level == 0:
        return

    # Draw the main branch
    t.forward(branch_len)

    # Right branch
    t.left(45)
    draw_pythagoras_tree(t, branch_len * math.sqrt(2) / 2, level - 1)

    # Left branch
    t.right(90)
    draw_pythagoras_tree(t, branch_len * math.sqrt(2) / 2, level - 1)

    # Return to the original position/angle
    t.left(45)
    t.backward(branch_len)

def main():
    try:
        recursion_level = int(input("Enter recursion level (recommended 6-10): "))
    except ValueError:
        print("Invalid input. Using default level 7.")
        recursion_level = 7

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Pythagoras Tree Fractal")

    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.left(90)  # Point upwards
    t.up()
    t.goto(0, -250)
    t.down()
    t.color("brown")

    draw_pythagoras_tree(t, 100, recursion_level)

    print("Drawing complete. Click on the window to exit.")
    screen.exitonclick()

if __name__ == "__main__":
    main()
