from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all cohorts
    def all(self):
        print('reached all************************')
        rows = self._connection.execute('SELECT * from cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(item)
        return cohorts

    # Find a single cohort by their id
    def find(self, cohort_id):
        rows = self._connection.execute(
            'SELECT * from cohorts WHERE id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row["id"], row["name"], row["starting_date"])
    
    # Find a single student => change the query to only fetch specific data
    def find_with_students(self, student_id):
        rows = self._connection.execute(
            "SELECT students.id as student_id, students.name, students.cohort_id, cohorts.id AS cohort_id, cohorts.name, cohorts.starting_date " \
            "FROM students JOIN cohorts ON students.cohort_id = cohorts.id " \
            "WHERE students.cohort_id = %s", [student_id])
        students = []
        for row in rows:
            student = Student(row["student_id"], row["name"], row["cohort_id"])
            students.append(student)

        # Each row has the same id, name, and genre, so we just use the first
        return Cohort(rows[0]["cohort_id"], rows[0]["name"], rows[0]["starting_date"], students)

    # Create a new cohort
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, cohort):
        self._connection.execute('INSERT INTO cohorts (name, starting_date) VALUES (%s, %s)', [cohort.name, cohort.starting_date])
        return None

    # Delete an cohort by their id
    def delete(self, cohort_id):
        self._connection.execute(
            'DELETE FROM cohorts WHERE id = %s', [cohort_id])
        return None


# Table: students
# id: SERIAL
# name: text
# cohort: text

# Table: cohorts
# id: SERIAL
# name: text
# starting_date: date

# Students names
# Cohorts names
# Cohorts starting dates
# Students cohort names