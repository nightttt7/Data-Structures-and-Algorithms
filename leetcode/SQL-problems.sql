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
