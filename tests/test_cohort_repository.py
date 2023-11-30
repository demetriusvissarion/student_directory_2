from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort

"""
When we call CohortRepository#all
We get a list of Cohort objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/student_directory_2.sql") # Seed our database with some test data
    repository = CohortRepository(db_connection) # Create a new CohortRepository

    cohorts = repository.all() # Get all cohorts
    print('cohorts')

    # Assert on the results
    assert str(cohorts) == '[Cohort(1, Cohort 1, 2023-11-28), Cohort(2, Cohort 2, 2023-11-29), Cohort(3, Cohort 3, 2023-11-30)]'


def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohort_of_the_student = repository.find_with_students(1)
    assert str(cohort_of_the_student) == 'Cohort(1, Cohort 1, 2023-11-28)'

# """
# When we call CohortRepository#find
# We get a single Cohort object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/student_directory_2.sql")
#     repository = CohortRepository(db_connection)

#     cohort = repository.find(3)
#     assert cohort == Cohort(3, "Taylor Swift", "Pop")

# """
# When we call CohortRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/student_directory_2.sql")
#     repository = CohortRepository(db_connection)

#     repository.create(Cohort(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Cohort(1, "Pixies", "Rock"),
#         Cohort(2, "ABBA", "Pop"),
#         Cohort(3, "Taylor Swift", "Pop"),
#         Cohort(4, "Nina Simone", "Jazz"),
#         Cohort(5, "The Beatles", "Rock"),
#     ]

# """
# When we call CohortRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/student_directory_2.sql")
#     repository = CohortRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Cohort(1, "Pixies", "Rock"),
#         Cohort(2, "ABBA", "Pop"),
#         Cohort(4, "Nina Simone", "Jazz"),
#     ]
