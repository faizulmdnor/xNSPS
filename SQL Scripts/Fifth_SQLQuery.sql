CREATE TABLE Region2(
	trans_id INT PRIMARY KEY IDENTITY(1010001, 1),
	date DATE,
	Region_name VARCHAR(20),
	Revenue MONEY
)

drop table Region
SELECT * FROM Region

SELECT region_name, SUM(revenue) AS total_revenue
FROM region
WHERE date > DATEADD(day, -28, GETDATE())
GROUP BY region_name
ORDER BY total_revenue DESC
OFFSET 4 ROWS FETCH NEXT 1 ROW ONLY;


SELECT * FROM Region2



SELECT region_name, SUM(revenue) AS total_revenue
FROM region2
WHERE date > DATEADD(day, -28, GETDATE())
GROUP BY region_name
ORDER BY total_revenue DESC

SELECT region_name, SUM(revenue) AS total_revenue
FROM region2
WHERE date > DATEADD(day, -28, GETDATE())
GROUP BY region_name
ORDER BY total_revenue DESC
OFFSET 4 ROWS FETCH NEXT 1 ROW ONLY;