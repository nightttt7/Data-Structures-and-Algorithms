-- Q175
-- use LEFT JOIN to show all person even has no address
-- very common interview question
SELECT FirstName, LastName, City, State
FROM Person LEFT JOIN Address
ON Person.PersonID = Address.PersonID
;

-- Q176
-- use the outer SELECT to return NULL if there is no second highest salary
SELECT
(SELECT DISTINCT Salary AS SecondHighestSalary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1)
AS SecondHighestSalary
;

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
SELECT Score, DENSE_RANK() OVER(ORDER BY Score DESC) AS 'Rank' FROM Scores

-- Q180
-- find all numbers that appear at least three times consecutively
-- use l1, l2, l3 as alias for table logs
SELECT DISTINCT l1.Num AS ConsecutiveNums FROM Logs l1, Logs l2, Logs l3
WHERE l1.Id = l2.Id-1 AND l2.Id = l3.Id - 1 AND l1.Num = l2.Num AND l2.Num = l3.Num

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
SELECT DepartmentId, MAX(Salary) FROM Employee GROUP BY DepartmentId
-- then select employee whose salary in inner query
