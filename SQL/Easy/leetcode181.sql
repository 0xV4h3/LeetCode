-- 181. Employees Earning More Than Their Managers
SELECT E.name AS Employee
FROM Employee E
INNER JOIN Employee M
ON E.managerId = M.id
WHERE E.salary > M.salary