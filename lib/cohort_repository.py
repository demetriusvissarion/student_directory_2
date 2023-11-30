from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all cohorts
    def all(self):
        rows = self._connection.execute('SELECT * from cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["cohort_name"], row["starting_date"])
            cohorts.append(item)
        return cohorts

    # Find a single cohort by their id
    def find(self, cohort_id):
        rows = self._connection.execute(
            'SELECT * from cohorts WHERE id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row["id"], row["cohort_name"], row["starting_date"])
    
    # Find a single student => change the query to only fetch specific data
    def find_with_students(self, cohort_id):
        rows = self._connection.execute(
            "SELECT * FROM cohorts JOIN students ON cohorts.id = students.cohort_id " \
            "WHERE cohorts.id = %s", [cohort_id])
        students = []
        for row in rows:
            student = Student(row["id"], row["student_name"], row["cohort_id"])
            students.append(student)

        # Each row has the same id, cohort_name, and starting_date, so we just use the first
        # print('Result: ', Cohort(rows[0]["id"], rows[0]["cohort_name"], rows[0]["starting_date"], students))
        return Cohort(rows[0]["id"], rows[0]["cohort_name"], rows[0]["starting_date"], students)

    # # Create a new cohort
    # # Do you want to get its id back? Look into RETURNING id;
    # def create(self, cohort):
    #     self._connection.execute('INSERT INTO cohorts (cohort_name, starting_date) VALUES (%s, %s)', [cohort.cohort_name, cohort.starting_date])
    #     return None

    # # Delete an cohort by their id
    # def delete(self, cohort_id):
    #     self._connection.execute(
    #         'DELETE FROM cohorts WHERE id = %s', [cohort_id])
    #     return None

# Table: cohorts
# id: SERIAL
# cohort_name: text
# starting_date: date

# Table: students
# id: SERIAL
# student_name: text
# cohort_id: text