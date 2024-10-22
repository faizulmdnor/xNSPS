WITH SiteTotals AS (
    SELECT 
        s.site_id,
        COUNT(e.emp_id) as total_employees_per_site
    FROM Employees e
    LEFT JOIN Sites s ON s.site_id = e.site_id
    WHERE e.status_id = 1
    GROUP BY s.site_id
)
SELECT 
    s.Site,
    p.Position,
    d.Department,
    COUNT(e.emp_id) as num_of_position,
    st.total_employees_per_site
FROM Employees e
LEFT JOIN Positions p ON p.pos_id = e.pos_id
LEFT JOIN Departments d ON d.dept_id = p.dept_id
LEFT JOIN Sites s ON s.site_id = e.site_id
LEFT JOIN SiteTotals st ON st.site_id = s.site_id
WHERE e.status_id = 1
GROUP BY s.Site, p.Position, d.Department, st.total_employees_per_site
ORDER BY s.Site, d.Department, p.Position, num_of_position;
