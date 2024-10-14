-- Insert into table Genders
INSERT INTO Genders (gender) VALUES ('Male'), ('Female');

--Insert into table Departments
INSERT INTO Departments (dept) 
VALUES 
    ('Human Resources'),
    ('Finance'),
    ('Information Technology'),
    ('Operations'),
    ('Marketing'),
	('Quality');


SELECT TOP 10 *
FROM Users
ORDER BY userid DESC

INSERT INTO Users (firstname, lastname, date_of_birth, gender_id, deptid)
VALUES ('Fiona', 'McFly', '1999-03-07', 300, 12);

SELECT * FROM vw_UserDetails
WHERE username IS NULL
OR nom_kp IS NULL