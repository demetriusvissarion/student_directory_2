class Cohort:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, cohort_name, starting_date, students = []):
        self.id = id
        self.cohort_name = cohort_name
        self.starting_date = starting_date
        self.students = students

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Cohort
    def __repr__(self):
        return f"Cohort({self.id}, {self.cohort_name}, {self.starting_date})"

# Table: cohorts
# id: SERIAL
# cohort_name: text
# starting_date: date

# Table: students
# id: SERIAL
# student_name: text
# cohort_id: text
