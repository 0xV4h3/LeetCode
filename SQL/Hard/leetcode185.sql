-- 185. Department Top Three Salaries
SELECT
    d.`name` `Department`,
    e1.`name` `Employee`,
    e1.`salary` `Salary`
FROM `Employee` e1
JOIN `Department` d ON e1.`departmentId` = d.`id`
WHERE e1.`salary` >= (
    SELECT MIN(`salary`)
    FROM (
        SELECT DISTINCT e2.`salary`
        FROM `Employee` e2
        WHERE e2.`departmentId` = e1.`departmentId`
        ORDER BY e2.`salary` DESC
        LIMIT 3
    ) top3
);