## Exercise

Infer the table schema from these user stories.

```
As a coach
So I can get to know all students
I want to keep a list of students' names.

As a coach
So I can get to know all students
I want to assign tags to students (for example, "happy", "excited", etc).

As a coach
So I can get to know all students
I want to be able to assign the same tag to many different students.

As a coach
So I can get to know all students
I want to be able to assign many different tags to a student.
```

1. Copy the [Many-to-Many Design
   Recipe](../resources/two_tables_many_to_many_design_recipe_template.md) and
   use it to design the schema for the two tables and their join table.

# Two Tables (Many-to-Many) Design Recipe Template

_Copy this recipe template to design and create two related database tables having a Many-to-Many relationship._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORIES:

As a coach
So I can get to know all students
I want to keep a list of students' names.

As a coach
So I can get to know all students
I want to assign tags to students (for example, "happy", "excited", etc).

As a coach
So I can get to know all students
I want to be able to assign the same tag to many different students.

As a coach
So I can get to know all students
I want to be able to assign many different tags to a student.
```

```
Nouns:

students: student_id, student_name
tags: tag_id, tag_title
students_tags: student_id, tag_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties               |
| --------------------- | ------------------------ |
| students              | student_id, student_name |
| tags                  | tag_id, tag_title        |
| students_tags         | student_id, tag_id       |

1. Name of the first table (always plural): `students` 

    Column names: `student_id`, `student_name`

2. Name of the second table (always plural): `tags` 

    Column names: `tag_id`, `tag_title`

3. Name of the third table (always plural): `students_tags` 

    Column names: `student_id`, `tag_id`

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: students
student_id: SERIAL
student_name: text

Table: tags
tag_id: SERIAL
tag_title: text

```

## 4. Design the Many-to-Many relationship

Make sure you can answer YES to these two questions:

1. Can one student have many tags? Yes
2. Can one tag have many students? Yes


_If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case._

## 5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is `table1_table2`.

```
# EXAMPLE

Join table for tables: students and tags
Join table name: students_tags
Columns: student_id, tag_id
```


## 6. Write the SQL.

```sql
-- EXAMPLE
-- file: posts_tags.sql

-- Replace the table name, columm names and types.

| Record                | Properties               |
| --------------------- | ------------------------ |
| students              | student_id, student_name |
| tags                  | tag_id, tag_title        |
| students_tags         | student_id, tag_id       |

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

```

## 7. Create the tables.

```bash
psql -h 127.0.0.1 student_directory_2 < seeds/student_directory_2.sql
```



2. Create the tables by loading the SQL file in `psql`.