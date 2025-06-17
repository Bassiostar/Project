def convert_tuple_to_list(input_tuple):
    """
    Converts a given tuple into a list.

    Args:
        input_tuple (tuple): The tuple to be converted.

    Returns:
        list: A new list containing the elements of the input tuple.
    """
    # The simplest and most common way to convert a tuple to a list
    # is to use the built-in list() constructor.
    # This constructor takes an iterable (like a tuple) and returns a new list.
    converted_list = list(input_tuple)
    return converted_list

# --- Example Usage ---

# 1. Define a sample tuple
my_tuple = (1, 2, 3, 'apple', 'banana', True)
print(f"Original tuple: {my_tuple}")
print(f"Type of original tuple: {type(my_tuple)}")

# 2. Convert the tuple to a list using the function
my_list = convert_tuple_to_list(my_tuple)
print(f"Converted list: {my_list}")
print(f"Type of converted list: {type(my_list)}")

# Another example with an empty tuple
empty_tuple = ()
empty_list = convert_tuple_to_list(empty_tuple)
print(f"\nOriginal empty tuple: {empty_tuple}")
print(f"Converted empty list: {empty_list}")
print(f"Type of converted empty list: {type(empty_list)}")

# Example with a tuple containing a single element
single_element_tuple = ("hello",) # Remember the comma for a single-element tuple
single_element_list = convert_tuple_to_list(single_element_tuple)
print(f"\nOriginal single-element tuple: {single_element_tuple}")
print(f"Converted single-element list: {single_element_list}")
print(f"Type of converted single-element list: {type(single_element_list)}")