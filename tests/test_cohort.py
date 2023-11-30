from datetime import date
from lib.cohort import Cohort

"""
Cohort constructs with an id, cohort_name and starting_date
"""
def test_cohort_constructs():
    today = date.today()
    cohort = Cohort(1, "Test Cohort", today)
    assert cohort.id == 1
    assert cohort.cohort_name == "Test Cohort"
    assert cohort.starting_date == today

"""
We can format cohorts to strings nicely
"""
def test_cohorts_format_nicely():
    today = date.today()
    cohort = Cohort(1, "Test Cohort", today)
    assert str(cohort) == f"Cohort(1, Test Cohort, {today})"
    # Try commenting out the `__repr__` method in lib/cohort.py
    # And see what happens when you run this test again.

"""
We can compare two identical cohorts
And have them be equal
"""
def test_cohorts_are_equal():
    today = date.today()
    cohort1 = Cohort(1, "Test Cohort", today)
    cohort2 = Cohort(1, "Test Cohort", today)
    assert cohort1 == cohort2
    # Try commenting out the `__eq__` method in lib/cohort.py
    # And see what happens when you run this test again.

# today == datetime.date(2023, 11, 30)