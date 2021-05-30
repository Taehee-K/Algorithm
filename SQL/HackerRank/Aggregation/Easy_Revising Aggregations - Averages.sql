-- [HackerRank Easy/SQL] Revising Aggregations - Averages
-- https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem

SELECT SUM(POPULATION)/COUNT(POPULATION)
FROM CITY
WHERE DISTRICT = 'California'