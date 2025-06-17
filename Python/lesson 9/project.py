class Expression:
    """
    Represents a mathematical expression.
    """
    def __init__(self, expression_string):
        """
        Initializes an Expression object with the given string.

        Args:
            expression_string (str): The mathematical expression as a string.
        """
        if not isinstance(expression_string, str):
            raise TypeError("Expression must be a string.")
        if not expression_string:
            raise ValueError("Expression string cannot be empty.")
        self._expression_string = expression_string

    def get_expression(self):
        """
        Returns the stored expression string.
        """
        return self._expression_string

    def evaluate(self):
        """
        Evaluates the mathematical expression and returns the result.

        Raises:
            ValueError: If the expression is invalid or contains unsafe operations.
            SyntaxError: If the expression has a syntax error.
            NameError: If the expression contains undefined variables.

        Returns:
            float or int: The result of the expression.
        """
        try:
            # Using eval() for simplicity. For production, consider a safer parser.
            result = eval(self._expression_string)
            return result
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            raise ValueError(f"Error evaluating expression '{self._expression_string}': {e}")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {e}")

# --- Usage Example ---
if __name__ == "__main__":
    # 1. Create Expression objects
    expression1 = Expression("10 + 5 * 2")
    expression2 = Expression("(25 - 5) / 4")
    expression3 = Expression("7 ** 2") # 7 to the power of 2
    expression4 = Expression("10 / 0") # Division by zero example
    expression5 = Expression("2 + invalid_var") # Name error example
    expression6 = Expression("10 + (5 * 2") # Syntax error example

    # 2. Evaluate and print results
    print(f"--- Solving Expressions ---")

    try:
        exp_str1 = expression1.get_expression()
        result1 = expression1.evaluate()
        print(f"Expression: '{exp_str1}' = {result1}")
    except ValueError as e:
        print(f"Error processing expression '{expression1.get_expression()}': {e}")

    try:
        exp_str2 = expression2.get_expression()
        result2 = expression2.evaluate()
        print(f"Expression: '{exp_str2}' = {result2}")
    except ValueError as e:
        print(f"Error processing expression '{expression2.get_expression()}': {e}")

    try:
        exp_str3 = expression3.get_expression()
        result3 = expression3.evaluate()
        print(f"Expression: '{exp_str3}' = {result3}")
    except ValueError as e:
        print(f"Error processing expression '{expression3.get_expression()}': {e}")

    print("\n--- Demonstrating Error Handling ---")
    try:
        exp_str4 = expression4.get_expression()
        result4 = expression4.evaluate()
        print(f"Expression: '{exp_str4}' = {result4}")
    except ValueError as e:
        print(f"Error processing expression '{expression4.get_expression()}': {e}")

    try:
        exp_str5 = expression5.get_expression()
        result5 = expression5.evaluate()
        print(f"Expression: '{exp_str5}' = {result5}")
    except ValueError as e:
        print(f"Error processing expression '{exp_str5}': {e}")

    try:
        exp_str6 = expression6.get_expression()
        result6 = expression6.evaluate()
        print(f"Expression: '{exp_str6}' = {result6}")
    except ValueError as e:
        print(f"Error processing expression '{exp_str6}': {e}")

    print("\n--- Testing edge cases for initialization ---")
    try:
        # expression_invalid = Expression(123) # This will raise a TypeError
        # expression_empty = Expression("")      # This will raise a ValueError
        pass # Commented out to avoid stopping execution if you just want to run the main examples
    except (TypeError, ValueError) as e:
        print(f"Initialization error: {e}")