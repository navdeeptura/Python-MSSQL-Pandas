SELECT 
	si.first_name, 
	si.last_name, 
	sb.name as subject_name, 
	sm.marks 
FROM student_information si 
JOIN students_marks sm ON sm.student_id = si.id
JOIN subjects sb ON sm.subject_id = sb.id
WHERE sm.marks < 33
GROUP BY si.first_name;

SELECT 
    si.first_name, 
    si.last_name,
    MIN(sm.marks) AS lowest_mark
FROM student_information si
JOIN students_marks sm ON sm.student_id = si.id
WHERE sm.marks < 33
GROUP BY si.first_name, si.last_name;

SELECT 
    si.first_name, 
    si.last_name, 
    COUNT(*) AS failed_subjects
FROM student_information si
JOIN students_marks sm ON sm.student_id = si.id
WHERE sm.marks < 33
GROUP BY si.first_name, si.last_name;


SELECT si.id, si.first_name, si.last_name, sb.name as subject_name, sm.marks
FROM students_marks sm
JOIN student_information si ON si.id = sm.student_id
JOIN subjects sb ON sb.id = sm.subject_id

SELECT sm.student_id, si.first_name,
FROM student_information si
JOIN students_marks sm ON si.id = sm.student_id
WHERE marks > 33; 

UPDATE student_information SET first_name = 'SIMRAN', last_name = 'BAN' where id = 7;

SELECT DISTINct count(*),TEMP.TotalSubject FROM(
SELECT DISTINCT student_id,count(subject_id) AS TotalSubject FROM students_marks
--WHERE marks > 33
GROUP BY student_id) TEMP
inner JOIN students_marks sm ON TEMP.student_id=sm.student_id
WHERE sm.marks>33 and sm.student_id=1



SELECT * FROM students_marks WHERE student_id=1



SELECT 
    sm.student_id
FROM students_marks sm
GROUP BY sm.student_id
HAVING COUNT(student_id) = SUM(CASE WHEN sm.marks >= 33 THEN 1 ELSE 0 END);
        6  sum(1+1+1+1+1+0+1) 6=5

1  6    5+1