"""
assessment.py
Defines the parent Assessment class and the child classes
Quiz, Exam, and Project.

This file demonstrates INHERITANCE and METHOD OVERRIDING:
each child class overrides display_info() and grade_message()
to give assessment-specific behaviour.
"""


class Assessment:
    """Parent class representing a generic piece of graded work."""

    def __init__(self, title, max_score):
        self._title = title
        self._max_score = max_score

    # ---------- Getters ----------
    def get_title(self):
        return self._title

    def get_max_score(self):
        return self._max_score

    # ---------- Shared behaviour ----------
    def calculate_percentage(self, score):
        """Converts a raw score into a percentage of max_score."""
        if self._max_score == 0:
            return 0
        return round((score / self._max_score) * 100, 2)

    def grade_message(self, score):
        """Generic feedback message. Overridden by child classes."""
        percentage = self.calculate_percentage(score)
        if percentage >= 50:
            return "Satisfactory result."
        return "Needs improvement."

    def display_info(self):
        """Displays basic assessment information. Overridden by child classes."""
        print(f"{self._title} - Max Score: {self._max_score}")


class Quiz(Assessment):
    """Child class of Assessment representing a quiz."""

    def display_info(self):
        # Overrides parent method -> method overriding
        print(f"Quiz: {self._title} - Max Score: {self._max_score}")

    def grade_message(self, score):
        # Overrides parent method -> method overriding
        percentage = self.calculate_percentage(score)
        if percentage >= 80:
            return "Great quiz result!"
        elif percentage >= 50:
            return "Good effort on the quiz."
        else:
            return "Needs more practice."


class Exam(Assessment):
    """Child class of Assessment representing an exam."""

    PASSING_PERCENTAGE = 55

    def display_info(self):
        print(f"Exam: {self._title} - Max Score: {self._max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= self.PASSING_PERCENTAGE:
            return "Passed exam."
        else:
            return "Failed exam."


class Project(Assessment):
    """Child class of Assessment representing a project."""

    def display_info(self):
        print(f"Project: {self._title} - Max Score: {self._max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 90:
            return "Excellent project!"
        elif percentage >= 50:
            return "Project submitted."
        else:
            return "Project needs improvement."
