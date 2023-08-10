import turtle

# Create a turtle object
window = turtle.Screen()
window.title("Ashok Chakra")
ashok = turtle.Turtle()

# Set turtle speed and shape
ashok.speed(3)
ashok.shape("turtle")

# Set background color
window.bgcolor("white")

# Move turtle to starting position
ashok.penup()
ashok.goto(-100, 0)
ashok.pendown()

# Set color for wheel spokes
ashok.color("blue")

# Draw the 24 spokes of the wheel
for _ in range(24):
    ashok.forward(100)
    ashok.backward(100)
    ashok.right(15)

# Set color for the wheel circle
ashok.color("navy")

# Draw the outer circle of the wheel
ashok.penup()
ashok.goto(0, -100)
ashok.pendown()
ashok.circle(100)

# Set color for the inner circle
ashok.color("white")

# Draw the inner circle of the wheel
ashok.penup()
ashok.goto(0, -80)
ashok.pendown()
ashok.circle(80)

# Hide the turtle
ashok.hideturtle()

# Close the turtle graphics window on click
turtle.done()
