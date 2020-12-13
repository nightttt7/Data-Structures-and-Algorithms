-- Q175
-- use LEFT JOIN to show all person even has no address
-- very common interview question
SELECT FirstName, LastName, City, State
FROM Person
  LEFT JOIN Address ON Person.PersonID = Address.PersonID;

-- Q176
-- use the outer SELECT to return NULL if there is no second highest salary
SELECT (
    SELECT DISTINCT Salary AS SecondHighestSalary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1
  ) AS SecondHighestSalary;

-- Q177
-- know how to create a function
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N-1;
  RETURN (
    SELECT
      (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET M)
  );
END

-- Q178
-- DENSE_RANK() OVER(ORDER BY x [DESC]), return the rank or DESC rank of x
-- Unlike the RANK() function, the DENSE_RANK() function always returns consecutive rank values.
SELECT Score, DENSE_RANK() OVER(ORDER BY Score DESC) AS 'Rank' FROM Scores;

-- Q180
-- find all numbers that appear at least three times consecutively
-- use l1, l2, l3 as alias for table logs
SELECT DISTINCT l1.Num AS ConsecutiveNums FROM Logs l1, Logs l2, Logs l3
WHERE l1.Id = l2.Id-1 AND l2.Id = l3.Id - 1 AND l1.Num = l2.Num AND l2.Num = l3.Num;

-- Q181
-- Still alias for table
SELECT e1.Name AS 'Employee' FROM Employee e1, Employee e2
WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary;

-- Use JOIN
SELECT e1.NAME AS Employee FROM Employee AS e1
JOIN Employee AS e2
ON e1.ManagerId = e2.Id AND e1.Salary > e2.Salary;

-- Q182
-- find all duplicate, use HAVING after GROUP BY
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1;

-- Q183
-- sub-query and NOT IN
SELECT customers.name AS 'Customers' FROM customers WHERE customers.id NOT IN
(select customerid from orders);

-- Q184
-- use sub-query
-- inner query:
SELECT DepartmentId, MAX(Salary) FROM Employee GROUP BY DepartmentId;
-- then select employee whose salary in inner query

-- Q185
-- 'PARTITION BY' just like 'GROUP BY'
SELECT DepartmentId, Name, Salary FROM
(SELECT e.*, DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC)
AS DeptPayRank FROM Employee e) AS a
WHERE DeptPayRank <=3;
-- Then change to join department name

-- Q196
-- DELETE duplicate
-- WHERE sentence "keeping only unique emails based on its smallest Id"
DELETE p1 FROM Person p1, Person p2 WHERE p1.Email = p2.Email AND p1.Id > p2.Id;

-- Another way, use ROW_NUMBER(), inner query:
DELETE ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) rownum FROM person;

-- Q197
-- higher temperature compared to its previous dates (yesterday)
-- similar way with Q180
SELECT w1.id FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.Temperature > w2.Temperature;

-- use JOIN, but algorithm is the same, faster!
SELECT w1.id FROM Weather w1 JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.Temperature > w2.Temperature;

-- Q262 hard
-- cancellation rate (two decimal), unbanned users, between Oct 1, 2013 and Oct 3, 2013
-- IF function (just like if else in Python), GROUP BY
SELECT Request_at AS 'Day',
ROUND(SUM(IF(status = 'completed', 0, 1)) / COUNT(*), 2) as 'Cancellation Rate'
FROM Trips WHERE
Client_Id NOT IN (SELECT Users_ID FROM Users Where Banned = 'Yes')
AND Driver_Id NOT IN (SELECT Users_ID FROM Users Where Banned = 'Yes')
AND (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
GROUP BY Request_at;

-- Q595 easy
SELECT name, population, area FROM World WHERE population > 25000000 OR area > 3000000;

-- Q596 easy
-- But must use DISTINCT, there may be duplicate student names in one class
SELECT class FROM 
(SELECT class, COUNT(DISTINCT student) AS class_count FROM courses GROUP BY class) AS temp
WHERE class_count >= 5;

-- Use HAVING
SELECT class FROM courses GROUP BY class HAVING COUNT(DISTINCT student) >= 5;

-- Q601 hard
-- consecutive, similar way with Q180
-- dont forget DISTINCT, ORDER BY
SELECT DISTINCT s1.* FROM Stadium s1, Stadium s2, Stadium s3
WHERE s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100 AND (
(s1.id+1 = s2.id AND s1.id+2 = s3.id) OR
(s1.id-1 = s2.id AND s1.id+1 = s3.id) OR
(s1.id-1 = s2.id AND s1.id-2 = s3.id))
ORDER BY s1.id;

-- Q620
-- use 'MOD'
SELECT * FROM cinema WHERE MOD(id, 2) = 1 AND description != 'boring'
ORDER BY rating DESC;

-- Q626
-- keypoint is how to deal with the max odd
-- find the id that is the max, but must use sub-query to get (select MAX(id) from seat)
SELECT IF(MOD(seat.id, 2)=0, seat.id-1, IF(seat.id=(select MAX(id) from seat) , seat.id, seat.id+1)) AS id, student FROM seat ORDER BY id;

-- or use XOR operator ^ in SQL, id+1^1-1 will change 1 to 2, 2 to 1, 3 to 4, 4 to 3
-- XOR: Convert to binary and then XOR, 0 is FALSE and 1 is TRUE
-- COALESCE: the first NOT NULL value of inputs
SELECT s1.id, COALESCE(s2.student, s1.student) AS student FROM seat s1 LEFT JOIN seat s2
ON ((s1.id + 1) ^ 1) - 1 = s2.id ORDER BY s1.id;

-- Q627 easy
-- update table
UPDATE salary SET sex=IF(sex='m', 'f', 'm');

-- Q1179
-- use many LEFT JOIN for query below
SELECT id, revenue as Jan_Revenue FROM Department d1 WHERE month='Jan';
-- complete solution, pay attention to (SELECT DISTINCT id FROM Department)
SELECT d.id,
  d_jan.revenue AS Jan_Revenue,
  d_feb.revenue AS Feb_Revenue,
  d_mar.revenue AS Mar_Revenue,
  d_apr.revenue AS Apr_Revenue,
  d_may.revenue AS May_Revenue,
  d_jun.revenue AS Jun_Revenue,
  d_jul.revenue AS Jul_Revenue,
  d_aug.revenue AS Aug_Revenue,
  d_sep.revenue AS Sep_Revenue,
  d_oct.revenue AS Oct_Revenue,
  d_nov.revenue AS Nov_Revenue,
  d_dec.revenue AS Dec_Revenue
FROM (SELECT DISTINCT id FROM Department) AS d
  LEFT JOIN Department d_jan ON d_jan.id = d.id AND d_jan.month = 'Jan'
  LEFT JOIN Department d_feb ON d_feb.id = d.id AND d_feb.month = 'Feb'
  LEFT JOIN Department d_mar ON d_mar.id = d.id AND d_mar.month = 'Mar'
  LEFT JOIN Department d_apr ON d_apr.id = d.id AND d_apr.month = 'Apr'
  LEFT JOIN Department d_may ON d_may.id = d.id AND d_may.month = 'May'
  LEFT JOIN Department d_jun ON d_jun.id = d.id AND d_jun.month = 'Jun'
  LEFT JOIN Department d_jul ON d_jul.id = d.id AND d_jul.month = 'Jul'
  LEFT JOIN Department d_aug ON d_aug.id = d.id AND d_aug.month = 'Aug'
  LEFT JOIN Department d_sep ON d_sep.id = d.id AND d_sep.month = 'Sep'
  LEFT JOIN Department d_oct ON d_oct.id = d.id AND d_oct.month = 'Oct'
  LEFT JOIN Department d_nov ON d_nov.id = d.id AND d_nov.month = 'Nov'
  LEFT JOIN Department d_dec ON d_dec.id = d.id AND d_dec.month = 'Dec';

-- or use GROUP BY
-- pay attention to MAX(), for each group we need to find the only no null value
SELECT id,
  MAX(IF(month = 'Jan', revenue, NULL)) AS Jan_Revenue,
  MAX(IF(month = 'Feb', revenue, NULL)) AS Feb_Revenue,
  MAX(IF(month = 'Mar', revenue, NULL)) AS Mar_Revenue,
  MAX(IF(month = 'Apr', revenue, NULL)) AS Apr_Revenue,
  MAX(IF(month = 'May', revenue, NULL)) AS May_Revenue,
  MAX(IF(month = 'Jun', revenue, NULL)) AS Jun_Revenue,
  MAX(IF(month = 'Jul', revenue, NULL)) AS Jul_Revenue,
  MAX(IF(month = 'Aug', revenue, NULL)) AS Aug_Revenue,
  MAX(IF(month = 'Sep', revenue, NULL)) AS Sep_Revenue,
  MAX(IF(month = 'Oct', revenue, NULL)) AS Oct_Revenue,
  MAX(IF(month = 'Nov', revenue, NULL)) AS Nov_Revenue,
  MAX(IF(month = 'Dec', revenue, NULL)) AS Dec_Revenue
FROM Department
GROUP BY id;

-- Q511
-- Game Play Analysis 1
-- 1. first login date
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;

-- Q512
-- Game Play Analysis 2
-- first device for each player
-- sub-query
SELECT player_id, device_id
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT player_id,
      MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
  );

-- FIRST_VALUE and PARTITION BY
-- must add DISTINCT
SELECT DISTINCT player_id,
  FIRST_VALUE(device_id) OVER (
    PARTITION BY player_id
    ORDER BY event_date
  ) AS device_id
FROM Activity;

-- Q534
-- Game Play Analysis 3
-- self join is useful, get cumsum
SELECT a1.player_id, a1.event_date,
  SUM(a2.games_played) AS games_played_so_far
FROM Activity a1
  Join Activity a2 ON a1.player_id = a2.player_id
  AND a1.event_date >= a2.event_date
GROUP BY a1.player_id,
  a1.event_date;

-- Q550
-- Game Play Analysis 4
-- if julianday worked, use it
-- use * 1.0 to get float
SELECT ROUND(
    SUM(
      CASE
        WHEN a1.event_date - a2.first_login = 1 THEN 1
        ELSE 0
      END
    ) * 1.0 / COUNT(DISTINCT a1.player_id),
    2
  ) AS fraction
FROM Activity a1
  Join (
    SELECT player_id,
      MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
  ) a2 ON a1.player_id = a2.player_id;

-- Q569
-- Median Employee Salary
-- how to use WITH
-- use ROW_NUMBER(continous and unique) but not RANK(skip the rank) or DENSE_RANK(continuous but duplicate rank)
WIth c AS (SELECT Company, COUNT(Salary) AS c FROM Employee GROUP BY Company),
     r AS (SELECT Id, Company, Salary,
           ROW_NUMBER() OVER(PARTITION BY Company ORDER BY Salary) AS r 
           FROM Employee)
SELECT r.Id, r.Company, r.Salary FROM r join c on r.Company = c.Company
WHERE r.r in (MAX(c.c/2, (c.c+1)/2), c.c/2+1);

-- Q570 easy
SELECT e1.name
FROM Employee e1
  JOIN Employee e2 ON e1.id = e2.Managerid
GROUP BY e1.id
HAVING COUNT(e2.id) >= 5;

-- Q574
-- DESC: from big to small
SELECT Name
FROM Candidate
WHERE id = (
    SELECT CandidateId
    FROM Vote
    GROUP BY CandidateId
    ORDER BY COUNT(CandidateId) DESC
    LIMIT 1
  );

-- Q579
-- Cumulative Sum
SELECT e1.Id, e1.Month, SUM(e2.Salary) AS Salary
FROM Employee e1
  JOIN Employee e2 ON e1.Id = e2.Id
  AND e1.Month - e2.Month BETWEEN 0 AND 2
GROUP BY e1.Id,
  e1.Month
HAVING (e1.Id, e1.Month) NOT IN (
    SELECT Id, MAX(Month)
    FROM Employee
    GROUP BY Id
  )
ORDER BY e1.Id,
  e1.Month DESC;

-- Q580 easy
-- Student Number in Departments
SELECT d.dept_name,
  count(s.student_id)
FROM department d
  LEFT JOIN student s On s.dept_id = d.dept_id
GROUP BY d.dept_id;

-- Q585
-- sum of all total investment values in 2016
WITH c1 AS (
  SELECT TIV_2015
  FROM insurance
  GROUP BY TIV_2015
  HAVING COUNT(PID) > 1
),
c2 AS (
  SELECT LAT, LON
  FROM insurance
  GROUP BY LAT, LON
  HAVING COUNT(PID) = 1
)
SELECT ROUND(SUM(TIV_2016) * 1.0, 2) AS TIV_2016
FROM insurance
WHERE TIV_2015 in c1
  AND (LAT, LON) in c2;
