"""
student.py
Defines the Student class.

This class demonstrates ENCAPSULATION:
all attributes are stored as "private" (prefixed with a single underscore)
and can only be read or changed through getter / setter methods.
"""

import re


class Student:
    def __init__(self, student_id, name, email):
        self._student_id = student_id
        self._name = name
        self._email = email
        self._courses = []          # list of course codes the student is enrolled in

    # ---------- Getters ----------
    def get_id(self):
        """Returns the student's ID."""
        return self._student_id

    def get_name(self):
        """Returns the student's name."""
        return self._name

    def get_email(self):
        return self._email

    def get_courses(self):
        return self._courses

    # ---------- Setters ----------
    def set_email(self, email):
        """Updates the student's email address, after validating its format."""
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if re.match(pattern, email):
            self._email = email
            return True
        else:
            print("Invalid email format. Email was not updated.")
            return False

    def set_name(self, name):
        if name.strip():
            self._name = name
            return True
        print("Invalid name.")
        return False

    # ---------- Behaviour ----------
    def enroll_course(self, course_code):
        """Adds a course code to the student's course list (no duplicates)."""
        if course_code not in self._courses:
            self._courses.append(course_code)

    def remove_course(self, course_code):
        if course_code in self._courses:
            self._courses.remove(course_code)

    def display_info(self):
        """Shows the student's basic information."""
        print(f"Student ID : {self._student_id}")
        print(f"Name       : {self._name}")
        print(f"Email      : {self._email}")
        courses = ", ".join(self._courses) if self._courses else "None"
        print(f"Courses    : {courses}")
