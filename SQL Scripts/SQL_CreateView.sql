-- Query to select user details along with related gender, department, and username
SELECT 
    u.userid,                         -- User's unique ID from 'Users' table
    u.firstname,                      -- User's first name from 'Users' table
    u.lastname,                       -- User's last name from 'Users' table
    u.date_of_birth,                  -- User's date of birth from 'Users' table
    g.gender,                         -- User's gender from 'Genders' table (joined via gender_id)
    d.dept,                           -- User's department from 'Departments' table (joined via deptid)
    m.username                        -- User's username from 'Username' table (joined via userid)
FROM Users u
LEFT JOIN Genders g ON g.gid = u.gender_id        -- Joining 'Genders' table to get the gender field
LEFT JOIN Departments d ON d.deptid = u.deptid    -- Joining 'Departments' table to get the department
LEFT JOIN Username m ON m.userid = u.userid;      -- Joining 'Username' table to get the username

-- Select everything from the view vw_UserDetails, which contains user details with gender, department, and username
SELECT * FROM vw_UserDetails;

-- Altering the view vw_UserDetails to ensure it includes the same user details with related gender, department, and username
ALTER VIEW vw_UserDetails
AS
SELECT 
    u.userid,                         -- User's unique ID from 'Users' table
	k.nom_kp,                         -- User's ID number from 'KadPengenalan' table
    u.firstname,                      -- User's first name from 'Users' table
    u.lastname,                       -- User's last name from 'Users' table
    u.date_of_birth,                  -- User's date of birth from 'Users' table
    g.gender,                         -- User's gender from 'Genders' table (joined via gender_id)
    d.dept,                           -- User's department from 'Departments' table (joined via deptid)
    m.username                        -- User's username from 'Username' table (joined via userid)
FROM Users u
LEFT JOIN Genders g ON g.gid = u.gender_id          -- Joining 'Genders' table to retrieve gender information
LEFT JOIN Departments d ON d.deptid = u.deptid      -- Joining 'Departments' table to retrieve department information
LEFT JOIN Username m ON m.userid = u.userid         -- Joining 'Username' table to retrieve username
LEFT JOIN KadPengenalan k ON k.userid = u.userid;   -- Joining 'KadPengenalan' table to retrieve ID number


-- Create a view for users in the 'Finance' department
CREATE VIEW vw_Finance AS
SELECT * FROM vw_UserDetails
WHERE dept = 'Finance';

-- Create a view for users in the 'Quality' department
CREATE VIEW vw_Quality AS
SELECT * FROM vw_UserDetails
WHERE dept = 'Quality';

-- Create a view for users in the 'Operations' department
CREATE VIEW vw_Operations AS
SELECT * FROM vw_UserDetails
WHERE dept = 'Operations';

-- Create a view for users in the 'Marketing' department
CREATE VIEW vw_Marketing AS
SELECT * FROM vw_UserDetails
WHERE dept = 'Marketing';

-- Create a view for users in the 'Information Technology' department
ALTER VIEW vw_InformationTechnology AS
SELECT * FROM vw_UserDetails
WHERE dept = 'Information Technology';

ALTER VIEW vw_UserDetails
AS
SELECT 
    u.userid,                         
	k.nom_kp,                         
    u.firstname,                      
    u.lastname,                       
    u.date_of_birth,                  
    COALESCE(g.gender, 'Not Specified') AS gender,  
    COALESCE(d.dept, 'Unknown') AS dept,  
    COALESCE(m.username, 'No Username') AS username  
FROM Users u
LEFT JOIN Genders g ON g.gid = u.gender_id         
LEFT JOIN Departments d ON d.deptid = u.deptid     
LEFT JOIN Username m ON m.userid = u.userid        
LEFT JOIN KadPengenalan k ON k.userid = u.userid;  

