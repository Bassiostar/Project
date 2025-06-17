import random

def guess_the_number():
    """
    Implements a number guessing game where the user tries to guess
    a randomly generated number within a specified range.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != secret_number:
        try:
            # Get user's guess
            guess_input = input("Take a guess: ")
            guess = int(guess_input) # Convert input to an integer
            attempts += 1 # Increment the attempt counter

            # Provide feedback to the user
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # Correct guess
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")

        except ValueError:
            # Handle cases where the user enters non-integer input
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

# Start the game
if __name__ == "__main__":
    guess_the_number()