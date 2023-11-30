DROP TABLE IF EXISTS cohorts CASCADE;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 1', '2023-11-28');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 2', '2023-11-29');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 3', '2023-11-30');

INSERT INTO students (name, cohort_id) VALUES ('Mike', 1);
INSERT INTO students (name, cohort_id) VALUES ('Joe', 1);
INSERT INTO students (name, cohort_id) VALUES ('Tom', 1);
INSERT INTO students (name, cohort_id) VALUES ('Will', 2);
INSERT INTO students (name, cohort_id) VALUES ('Pete', 3);
INSERT INTO students (name, cohort_id) VALUES ('Sam', 3);
INSERT INTO students (name, cohort_id) VALUES ('John', 3);
INSERT INTO students (name, cohort_id) VALUES ('Chris', 3);