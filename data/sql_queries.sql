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

Select * from student_information;