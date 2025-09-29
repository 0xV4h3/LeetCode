-- 184. Department Highest Salary
SELECT d.`name` Department, e.`name` Employee, e.Salary 
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
WHERE e.Salary = (
    SELECT MAX(Salary) 
    FROM Employee 
    WHERE DepartmentId = d.Id
);