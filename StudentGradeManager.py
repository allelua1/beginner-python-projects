# Store students and their marks in a dictionary
# Functions to: add student, calculate average, find highest/lowest scorer
# Use lambda to sort students by grade

students = [
    {"name": "Benigne", "Marks": 90},
    {"name": "Diane", "Marks": 80},
    {"name": "Ben", "Marks": 95}
]


def add_student(students, name, marks):
    """Add a new student with validation"""
    try:
        marks = int(marks)
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0-100")
            return
        students.append({"name": name, "Marks": marks})
        print(f"Student {name} with {marks} marks added successfully!")
    except ValueError:
        print("Error: Marks must be a valid number")


def calculate_average(students):
    """Calculate and return average marks"""
    if not students:
        print("No students in the system")
        return 0
    
    total = sum(student["Marks"] for student in students)
    average = total / len(students)
    print(f"Average Marks: {average:.2f}")
    return average


def find_highLow_Scorer(students):
    """Find and display highest and lowest scorers"""
    if not students:
        print("No students in the system")
        return
    
    marks = [student["Marks"] for student in students]
    highest = max(marks)
    lowest = min(marks)
    
    highest_student = [s["name"] for s in students if s["Marks"] == highest]
    lowest_student = [s["name"] for s in students if s["Marks"] == lowest]
    
    print(f"Highest scorer: {highest_student[0]} with {highest} marks")
    print(f"Lowest scorer: {lowest_student[0]} with {lowest} marks")


def display_student(students):
    """Display students sorted by grade (non-destructive)"""
    if not students:
        print("No students in the system")
        return
    
    # Sort without modifying original list
    sorted_students = sorted(students, key=lambda student: student["Marks"], reverse=True)
    print("\n--- Students Sorted by Grade (Highest to Lowest) ---")
    for student in sorted_students:
        print(f"{student['name']}: {student['Marks']} marks")
    print()


# Main program loop
while True:
    print("\n=== Student Grade Manager ===")
    print("1. Add Student")
    print("2. Calculate Average")
    print("3. Highest/Lowest Scorer")
    print("4. Display Sorted Student By Grade")
    print("5. Exit")

    try:
        choice = int(input("Enter number (1-5): "))
        
        if choice == 1:
            student_name = input("Enter Student Name: ")
            student_marks = input("Enter Student Marks: ")
            add_student(students, student_name, student_marks)
        elif choice == 2:
            calculate_average(students)
        elif choice == 3:
            find_highLow_Scorer(students)
        elif choice == 4:
            display_student(students)
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5")
    except ValueError:
        print("Error: Please enter a valid number")
        
