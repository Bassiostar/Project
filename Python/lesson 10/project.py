import math

# Base class for all polygons (and shapes)
class Shape:
    def calculate_area(self):
        """
        Abstract method to calculate the area of the shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement 'calculate_area' method")

class Triangle(Shape):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive values.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values.")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be a positive value.")
        super().__init__(side, side) # A square is a rectangle with equal sides

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("All bases and height must be positive values.")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Input must be a positive number. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the Polygon Area Calculator!")

    while True:
        print("\nSelect a polygon to calculate its area:")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Square")
        print("4. Circle")
        print("5. Trapezoid")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        shape = None
        try:
            if choice == '1':
                base = get_positive_float_input("Enter the base of the triangle: ")
                height = get_positive_float_input("Enter the height of the triangle: ")
                shape = Triangle(base, height)
            elif choice == '2':
                length = get_positive_float_input("Enter the length of the rectangle: ")
                width = get_positive_float_input("Enter the width of the rectangle: ")
                shape = Rectangle(length, width)
            elif choice == '3':
                side = get_positive_float_input("Enter the side of the square: ")
                shape = Square(side)
            elif choice == '4':
                radius = get_positive_float_input("Enter the radius of the circle: ")
                shape = Circle(radius)
            elif choice == '5':
                base1 = get_positive_float_input("Enter the first base of the trapezoid: ")
                base2 = get_positive_float_input("Enter the second base of the trapezoid: ")
                height = get_positive_float_input("Enter the height of the trapezoid: ")
                shape = Trapezoid(base1, base2, height)
            elif choice == '6':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue

            if shape:
                area = shape.calculate_area()
                print(f"The area of the selected shape is: {area:.2f}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()