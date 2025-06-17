# Function to calculate attendance percentage
def calculate_attendance(total_classes, absent_classes):
    attended_classes = total_classes - absent_classes
    percentage = (attended_classes / total_classes) * 100
    return percentage

# Main code
if __name__ == "__main__":
    # Input from the user
    total_classes = int(input("Enter total number of working days: "))
    absent_classes = int(input("Enter total number of days absent: "))

    # Calculate attendance percentage
    attendance_percentage = calculate_attendance(total_classes, absent_classes)

    print(f"Attendance Percentage: {attendance_percentage:.2f}%")

    # Check eligibility
    if attendance_percentage < 75:
        print("You are not eligible to sit in the exam.")
    else:
        print("You are eligible to sit in the exam.")