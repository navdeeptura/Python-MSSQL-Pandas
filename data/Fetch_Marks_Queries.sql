USE StudentsDatabase;
SELECT * FROM students_marks;
Select id, first_name, last_name FROM student_information where id in 
(Select DISTINCT student_id from students_marks where marks > 33);

SELECT * FROM subjects