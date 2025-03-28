--SELECT sm.student_id, si.first_name, si.last_name, sm.marks from students_marks sm JOIN student_information si ON si.id = sm.student_id;

SELECT TOP 10
	sm.student_id, 
	si.first_name + ' ' + si.last_name as full_name, 
	sm.marks
FROM students_marks sm 
JOIN student_information si ON si.id = sm.student_id
ORDER BY marks DESC;

SELECT sm.student_id, si.first_name + ' ' + si.last_name as full_name, SUM(sm.total_marks) as total, SUM(sm.marks) as marks, 
CAST(SUM(sm.marks)  AS FLOAT) / CAST(SUM(sm.total_marks) AS FLOAT) * 100 AS Percentage
FROM students_marks sm
JOIN student_information si ON si.id = sm.student_id
GROUP BY student_id, first_name, si.last_name
ORDER BY Percentage DESC


select * from student_information
select * from subjects
select * from students_marks



select DISTINCt si.id, si.first_name,count(su.name) from student_information si
inner join students_marks sm on si.id=sm.student_id
--inner join subjects su on sm.subject_id=su.id
group by si.id,si.first_name
