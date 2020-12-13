-- use SQLite in this file

-- Q Workers
-- selects only the names of employees who are not managers
SELECT name FROM employees WHERE id NOT IN
(SELECT DISTINCT e1.id FROM employees e1 JOIN employees e2
 ON e1.id = e2.managerId)
 ;
-- I don't know why this is wrong:
SELECT name FROM employees WHERE id NOT IN
(SELECT managerId FROM employees)
;

-- Q Regional Sales Comparison
-- value and (max(value)-value)
-- SQLite not support RIGHT JOIN; use WITH for multiple times use
-- remember DISTINCT; care about when denominator is 0
WITH average AS (
    SELECT r.name as r_name,
    (CASE WHEN SUM(IFNULL(s.amount, 0)) = 0 THEN 0
     -- NB! use DISTINCT to get actual number of employees
     ELSE SUM(IFNULL(s.amount,0)) / COUNT(DISTINCT e.id) END) AS average
    FROM regions r
    LEFT JOIN states st ON r.id = st.regionId
    LEFT JOIN employees e ON st.id = e.stateId
    LEFT JOIN sales s ON e.id = s.employeeId
    GROUP BY r.Id
)
SELECT 
  r_name,
  average,
  (SELECT max(average) FROM average)- average AS difference
FROM average
;

-- Q Sessions
-- get average duration for userId who have more than 1 id
-- use GROUP BY and HAVING to filter
SELECT userId, SUM(duration)/COUNT(id)
FROM 'sessions' GROUP BY userId HAVING COUNT(id) > 1
;

-- Q Web Shop (easy)
SELECT i.name, s.name
FROM sellers s Join items i ON i.sellerId = s.id
WHERE s.rating > 4;

-- Q Pets
-- select distince names from two tables
SELECT DISTINCT name FROM
(SELECT DISTINCT name FROM dogs
UNION ALL
SELECT DISTINCT name FROM cats)
;

-- UNION will delete the duplicate terms
SELECT DISTINCT name FROM dogs
UNION
SELECT DISTINCT name FROM cats
;
