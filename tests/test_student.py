from lib.student import Student

"""
Student constructs with an id, name and genre
"""
def test_student_constructs():
    student = Student(1, "Test Student", "Test Cohort")
    assert student.id == 1
    assert student.name == "Test Student"
    assert student.cohort == "Test Cohort"

"""
We can format students to strings nicely
"""
def test_students_format_nicely():
    student = Student(1, "Test Student", "Test Cohort")
    assert str(student) == "Student(1, Test Student, Test Cohort)"
    # Try commenting out the `__repr__` method in lib/student.py
    # And see what happens when you run this test again.

"""
We can compare two identical students
And have them be equal
"""
def test_students_are_equal():
    student1 = Student(1, "Test Student", "Test Cohort")
    student2 = Student(1, "Test Student", "Test Cohort")
    assert student1 == student2
    # Try commenting out the `__eq__` method in lib/student.py
    # And see what happens when you run this test again.
