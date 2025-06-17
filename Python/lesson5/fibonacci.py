def fibonacci_series(n_terms):
    """
    Prints the Fibonacci series up to n_terms.

    Args:
        n_terms (int): The number of terms in the Fibonacci series to print.
    """
    if n_terms <= 0:
        print("Please enter a positive integer for the number of terms.")
        return
    elif n_terms == 1:
        print("Fibonacci series (1 term):")
        print(0)
        return

    # Initialize the first two terms
    a, b = 0, 1
    count = 0

    print(f"Fibonacci series up to {n_terms} terms:")

    while count < n_terms:
        print(a, end=" ") # Print the current term
        next_term = a + b  # Calculate the next term
        a = b              # Update 'a' to the current 'b'
        b = next_term      # Update 'b' to the newly calculated next term
        count += 1
    print() # Print a newline at the end for better formatting

# Get input from the user
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
    fibonacci_series(num_terms)
except ValueError:
    print("Invalid input. Please enter an integer.")