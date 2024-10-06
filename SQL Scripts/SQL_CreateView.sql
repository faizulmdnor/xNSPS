-- Select user details with related gender, department, and username
SELECT 
    u.userid,                         -- User ID from 'Users' table
    u.firstname,                      -- First name from 'Users' table
    u.lastname,                       -- Last name from 'Users' table
    u.date_of_birth,                  -- Date of birth from 'Users' table
    g.gender,                         -- Gender from 'Genders' table (joined using gender_id)
    d.dept,                           -- Department from 'Departments' table (joined using deptid)
    m.username                        -- Username from 'Username' table (joined using userid)
FROM Users u
LEFT JOIN Genders g ON g.gid = u.gender_id        -- Left join 'Genders' table to get gender
LEFT JOIN Departments d ON d.deptid = u.deptid    -- Left join 'Departments' table to get department
LEFT JOIN Username m ON m.userid = u.userid;      -- Left join 'Username' table to get username

-- Alter the view vw_UserDetails to reflect the same user details with related gender, department, and username
ALTER VIEW vw_UserDetails
AS
SELECT 
    u.userid,                         -- User ID from 'Users' table
    u.firstname,                      -- First name from 'Users' table
    u.lastname,                       -- Last name from 'Users' table
    u.date_of_birth,                  -- Date of birth from 'Users' table
    g.gender,                         -- Gender from 'Genders' table (joined using gender_id)
    d.dept,                           -- Department from 'Departments' table (joined using deptid)
    m.username                        -- Username from 'Username' table (joined using userid)
FROM Users u
LEFT JOIN Genders g ON g.gid = u.gender_id        -- Left join 'Genders' table to get gender
LEFT JOIN Departments d ON d.deptid = u.deptid    -- Left join 'Departments' table to get department
LEFT JOIN Username m ON m.userid = u.userid;      -- Left join 'Username' table to get username
