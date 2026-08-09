# Task 1: Introduction
# This program addresses the problem of managing student academic records in an educational institution. The Student Academic Management System automates the process of recording student profiles, logging scores across multiple enrolled courses, calculating average percentages, determining pass/fail status, and assigning letter grades.

# Task 2: Terminal Execution
# To execute the Python program through the terminal:

# Open system Terminal, Command Prompt, or PowerShell.

# Navigate to the folder containing main.py:

# Bash
# cd path/to/your/folder
# Run the script using the Python interpreter:

# Bash
# python main.py
# (On macOS/Linux, use python3 main.py if required)

# Task 3: Python Interpreter (Interactive REPL)
# The Python interactive interpreter allows testing individual expressions, variables, and data structures step-by-step prior to writing full programs.

# Launch interactive mode from terminal:

# Bash
# python
# Test sample commands directly:

# Python
# >>> student_name = "Sarah"
# >>> scores = [88, 92, 79]
# >>> total = sum(scores)
# >>> avg = total / len(scores)
# >>> print(f"{student_name}'s Average: {avg:.2f}")
# Sarah's Average: 86.33
# >>> exit()


# ==============================================================================
# STUDENT ACADEMIC MANAGEMENT SYSTEM
# ==============================================================================

# ------------------------------------------------------------------------------
# TASK 4: VARIABLES
# ------------------------------------------------------------------------------
system_name = "Academic Performance Tracker"  # String variable
passing_score = 60                            # Integer variable
gpa_scale = 4.0                               # Float variable
is_system_active = True                      # Boolean variable

# ------------------------------------------------------------------------------
# TASK 7: LISTS AND TUPLES
# ------------------------------------------------------------------------------
# Immutable Tuple holding permanent system metadata
SYSTEM_METADATA = ("SYS-2026", "v1.0", "University Academic Portal")

# Mutable List storing available course offerings
course_catalog = ["CS101", "CS102", "MATH201", "ENG101"]

# ------------------------------------------------------------------------------
# TASK 6: DICTIONARY USAGE
# ------------------------------------------------------------------------------
# Nested dictionary to store student records, profiles, and subject grades
students_db = {
    "S101": {
        "name": "Sarah Ahmed",
        "major": "Computer Science",
        "scores": {"CS101": 88, "MATH201": 92, "ENG101": 79}
    },
    "S102": {
        "name": "Bilal Khan",
        "major": "Data Science",
        "scores": {"CS101": 55, "MATH201": 62, "ENG101": 48}
    }
}


def calculate_grade(average):
    """
    TASK 5 & TASK 8: OPERATORS AND CONDITIONAL STATEMENTS
    Determines letter grade using logical comparison operators and if-elif-else logic.
    """
    if average >= 90:
        return "A"
    elif average >= 80 and average < 90:  # Logical 'and' with relational operator
        return "B"
    elif average >= 70 and average < 80:
        return "C"
    elif average >= 60 and average < 70:
        return "D"
    else:
        return "F"


def display_all_students():
    """
    TASK 9: THE FOR LOOP
    Iterates through student dictionary data to compute and display performance metrics.
    """
    print("\n--- ALL STUDENT ACADEMIC RECORDS ---")
    
    # Task 9: Iterating over key-value pairs of the nested dictionary
    for student_id, details in students_db.items():
        name = details["name"]
        major = details["major"]
        scores_dict = details["scores"]
        
        # Task 5: Arithmetic operators (+ and /)
        total_marks = sum(scores_dict.values())
        total_subjects = len(scores_dict)
        average = total_marks / total_subjects if total_subjects > 0 else 0.0
        
        # Task 8: Conditional pass/fail check
        grade = calculate_grade(average)
        is_passed = average >= passing_score  # Task 5: Relational operator (>=)
        status = "PASSED" if is_passed else "FAILED"

        print(f"\nID: {student_id} | Name: {name} | Major: {major}")
        print("  Subject Scores:")
        for course, score in scores_dict.items():
            print(f"    - {course}: {score}")
        print(f"  Average: {average:.2f}% | Grade: {grade} | Status: {status}")


def add_student():
    """
    TASK 10: USER INPUT AND WHILE LOOP
    Captures dynamic input from user with numerical validation loops.
    """
    print("\n--- ADD NEW STUDENT RECORD ---")
    student_id = input("Enter Student ID (e.g., S103): ").strip().upper()
    
    if student_id in students_db:
        print("Error: Student ID already exists in system!")
        return

    name = input("Enter Student Name: ").strip()
    major = input("Enter Major: ").strip()
    
    scores = {}
    print("\nEnter scores for available catalog courses (0-100):")
    
    # Task 9: Loop through list of courses
    for course in course_catalog:
        # Task 10: Input validation loop using while True
        while True:
            try:
                score_str = input(f"  Score for {course}: ")
                score = float(score_str)  # Variable type conversion
                
                # Task 5 & 8: Range validation with comparison and logical operators
                if 0 <= score <= 100:
                    scores[course] = score
                    break
                else:
                    print("    Invalid range! Enter a score between 0 and 100.")
            except ValueError:
                print("    Invalid input! Enter a valid numeric score.")

    # Task 6: Updating dictionary with new key-value entry
    students_db[student_id] = {
        "name": name,
        "major": major,
        "scores": scores
    }
    print(f"\nSuccess: Record for {name} ({student_id}) added successfully!")


# ------------------------------------------------------------------------------
# MAIN EXECUTION ROUTINE
# ------------------------------------------------------------------------------
def main():
    print("=" * 60)
    print(f"  {system_name}")
    print(f"  System ID: {SYSTEM_METADATA[0]} | Version: {SYSTEM_METADATA[1]}")
    print("=" * 60)

    # Task 10: Interactive CLI application loop
    while is_system_active:
        print("\n--- MENU OPTIONS ---")
        print("1. View All Student Records")
        print("2. Add New Student Record")
        print("3. View System Metadata & Course Catalog")
        print("4. Exit Program")
        
        # Task 10: User Input
        user_choice = input("\nSelect an option (1-4): ").strip()

        # Task 8: Decision control logic
        if user_choice == "1":
            display_all_students()
        elif user_choice == "2":
            add_student()
        elif user_choice == "3":
            print(f"\nSystem Metadata (Tuple): {SYSTEM_METADATA}")
            print(f"Available Courses (List): {course_catalog}")
        elif user_choice == "4":
            print("\nExiting System. All session tasks completed.")
            break
        else:
            print("Invalid selection! Please enter a option between 1 and 4.")


if __name__ == "__main__":
    main()