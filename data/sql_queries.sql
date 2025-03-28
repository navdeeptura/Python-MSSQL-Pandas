--create database StudentsDatabase;

--USE StudentsDatabase;

CREATE TABLE student_information(
	id	INT PRIMARY KEY IDENTITY(1,1),
	first_name	VARCHAR(50)	NOT NULL,
	last_name	VARCHAR(50) NOT NULL,
	phone	VARCHAR(15),
	address	VARCHAR(250),
	city	VARCHAR(50),
	created_at DATETIME DEFAULT GETDATE()
);

ALTER TABLE student_information
	ADD created_at DATETIME DEFAULT GETDATE();

INSERT INTO student_information (first_name, last_name, phone, address, city)
VALUES ('Navdeep', 'Tu', '9999999999', 'Taysham Crescent', 'Etobicoke');

INSERT INTO student_information (first_name, last_name, phone, address, city) VALUES ('RAMAN', 'Tu', '7777777777', 'financial drive', 'brampton');

Select * from student_information;

UPDATE student_information SET first_name = 'NIYA', last_name = 'TU',
    phone = '6666666666', address = 'Long more Road 2', city = 'Mississauga'
    WHERE (first_name = 'NIYA' and last_name = 'TUR');
Select * from student_information;

CREATE TABLE subjects(
	id	INT PRIMARY KEY IDENTITY(1,1),
	name	VARCHAR(100),
	code	VARCHAR(50),
	department	VARCHAR(100)
);
INSERT INTO subjects(name, code, department) VALUES ('Project Management', 'PMC100', 'Information Technology');
INSERT INTO subjects (name, code, department) VALUES
('Database Systems', 'DBS101', 'Information Technology'),
('Operating Systems', 'OPS102', 'Information Technology'),
('Cybersecurity Fundamentals', 'CYB110', 'Information Technology'),
('Software Engineering', 'SWE120', 'Computer Science'),
('Artificial Intelligence', 'AI130', 'Computer Science'),
('Network Administration', 'NET140', 'Information Technology'),
('Data Structures and Algorithms', 'DSA150', 'Computer Science'),
('Cloud Computing', 'CLC160', 'Information Technology'),
('Human-Computer Interaction', 'HCI170', 'Computer Science');

SELECT * FROM subjects;


CREATE TABLE students_marks(
	student_id INT NOT NULL,
	subject_id INT NOT NULL,
	total_marks	INT	NOT NULL,
	passing_marks INT NOT NULL,
	marks	INT,
	PRIMARY KEY (student_id, subject_id),
	FOREIGN KEY (student_id) REFERENCES student_information(id),
	FOREIGN KEY (subject_id)	REFERENCES subjects(id)
);

INSERT INTO students_marks (student_id, subject_id, total_marks, passing_marks, marks)
VALUES (10, 3, 100, 33, 45);
SELECT * FROM students_marks;

