def is_armstrong(num_str):
    """Checks if a number(given as a string) is an armstrong number."""
    try:
        num_int = int(num_str)
        num_digits = len(num_str)
        sum_of_powers = 0
        temp = num_int
        while temp > 0:
            digit = temp % 10
            sum_of_powers += digit ** num_digits
            temp //= 10
        return num_int == sum_of_powers
    except ValueError:
        return False
    if __name__ == "__main__":
        user_input = input("Enter a number: ")
        if is_armstrong(user_input):
            print(f"{user_input} is an Armstrong number.")