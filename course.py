"""
course.py
Defines the Course class.
"""


class Course:
    def __init__(self, course_code, course_name):
        self._course_code = course_code
        self._course_name = course_name
        self._students = []        # list of student IDs enrolled in this course
        self._assessments = []     # list of Assessment (or subclass) objects

    # ---------- Getters ----------
    def get_code(self):
        return self._course_code

    def get_name(self):
        return self._course_name

    def get_students(self):
        return self._students

    def get_assessments(self):
        return self._assessments

    # ---------- Behaviour ----------
    def add_student(self, student_id):
        """Enrolls a student in this course by adding the student's ID."""
        if student_id not in self._students:
            self._students.append(student_id)

    def remove_student(self, student_id):
        if student_id in self._students:
            self._students.remove(student_id)

    def add_assessment(self, assessment):
        """Adds a Quiz, Exam, or Project object to the course."""
        self._assessments.append(assessment)

    def find_assessment(self, title):
        """Searches for an assessment by title. Returns the object or None."""
        for assessment in self._assessments:
            if assessment.get_title().lower() == title.lower():
                return assessment
        return None

    def display_info(self):
        """Shows course details: code, name, number of students, assessments."""
        print(f"Course Code : {self._course_code}")
        print(f"Course Name : {self._course_name}")
        print(f"Enrolled Students: {len(self._students)}")
        print("Assessments:")
        if not self._assessments:
            print("  (none yet)")
        for assessment in self._assessments:
            print(f"  - {assessment.get_title()} / Max Score: {assessment.get_max_score()}")
