# -------------------------------------------------
# College Grade Management System
# -------------------------------------------------
# This program manages student grades using the
# standard U.S. college GPA scale (4.0 with +/-).
# It supports student records, grade reports,
# GPA calculation, and class summaries.
# -------------------------------------------------

students = {}  # student_name : list_of_numeric_grades


# Standard U.S. college GPA scale
GPA_SCALE = {
    "A": 4.0,  "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0,
    "F": 0.0
}


def get_letter_grade(score):
    """Convert numeric score to college letter grade."""
    if score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_gpa(grades):
    """Calculate GPA using college-grade weighting."""
    if not grades:
        return 0.0

    total_points = 0
    for grade in grades:
        letter = get_letter_grade(grade)
        total_points += GPA_SCALE[letter]

    return total_points / len(grades)


def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if name in students:
        print("Student already exists.")
    else:
        students[name] = []
        print("Student added successfully.")


def add_grade():
    name = input("Enter student name: ").strip()
    if name not in students:
        print("Student not found.")
        return

    try:
        grade = float(input("Enter grade (0–100): "))
        if 0 <= grade <= 100:
            students[name].append(grade)
            print("Grade added.")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid grade input.")


def view_student_report():
    name = input("Enter student name: ").strip()
    if name not in students:
        print("Student not found.")
        return

    grades = students[name]
    if not grades:
        print(f"{name} has no grades recorded.")
        return

    average = sum(grades) / len(grades)
    gpa = calculate_gpa(grades)

    print(f"\nAcademic Report: {name}")
    print("-" * 45)
    for i, grade in enumerate(grades, start=1):
        letter = get_letter_grade(grade)
        points = GPA_SCALE[letter]
        print(f"Course {i}: {grade:>5.1f} → {letter:<2} ({points:.1f})")

    print("-" * 45)
    print(f"Numeric Average: {average:.2f}")
    print(f"College GPA: {gpa:.2f}")


def view_class_summary():
    if not students:
        print("No students available.")
        return

    print("\nClass GPA Summary")
    print("-" * 55)
    print(f"{'Student':<15} {'Avg':>8} {'GPA':>8}")
    print("-" * 55)

    for name, grades in students.items():
        if grades:
            avg = sum(grades) / len(grades)
            gpa = calculate_gpa(grades)
            print(f"{name:<15} {avg:>8.2f} {gpa:>8.2f}")
        else:
            print(f"{name:<15} {'N/A':>8} {'0.00':>8}")


# Main menu loop
while True:
    print("\nCollege Grade Management Menu")
    print("1 - Add Student")
    print("2 - Add Grade")
    print("3 - View Student Report")
    print("4 - View Class Summary")
    print("5 - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        view_student_report()
    elif choice == "4":
        view_class_summary()
    elif choice == "5":
        print("System closed.")
        break
    else:
        print("Invalid option. Please try again.")
