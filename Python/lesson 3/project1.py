# Function to swap three numbers
def swap_numbers(a, b, c):
    return c, a, b

# Main code
if __name__ == "__main__":
    # Input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    print(f"Before swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")

    # Swapping the numbers
    num1, num2, num3 = swap_numbers(num1, num2, num3)

    print(f"After swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")