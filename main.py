"""
main.py
Entry point of the Student Gradebook & Course Manager.
Contains only the text menu / input-validation logic; the actual
data handling lives in the Gradebook, Student, Course, and
Assessment classes.
"""

from student import Student
from course import Course
from assessment import Quiz, Exam, Project
from gradebook import Gradebook


def get_int_input(prompt):
    """Keeps asking until the user enters a valid integer."""
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a whole number.")


def get_float_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a number.")


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def load_sample_data(gb):
    """Optional sample data so the menu can be tested quickly."""
    s1 = Student("S001", "Ahmad Rahimi", "ahmad@example.com")
    gb.add_student(s1)

    c1 = Course("PY101", "Python Programming")
    gb.add_course(c1)

    gb.enroll_student("S001", "PY101")

    gb.add_assessment("PY101", Quiz("Quiz 1", 10))
    gb.add_assessment("PY101", Exam("Midterm Exam", 100))
    gb.add_assessment("PY101", Project("Final Project", 100))

    gb.record_grade("S001", "PY101", "Quiz 1", 8)
    gb.record_grade("S001", "PY101", "Midterm Exam", 75)
    gb.record_grade("S001", "PY101", "Final Project", 90)


def add_student_menu(gb):
    student_id = get_non_empty("Student ID: ")
    if gb.get_student(student_id):
        print("A student with that ID already exists.")
        return
    name = get_non_empty("Name: ")
    email = get_non_empty("Email: ")
    gb.add_student(Student(student_id, name, email))


def add_course_menu(gb):
    code = get_non_empty("Course Code: ")
    if gb.get_course(code):
        print("A course with that code already exists.")
        return
    name = get_non_empty("Course Name: ")
    gb.add_course(Course(code, name))


def enroll_menu(gb):
    student_id = get_non_empty("Student ID: ")
    course_code = get_non_empty("Course Code: ")
    gb.enroll_student(student_id, course_code)


def add_assessment_menu(gb):
    course_code = get_non_empty("Course Code: ")
    if not gb.get_course(course_code):
        print("Course not found.")
        return
    title = get_non_empty("Assessment Title: ")
    max_score = get_float_input("Max Score: ")
    print("Type: 1) Quiz  2) Exam  3) Project")
    choice = get_non_empty("Choose type: ")
    if choice == "1":
        assessment = Quiz(title, max_score)
    elif choice == "2":
        assessment = Exam(title, max_score)
    elif choice == "3":
        assessment = Project(title, max_score)
    else:
        print("Invalid type.")
        return
    gb.add_assessment(course_code, assessment)


def record_grade_menu(gb):
    student_id = get_non_empty("Student ID: ")
    course_code = get_non_empty("Course Code: ")
    title = get_non_empty("Assessment Title: ")
    score = get_float_input("Score: ")
    gb.record_grade(student_id, course_code, title, score)


def search_student_menu(gb):
    keyword = get_non_empty("Search by ID or name: ")
    results = gb.search_student(keyword)
    if not results:
        print("No matching students found.")
        return
    for student in results:
        student.display_info()
        print("-" * 30)


def update_student_menu(gb):
    student_id = get_non_empty("Student ID to update: ")
    student = gb.get_student(student_id)
    if not student:
        print("Student not found.")
        return
    print("1) Update name  2) Update email")
    choice = get_non_empty("Choose: ")
    if choice == "1":
        student.set_name(get_non_empty("New name: "))
    elif choice == "2":
        student.set_email(get_non_empty("New email: "))
    else:
        print("Invalid choice.")


def delete_student_menu(gb):
    student_id = get_non_empty("Student ID to delete: ")
    gb.delete_student(student_id)


def show_report_menu(gb):
    student_id = get_non_empty("Student ID: ")
    gb.show_report(student_id)


def show_ranking_menu(gb):
    course_code = get_non_empty("Course Code: ")
    gb.show_ranking(course_code)


MENU_TEXT = """
===== Student Gradebook Manager =====
1. Add Student
2. View Students
3. Add Course
4. Enroll Student in Course
5. Add Assessment
6. Record Grade
7. View Student Report
8. Search Student
9. Update Student
10. Delete Student
11. Show Ranking (by course)
0. Exit
"""


def main():
    gb = Gradebook(passing_grade=55)
    load_sample_data(gb)   # comment this out if you don't want sample data

    actions = {
        "1": lambda: add_student_menu(gb),
        "2": lambda: gb.view_students(),
        "3": lambda: add_course_menu(gb),
        "4": lambda: enroll_menu(gb),
        "5": lambda: add_assessment_menu(gb),
        "6": lambda: record_grade_menu(gb),
        "7": lambda: show_report_menu(gb),
        "8": lambda: search_student_menu(gb),
        "9": lambda: update_student_menu(gb),
        "10": lambda: delete_student_menu(gb),
        "11": lambda: show_ranking_menu(gb),
    }

    while True:
        print(MENU_TEXT)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please choose a number from the menu.")


if __name__ == "__main__":
    main()
