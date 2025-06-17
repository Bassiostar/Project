import math

class Polygon:
    """Base class for all shapes."""
    def __init__(self, name="Polygon"):
        # Encapsulated attribute for the shape's name
        self._name = name

    def area(self):
        """Abstract method to calculate the area."""
        raise NotImplementedError("Subclasses must implement the 'area' method.")

    def display_info(self):
        """Displays the calculated area for the shape."""
        try:
            print(f"The area of the {self._name} is: {self.area():.2f} square units.")
        except NotImplementedError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Input error for {self._name}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {self._name}: {e}")

class Triangle(Polygon):
    """Represents a triangle."""
    def __init__(self, base, height):
        super().__init__("Triangle")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive values.")
        self._base = base
        self._height = height

    def area(self):
        return 0.5 * self._base * self._height

class Rectangle(Polygon):
    """Represents a rectangle."""
    def __init__(self, length, width):
        super().__init__("Rectangle")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values.")
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

class Circle(Polygon):
    """Represents a circle."""
    def __init__(self, radius):
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        self._radius = radius

    def area(self):
        return math.pi * self._radius**2

# --- Program Execution ---
if __name__ == "__main__":
    shapes_to_calculate = []

    while True:
        print("\n--- Choose a Shape ---")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Calculate All & Exit")
        print("5. Exit Without Calculating")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == '1':
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                shapes_to_calculate.append(Triangle(base, height))
            elif choice == '2':
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                shapes_to_calculate.append(Rectangle(length, width))
            elif choice == '3':
                radius = float(input("Enter the radius of the circle: "))
                shapes_to_calculate.append(Circle(radius))
            elif choice == '4':
                print("\n--- Calculating Areas ---")
                for shape in shapes_to_calculate:
                    shape.display_info()
                break # Exit the loop after calculation
            elif choice == '5':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter numeric values greater than zero.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
# hello
# This code defines a base class Polygon and subclasses for Triangle, Rectangle, and Circle.