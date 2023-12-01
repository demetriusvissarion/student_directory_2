DROP TABLE IF EXISTS cohorts CASCADE;
CREATE TABLE cohorts (
  cohort_id SERIAL PRIMARY KEY,
  cohort_name VARCHAR(255),
  starting_date DATE
);

DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
  student_id SERIAL PRIMARY KEY,
  student_name VARCHAR(255),
  cohort_id INTEGER,
  constraint fk_cohort foreign key(cohort_id) references cohorts(cohort_id) on delete cascade
);

DROP TABLE IF EXISTS tags CASCADE;
CREATE TABLE tags (
  tag_id SERIAL PRIMARY KEY,
  tag_title VARCHAR(255)
);

DROP TABLE IF EXISTS student_tags CASCADE;
CREATE TABLE student_tags (
  student_id int,
  tag_id int,
  constraint fk_student foreign key(student_id) references students(student_id) on delete cascade,
  constraint fk_tag foreign key(tag_id) references tags(tag_id) on delete cascade,
  PRIMARY KEY (student_id, tag_id)
);

-- | Record                | Properties                    |
-- | --------------------- | ----------------------------- |
-- | cohorts               | id, cohort_name, starting_date|
-- | students              | student_id, student_name      |
-- | tags                  | tag_id, tag_title             |
-- | students_tags         | student_id, tag_id            |

-- Finally, we add any records that are needed for the tests to run
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Cohort 1', '2023-11-28');
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Cohort 2', '2023-11-29');
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('Cohort 3', '2023-11-30');

INSERT INTO students (student_name, cohort_id) VALUES ('Mike', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Joe', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Tom', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Will', 2);
INSERT INTO students (student_name, cohort_id) VALUES ('Pete', 3);
INSERT INTO students (student_name, cohort_id) VALUES ('Sam', 3);
INSERT INTO students (student_name, cohort_id) VALUES ('John', 3);
INSERT INTO students (student_name, cohort_id) VALUES ('Chris', 3);

INSERT INTO tags (tag_title) VALUES ('happy');
INSERT INTO tags (tag_title) VALUES ('sad');
INSERT INTO tags (tag_title) VALUES ('nervous');
INSERT INTO tags (tag_title) VALUES ('excited');

INSERT INTO student_tags (student_id, tag_id) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 3),
(6, 2),
(7, 1),
(6, 3),
(2, 4),
(3, 4);

ALTER TABLE student_tags ADD FOREIGN KEY (tag_id) REFERENCES tags(tag_id);
ALTER TABLE student_tags ADD FOREIGN KEY (student_id) REFERENCES students(student_id);