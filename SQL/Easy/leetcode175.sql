-- 175. Combine Two Tables
SELECT P.firstName, P.lastName, A.city, A.state
FROM  Person AS P
LEFT JOIN Address AS A ON A.personId = P.personId 