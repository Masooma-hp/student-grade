# Student Gradebook & Course Manager

**Full Name:** _[Your Name Here]_

**Project Title:** Student Gradebook & Course Manager

## What This Project Does
A terminal-based Python application for managing students, courses,
assessments, and grades. Users can add students, add courses, enroll
students in courses, add quizzes/exams/projects, record grades, and
view a full student report with average grade, letter grade, and
pass/fail result.

## How to Run
```
python3 main.py
```
The program starts with a small set of sample data (one student,
one course, three assessments, and grades already recorded) so you
can test the menu immediately. Remove the `load_sample_data(gb)` call
in `main.py` if you want to start with an empty system.

## Classes Created
- **Student** (`student.py`) – stores student information.
- **Course** (`course.py`) – stores course information, enrolled
  students, and assessments.
- **Assessment** (`assessment.py`) – parent class for graded work.
- **Quiz, Exam, Project** (`assessment.py`) – child classes of
  `Assessment`.
- **Gradebook** (`gradebook.py`) – connects students, courses,
  assessments, and grades; contains the main business logic.
- **main.py** – the text menu only; it calls into the classes above
  but contains no data-storage logic of its own.

## Where OOP Concepts Were Used
- **Encapsulation:** `Student` stores all attributes as private
  (`_student_id`, `_name`, `_email`, `_courses`) and only exposes
  them through getter methods and a validating `set_email()` setter.
  The same pattern is used in `Course`, `Assessment`, and
  `Gradebook`.
- **Inheritance:** `Quiz`, `Exam`, and `Project` all inherit from the
  parent `Assessment` class (`assessment.py`).
- **Method Overriding:** each child class overrides
  `display_info()` and `grade_message()` to give assessment-specific
  output (e.g. `Quiz` gives quiz-style feedback, `Exam` checks a
  55% pass mark, `Project` rewards very high scores).

## Two Custom (Creative) Features
1. **Letter Grades** – `Gradebook.get_letter_grade()` converts a
   student's numeric average into a letter grade (A–F), shown on
   every student report.
2. **Ranking** – `Gradebook.show_ranking()` (menu option 11) lists
   every student enrolled in a course from the highest average to
   the lowest, along with their letter grade.

## Notes
- Data is **not saved** between runs (no file handling was used, as
  intended by the assignment).
- Input validation is used throughout: menu choices, numeric input,
  email format, grade ranges (0 to max score), and checks that a
  student/course/assessment exists before it is used.
