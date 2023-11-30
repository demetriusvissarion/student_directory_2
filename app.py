from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_directory_2.sql")

# Retrieve all cohorts
cohort_repository = CohortRepository(connection)
cohorts = cohort_repository.all()

# List them out
for cohort in cohorts:
    print(cohort)
