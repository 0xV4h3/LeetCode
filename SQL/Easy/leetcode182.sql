-- 182. Duplicate Emails
SELECT `email` Email
FROM    Person 
GROUP BY `email`
HAVING COUNT(*) > 1;
