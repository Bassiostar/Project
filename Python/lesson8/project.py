# Define a class named 'Robot' to represent our robot
class Robot:
    """
    A class to represent a robot, demonstrating Object-Oriented Programming concepts.
    """

    # The constructor method (__init__) initializes the attributes of a Robot object.
    # It takes 'name', 'model', and 'purpose' as parameters.
    def __init__(self, name, model, purpose):
        self.name = name        # Attribute: The name of the robot
        self.model = model      # Attribute: The model name/number of the robot
        self.purpose = purpose  # Attribute: The primary function or purpose of the robot

    # A method to introduce the robot.
    # Methods are functions associated with the class that operate on the object's data.
    def introduce(self):
        """
        Prints an introduction message for the robot, using its attributes.
        """
        print(f"Hello! My name is {self.name}.")
        print(f"I am a {self.model} model robot.")
        print(f"My primary purpose is to {self.purpose}.")
        print("It's a pleasure to meet you!")

    # Another method to demonstrate a simple action the robot can perform.
    def perform_action(self, action_description):
        """
        Simulates the robot performing a specified action.
        """
        print(f"{self.name} is now performing: {action_description}")

# --- Creating Objects (Instances) of the Robot Class ---

# Create the first robot object
# This is an instance of the 'Robot' class, with specific values for its attributes.
robot1 = Robot("RoboFriend", "A-1000", "assist with daily tasks")

# Create a second robot object
robot2 = Robot("DataBot", "D-500", "analyze large datasets")

# --- Using the Objects and their Methods ---

print("--- Robot 1 Introduction ---")
# Call the 'introduce' method on the 'robot1' object.
# The method uses the 'name', 'model', and 'purpose' attributes of 'robot1'.
robot1.introduce()
robot1.perform_action("scanning the environment for anomalies")
print("\n") # Add a newline for better readability between robot introductions

print("--- Robot 2 Introduction ---")
# Call the 'introduce' method on the 'robot2' object.
robot2.introduce()
robot2.perform_action("compiling a financial report")
print("\n")

# You can also access attributes directly, though it's often better to use methods
# if there's complex logic involved in retrieving or setting the data.
print(f"Robot 1's name is: {robot1.name}")
print(f"Robot 2's purpose is: {robot2.purpose}")
