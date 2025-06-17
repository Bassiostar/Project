import turtle
def draw_equilateral_triangle(t, side_length, pen_color, fill_color):
    """
    Draws an equilateral triangle using the given turtle object.
    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        side_length (int): The length of each side of the triangle.
        pen_color (str): The color of the pen (outline).
        fill_color (str): The color to fill the triangle with.
    """
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill() # Start filling the shape

    for _ in range(3): # An equilateral triangle has 3 sides
        t.forward(side_length)
        t.left(120) # Turn 120 degrees for an equilateral triangle

    t.end_fill() # End filling the shape
def draw_rectangle(t, width, height, pen_color, fill_color):
    """
    Draws a rectangle using the given turtle object.
    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        pen_color (str): The color of the pen (outline).
        fill_color (str): The color to fill the rectangle with.
    """
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill() # Start filling the shape
    # Draw the four sides of the rectangle
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill() # End filling the shape
def draw_hexagon(t, side_length, pen_color, fill_color):
    """
    Draws a hexagon using the given turtle object.
    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        side_length (int): The length of each side of the hexagon.
        pen_color (str): The color of the pen (outline).
        fill_color (str): The color to fill the hexagon with.
    """
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill() # Start filling the shape
    for _ in range(6): # A hexagon has 6 sides
        t.forward(side_length)
        t.left(60) # Turn 60 degrees for a regular hexagon
    t.end_fill() # End filling the shape
# --- Main program setup ---
# 1. Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=600) # Set the window size
screen.bgcolor("lightgray") # Set the background color of the drawing window
screen.title("Polygon Drawing with Turtle") # Set the title of the window
# 2. Create a turtle object
artist = turtle.Turtle()
artist.speed(5) # Set the drawing speed (1-10, 0 for fastest)
artist.pensize(2) # Set the thickness of the pen
# --- Draw the shapes ---
# Draw Equilateral Triangle
artist.penup() # Lift the pen to move without drawing
artist.goto(-250, 100) # Move to a starting position for the triangle
artist.pendown() # Put the pen down to start drawing
draw_equilateral_triangle(artist, 100, "blue", "lightblue")
# Draw Rectangle
artist.penup() # Lift the pen
artist.goto(50, 100) # Move to a starting position for the rectangle
artist.pendown() # Put the pen down
draw_rectangle(artist, 150, 80, "red", "lightcoral")
# Draw Hexagon
artist.penup() # Lift the pen
artist.goto(-100, -150) # Move to a starting position for the hexagon
artist.pendown() # Put the pen down
draw_hexagon(artist, 70, "green", "lightgreen")
# Keep the window open until it's manually closed
turtle.done()