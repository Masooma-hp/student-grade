
"""
Student Gradebook & Course Manager
------------------------------------
A terminal-based Python application for managing students, instructors,
courses, and grades.

Demonstrates:
- Functions
- Lists & Dictionaries
- Object-Oriented Programming (OOP)
- Encapsulation
- Inheritance
- Method Overriding
"""


# ------------------------------------------------------------------
# BASE CLASS: Person
# ------------------------------------------------------------------
class Person:
    """Base class representing a generic person (encapsulated)."""

    def __init__(self, name, person_id):
        # Encapsulation: attributes are "protected" using a single underscore
        self._name = name
        self._person_id = person_id

    # --- Getters (encapsulation) ---
    def get_name(self):
        return self._name

    def get_id(self):
        return self._person_id

    # --- Setters (encapsulation) ---
    def set_name(self, name):
        self._name = name

    def display_info(self):
        """Base method — will be overridden by subclasses."""
        return f"ID: {self._person_id} | Name: {self._name}"

    def __str__(self):
        return self.display_info()


# ------------------------------------------------------------------
# SUBCLASS: Student (inherits from Person)
# ------------------------------------------------------------------
class Student(Person):
    """Represents a student, inherits from Person."""

    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self._enrolled_courses = []      # list of Course objects
        self._grades = {}                # dict: {course_code: [grades]}

    def enroll(self, course):
        if course not in self._enrolled_courses:
            self._enrolled_courses.append(course)
            self._grades[course.get_code()] = []

    def add_grade(self, course_code, grade):
        if course_code in self._grades:
            self._grades[course_code].append(grade)
            return True
        return False

    def get_average(self, course_code=None):
        """Return average grade for one course, or overall average."""
        if course_code:
            grades = self._grades.get(course_code, [])
            return sum(grades) / len(grades) if grades else 0.0
        else:
            all_grades = [g for grades in self._grades.values() for g in grades]
            return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def get_courses(self):
        return self._enrolled_courses

    # --- Method Overriding ---
    def display_info(self):
        courses = ", ".join(c.get_code() for c in self._enrolled_courses) or "None"
        avg = self.get_average()
        return (f"[Student] ID: {self._person_id} | Name: {self._name} | "
                f"Courses: {courses} | Overall Avg: {avg:.2f}")


# ------------------------------------------------------------------
# SUBCLASS: Instructor (inherits from Person)
# ------------------------------------------------------------------
class Instructor(Person):
    """Represents an instructor, inherits from Person."""

    def __init__(self, name, person_id, department):
        super().__init__(name, person_id)
        self._department = department
        self._courses_taught = []

    def assign_course(self, course):
        if course not in self._courses_taught:
            self._courses_taught.append(course)

    def get_department(self):
        return self._department

    # --- Method Overriding ---
    def display_info(self):
        courses = ", ".join(c.get_code() for c in self._courses_taught) or "None"
        return (f"[Instructor] ID: {self._person_id} | Name: {self._name} | "
                f"Department: {self._department} | Teaches: {courses}")


# ------------------------------------------------------------------
# CLASS: Course
# ------------------------------------------------------------------
class Course:
    """Represents a course with an instructor and enrolled students."""

    def __init__(self, code, title, instructor=None):
        self._code = code
        self._title = title
        self._instructor = instructor
        self._students = []

    def get_code(self):
        return self._code

    def get_title(self):
        return self._title

    def set_instructor(self, instructor):
        self._instructor = instructor
        instructor.assign_course(self)

    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)

    def get_students(self):
        return self._students

    def __str__(self):
        instructor_name = self._instructor.get_name() if self._instructor else "TBA"
        return (f"[{self._code}] {self._title} | Instructor: {instructor_name} | "
                f"Enrolled: {len(self._students)} student(s)")


# ------------------------------------------------------------------
# CLASS: Gradebook (manages everything + menu system)
# ------------------------------------------------------------------
class Gradebook:
    """Main manager class that holds all students, instructors and courses."""

    def __init__(self):
        self._students = {}      # {student_id: Student}
        self._instructors = {}   # {instructor_id: Instructor}
        self._courses = {}       # {course_code: Course}

    # ---------------- Student management ----------------
    def add_student(self, name, student_id):
        if student_id in self._students:
            print("⚠ A student with this ID already exists.")
            return
        self._students[student_id] = Student(name, student_id)
        print(f"✅ Student '{name}' added successfully.")

    def list_students(self):
        if not self._students:
            print("No students found.")
            return
        for student in self._students.values():
            print(student.display_info())

    # ---------------- Instructor management ----------------
    def add_instructor(self, name, instructor_id, department):
        if instructor_id in self._instructors:
            print("⚠ An instructor with this ID already exists.")
            return
        self._instructors[instructor_id] = Instructor(name, instructor_id, department)
        print(f"✅ Instructor '{name}' added successfully.")

    def list_instructors(self):
        if not self._instructors:
            print("No instructors found.")
            return
        for instructor in self._instructors.values():
            print(instructor.display_info())

    # ---------------- Course management ----------------
    def add_course(self, code, title, instructor_id=None):
        if code in self._courses:
            print("⚠ A course with this code already exists.")
            return
        instructor = self._instructors.get(instructor_id)
        course = Course(code, title, instructor)
        if instructor:
            instructor.assign_course(course)
        self._courses[code] = course
        print(f"✅ Course '{title}' ({code}) added successfully.")

    def list_courses(self):
        if not self._courses:
            print("No courses found.")
            return
        for course in self._courses.values():
            print(course)

    # ---------------- Enrollment & Grades ----------------
    def enroll_student(self, student_id, course_code):
        student = self._students.get(student_id)
        course = self._courses.get(course_code)
        if not student or not course:
            print("⚠ Student or course not found.")
            return
        student.enroll(course)
        course.add_student(student)
        print(f"✅ {student.get_name()} enrolled in {course.get_code()}.")

    def add_grade(self, student_id, course_code, grade):
        student = self._students.get(student_id)
        if not student:
            print("⚠ Student not found.")
            return
        success = student.add_grade(course_code, grade)
        if success:
            print(f"✅ Grade {grade} added for {student.get_name()} in {course_code}.")
        else:
            print("⚠ Student is not enrolled in this course.")

    def show_student_report(self, student_id):
        student = self._students.get(student_id)
        if not student:
            print("⚠ Student not found.")
            return
        print("\n--- Student Report ---")
        print(student.display_info())
        for course in student.get_courses():
            avg = student.get_average(course.get_code())
            print(f"  {course.get_code()} - {course.get_title()}: Avg = {avg:.2f}")


# ------------------------------------------------------------------
# FUNCTION: input helpers
# ------------------------------------------------------------------
def get_float_input(prompt):
    """Helper function to safely get a float grade from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠ Please enter a valid number.")


# ------------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------------
def main():
    gb = Gradebook()

    menu = """
====== Student Gradebook & Course Manager ======
1. Add Student
2. Add Instructor
3. Add Course
4. Enroll Student in Course
5. Add Grade
6. View All Students
7. View All Instructors
8. View All Courses
9. View Student Report
0. Exit
=================================================
"""

    while True:
        print(menu)
        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            sid = input("Student ID: ").strip()
            gb.add_student(name, sid)

        elif choice == "2":
            name = input("Instructor name: ").strip()
            iid = input("Instructor ID: ").strip()
            dept = input("Department: ").strip()
            gb.add_instructor(name, iid, dept)

        elif choice == "3":
            code = input("Course code (e.g. CS101): ").strip()
            title = input("Course title: ").strip()
            iid = input("Instructor ID (leave blank if none): ").strip()
            gb.add_course(code, title, iid if iid else None)

        elif choice == "4":
            sid = input("Student ID: ").strip()
            code = input("Course code: ").strip()
            gb.enroll_student(sid, code)

        elif choice == "5":
            sid = input("Student ID: ").strip()
            code = input("Course code: ").strip()
            grade = get_float_input("Grade (0-100): ")
            gb.add_grade(sid, code, grade)

        elif choice == "6":
            print("\n--- All Students ---")
            gb.list_students()

        elif choice == "7":
            print("\n--- All Instructors ---")
            gb.list_instructors()

        elif choice == "8":
            print("\n--- All Courses ---")
            gb.list_courses()

        elif choice == "9":
            sid = input("Student ID: ").strip()
            gb.show_student_report(sid)

        elif choice == "0":
            print("Goodbye! 👋")
            break

        else:
            print("⚠ Invalid option, please try again.")


if __name__ == "__main__":
    main()
while True:
        print(menu)
        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            sid = input("Student ID: ").strip()
            gb.add_student(name, sid)

        elif choice == "2":
            name = input("Instructor name: ").strip()
            iid = input("Instructor ID: ").strip()
            dept = input("Department: ").strip()
            gb.add_instructor(name, iid, dept)

        elif choice == "3":
            code = input("Course code (e.g. CS101): ").strip()
            title = input("Course title: ").strip()
            iid = input("Instructor ID (leave blank if none): ").strip()
            gb.add_course(code, title, iid if iid else None)

        elif choice == "4":
            sid = input("Student ID: ").strip()
            code = input("Course code: ").strip()
            gb.enroll_student(sid, code)

        elif choice == "5":
            sid = input("Student ID: ").strip()
            code = input("Course code: ").strip()
            grade = get_float_input("Grade (0-100): ")
            gb.add_grade(sid, code, grade)

        elif choice == "6":
            print("\n--- All Students ---")
            gb.list_students()

        elif choice == "7":
            print("\n--- All Instructors ---")
            gb.list_instructors()

        elif choice == "8":
            print("\n--- All Courses ---")
            gb.list_courses()

        elif choice == "9":
            sid = input("Student ID: ").strip()
            gb.show_student_report(sid)

        elif choice == "0":
            print("Goodbye! 👋")
            break

        else:
            print("⚠ Invalid option, please try again.")


if __name__ == "__main__":
    main()