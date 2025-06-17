import os

# Define the filename
STUDENT_FILE = "students.txt"

def ensure_file_exists():
    """Ensures the student file exists. If not, it creates an empty one."""
    if not os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, 'w') as f:
            pass  # Create an empty file

def load_students():
    """
    Loads student data from the file.
    Returns a dictionary where keys are student names (lowercase)
    and values are their favorite subjects.
    """
    students = {}
    ensure_file_exists()
    try:
        with open(STUDENT_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        name, subject = line.split(',', 1) # Split only on the first comma
                        students[name.strip().lower()] = {'name': name.strip(), 'subject': subject.strip()}
                    except ValueError:
                        print(f"Skipping malformed line: {line}")
    except FileNotFoundError:
        # This case should ideally be handled by ensure_file_exists, but good to have as a fallback
        print(f"Warning: {STUDENT_FILE} not found. Starting with an empty record.")
    return students

def save_students(students_data):
    """
    Saves student data back to the file.
    Takes a dictionary of student data as input.
    """
    with open(STUDENT_FILE, 'w') as f:
        for student_info in students_data.values():
            f.write(f"{student_info['name']},{student_info['subject']}\n")
    print("Student records updated successfully!")

def add_or_update_student(students_data, name, subject):
    """
    Adds a new student or updates an existing one's favorite subject.
    """
    lower_name = name.lower()
    if lower_name in students_data:
        print(f"Updating {name}'s favorite subject from '{students_data[lower_name]['subject']}' to '{subject}'.")
    else:
        print(f"Adding new student: {name} with favorite subject: {subject}.")
    students_data[lower_name] = {'name': name, 'subject': subject}
    save_students(students_data)

def display_students(students_data):
    """
    Displays all registered students and their favorite subjects.
    """
    if not students_data:
        print("No student records found.")
        return

    print("\n--- Current Student Records ---")
    for student_info in students_data.values():
        print(f"Name: {student_info['name']}, Favorite Subject: {student_info['subject']}")
    print("-------------------------------\n")

def main():
    """Main function to run the student record management system."""
    students = load_students()

    while True:
        print("\n--- Roy's Student Record Manager ---")
        print("1. View all students")
        print("2. Add/Update student record")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_students(students)
        elif choice == '2':
            name = input("Enter student's name: ").strip()
            if not name:
                print("Student name cannot be empty.")
                continue
            subject = input(f"Enter {name}'s favorite subject: ").strip()
            if not subject:
                print("Favorite subject cannot be empty.")
                continue
            add_or_update_student(students, name, subject)
        elif choice == '3':
            print("Exiting Roy's Student Record Manager. Good luck, Roy!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()